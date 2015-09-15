#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "CATTools/DataFormats/interface/Muon.h"
#include "CATTools/DataFormats/interface/Electron.h"
#include "CATTools/DataFormats/interface/Jet.h"
#include "CATTools/DataFormats/interface/MET.h"
#include "CATTools/DataFormats/interface/SecVertex.h"

#include "CATTools/CatAnalyzer/interface/KinematicSolvers.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
//#include "DataFormats/Candidate/interface/CompositeCandidate.h"
//#include "DataFormats/Candidate/interface/CompositeRefCandidate.h"
#include "DataFormats/Candidate/interface/CompositePtrCandidate.h"
#include "CommonTools/Utils/interface/PtComparator.h"

using namespace std;

namespace cat {

class TTbarDileptonKinSolutionProducer : public edm::stream::EDProducer<>
{
public:
  TTbarDileptonKinSolutionProducer(const edm::ParameterSet& pset);
  virtual ~TTbarDileptonKinSolutionProducer() {};
  void produce(edm::Event & event, const edm::EventSetup&) override;

private:
  typedef cat::Muon TMuon;
  typedef cat::Electron TElectron;;
  typedef cat::Jet TJet;
  typedef cat::MET TMET;
  edm::EDGetTokenT<edm::View<reco::CandidatePtr> > leptonToken_;
  edm::EDGetTokenT<edm::View<reco::CandidatePtr> > jetToken_;
  edm::EDGetTokenT<float> metToken_, metphiToken_;

private:
  typedef reco::Candidate::LorentzVector LV;
  typedef reco::LeafCandidate Cand;
  typedef std::vector<Cand> CandColl;
  typedef std::vector<float> floats;
  std::unique_ptr<KinematicSolver> solver_;

};

}

using namespace cat;

TTbarDileptonKinSolutionProducer::TTbarDileptonKinSolutionProducer(const edm::ParameterSet& pset)
{
  leptonToken_ = consumes<edm::View<reco::CandidatePtr> >(pset.getParameter<edm::InputTag>("leptons"));
  jetToken_ = consumes<edm::View<reco::CandidatePtr> >(pset.getParameter<edm::InputTag>("jets"));
  metToken_ = consumes<float>(pset.getParameter<edm::InputTag>("met"));
  metphiToken_ = consumes<float>(pset.getParameter<edm::InputTag>("metphi"));

  auto solverName = pset.getParameter<std::string>("solver");
  std::transform(solverName.begin(), solverName.end(), solverName.begin(), ::toupper);
  if      ( solverName == "CMSKIN" ) solver_.reset(new CMSKinSolver());
  else if ( solverName == "DESYMASSLOOP" ) solver_.reset(new DESYMassLoopSolver());
  else if ( solverName == "DESYSMEARED" ) solver_.reset(new DESYSmearedSolver());
  else if ( solverName == "MT2"    ) solver_.reset(new MT2Solver());
  else if ( solverName == "MAOS"   ) solver_.reset(new MAOSSolver());
  else if ( solverName == "NUWGT"  ) solver_.reset(new NuWeightSolver());
  else {
    cerr << "The solver name\"" << pset.getParameter<std::string>("solver") << "\" is not known please check spellings.\n";
    solver_.reset(new TTDileptonSolver()); // A dummy solver
  }

  produces<CandColl>();

  produces<floats>("aux");
  produces<floats>("mLL");
  produces<floats>("mLB");
  produces<floats>("mAddJJ");
  produces<floats>("dphi");
}

void TTbarDileptonKinSolutionProducer::produce(edm::Event& event, const edm::EventSetup&)
{
  std::auto_ptr<CandColl> cands(new CandColl);
  //auto candsRefProd = event.getRefBeforePut<CRCandColl>();

  std::auto_ptr<floats> out_aux(new floats);
  std::auto_ptr<floats> out_mLL(new floats);
  std::auto_ptr<floats> out_mLB(new floats);
  std::auto_ptr<floats> out_mAddJJ(new floats);
  std::auto_ptr<floats> out_dphi(new floats);

  edm::Handle<edm::View<reco::CandidatePtr> > leptonHandle;
  event.getByToken(leptonToken_, leptonHandle);

  edm::Handle<edm::View<reco::CandidatePtr> > jetHandle;
  event.getByToken(jetToken_, jetHandle);

  edm::Handle<float> metHandle;
  event.getByToken(metToken_, metHandle);
  const float met = *metHandle;
  event.getByToken(metphiToken_, metHandle);
  const float metphi = *metHandle;
  const LV metLV(met*cos(metphi), met*sin(metphi), 0, met);

  do {
    // Check objects to exist
    if ( leptonHandle->size() < 2 ) break;
    if ( jetHandle->size() < 2 ) break;

    // Pick leading leptons.
    const auto lep1 = leptonHandle->at(0);
    const auto lep2 = leptonHandle->at(1);
    const LV lep1LV = lep1->p4();
    const LV lep2LV = lep2->p4();
    LV inputLV[5] = {metLV, lep1LV, lep2LV};
    LV nu1LV, nu2LV;
    double quality = -1e9; // Default quality value

    // Run the solver with all jet combinations
    reco::CandidatePtr selectedJet1, selectedJet2;
    for ( auto jet1 : *jetHandle )
    {
      inputLV[3] = jet1->p4();
      for ( auto jet2 : *jetHandle )
      {
        if ( jet1 == jet2 ) continue;
        inputLV[4] = jet2->p4();

        solver_->solve(inputLV);
        if ( solver_->quality() > quality )
        {
          quality = solver_->quality();
          selectedJet1 = jet1;
          selectedJet2 = jet2;
          nu1LV = solver_->nu1();
          nu2LV = solver_->nu2();
        }
      }
    }
    if ( quality <= -1e9 ) break; // failed to get solution

    // Redo the calculation with the selected ones to update internal variables
    inputLV[3] = selectedJet1->p4();
    inputLV[4] = selectedJet2->p4();
    solver_->solve(inputLV);
    quality = solver_->quality();
    std::copy(solver_->aux().begin(), solver_->aux().end(), std::back_inserter(*out_aux));

    cands->resize(7);

    Cand& ttbar = cands->at(0);
    Cand& top1 = cands->at(1);
    Cand& top2 = cands->at(2);
    Cand& w1 = cands->at(3);
    Cand& w2 = cands->at(4);
    Cand& nu1 = cands->at(5);
    Cand& nu2 = cands->at(6);

    // Set four momentum
    nu1.setP4(nu1LV);
    nu2.setP4(nu2LV);
    w1.setP4(solver_->l1()+nu1LV);
    w2.setP4(solver_->l2()+nu2LV);
    top1.setP4(w1.p4()+solver_->j1());
    top2.setP4(w2.p4()+solver_->j2());
    ttbar.setP4(top1.p4()+top2.p4());

    // Set basic quantum numbers (do channel dependent things later)
    const int lep1Q = lep1->charge();
    const int lep2Q = lep2->charge();
    ttbar.setPdgId(0);
    w1.setPdgId(-24*lep1Q);
    w2.setPdgId(-24*lep2Q);
    top1.setPdgId(-6*lep1Q);
    top2.setPdgId(-6*lep2Q);

    // Do the basic mother-daughter associations
    /*
    auto prodId = candsRefProd.id();
    auto getter = candsRefProd.productGetter();
    ttbar.addDaughter(reco::CandidatePtr(prodId, 1, getter));
    ttbar.addDaughter(reco::CandidatePtr(prodId, 2, getter));
    top1.addDaughter(reco::CandidatePtr(prodId, 3, getter));
    top2.addDaughter(reco::CandidatePtr(prodId, 4, getter));

    nu1.setPdgId((pdgId1+1)*lep1->charge());
    nu2.setPdgId((pdgId2+1)*lep2->charge());

    w1.addDaughter(reco::CandidatePtr(prodId, 5, getter));
    w2.addDaughter(reco::CandidatePtr(prodId, 6, getter));
    */

    out_mLL->push_back((solver_->l1()+solver_->l2()).mass());
    out_dphi->push_back(deltaPhi(top1.phi(), top2.phi()));
    out_mLB->push_back((solver_->l1()+solver_->j1()).mass());
    out_mLB->push_back((solver_->l2()+solver_->j2()).mass());
    if ( jetHandle->size() >= 4 )
    {
      int nUsedJet = 0;
      LV addJet2P4;
      for ( auto jet : *jetHandle )
      {
        if ( jet == selectedJet1 or jet == selectedJet2 ) continue;
        addJet2P4 += jet->p4();
        if ( ++nUsedJet > 2 ) break;
      }
      out_mAddJJ->push_back(addJet2P4.mass());
    }
  } while (false);

  event.put(cands);

  event.put(out_aux, "aux");
  event.put(out_mLL, "mLL");
  event.put(out_mLB, "mLB");
  event.put(out_mAddJJ, "mAddJJ");
  event.put(out_dphi, "dphi");
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TTbarDileptonKinSolutionProducer);


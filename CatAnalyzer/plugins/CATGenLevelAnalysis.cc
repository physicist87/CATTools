#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "CommonTools/Utils/interface/TFileDirectory.h"

#include "Math/GenVector/Boost.h"
#include "TH1.h"
#include "TH1F.h"
#include "TH2F.h"

#include <iostream>

using namespace std;

class CATGenLevelAnalysis : public edm::EDAnalyzer
{
public:
  CATGenLevelAnalysis(const edm::ParameterSet& pset);
  void analyze(const edm::Event& event, const edm::EventSetup& eventSetup) override;

private:
  edm::EDGetTokenT<int> channelToken_;
  edm::EDGetTokenT<std::vector<int> > modesToken_;
  edm::EDGetTokenT<reco::GenParticleCollection> partonTopToken_;
  edm::EDGetTokenT<reco::GenParticleCollection> pseudoTopToken_;

  typedef const reco::Candidate* CCandPtr;
  bool isAcceptedFullLept(CCandPtr l1, CCandPtr l2, CCandPtr b1, CCandPtr b2) {
    if ( l1->pt() < 20 or std::abs(l1->eta()) > 2.4 ) return false;
    if ( l2->pt() < 20 or std::abs(l2->eta()) > 2.4 ) return false;
    if ( b1->pt() < 30 or std::abs(b1->eta()) > 2.4 ) return false;
    if ( b2->pt() < 30 or std::abs(b2->eta()) > 2.4 ) return false;
    return true;
  }
  bool isAcceptedSemiLept(CCandPtr lep, CCandPtr q1, CCandPtr q2, CCandPtr b1, CCandPtr b2) {
    if ( lep->pt() < 30 or std::abs(lep->eta()) > 2.4 ) return false;
    if ( q1->pt() < 30 or std::abs(q1->eta()) > 2.4 ) return false;
    if ( q2->pt() < 30 or std::abs(q2->eta()) > 2.4 ) return false;
    if ( b1->pt() < 30 or std::abs(b1->eta()) > 2.4 ) return false;
    if ( b2->pt() < 30 or std::abs(b2->eta()) > 2.4 ) return false;
    return true;
  }

  typedef TH1F* H1;
  typedef TH2F* H2;

  enum {
    SL_topPt        , SL_topPtTtbarSys, SL_topY         ,
    SL_ttbarDelPhi  , SL_topPtLead    , SL_topPtSubLead ,
    SL_ttbarPt      , SL_ttbarY       , SL_ttbarMass    ,

    DL_topPt        , DL_topPtTtbarSys, DL_topY         ,
    DL_ttbarDelPhi  , DL_topPtLead    , DL_topPtSubLead ,
    DL_ttbarPt      , DL_ttbarY       , DL_ttbarMass    ,

    END
  };

  // 1D histograms
  std::vector<TH1F*> hFulParton_; // Full phase space parton level
  std::vector<TH1F*> hFidParton_; // Fiducial phase space parton level
  std::vector<TH1F*> hPseudo_   ; // Particle level (fiducial cut by construction)
  std::vector<TH1F*> hFidPseudo_; // Parton level channel filtered phase space particle level (parton level fiducial cut)

  // Response matrices
  std::vector<TH2F*> h2_, h2Fid_;
};

//using namespace cat;

CATGenLevelAnalysis::CATGenLevelAnalysis(const edm::ParameterSet& pset)
{
  partonTopToken_ = consumes<reco::GenParticleCollection>(pset.getParameter<edm::InputTag>("partonTop"));
  pseudoTopToken_ = consumes<reco::GenParticleCollection>(pset.getParameter<edm::InputTag>("pseudoTop"));
  channelToken_ = consumes<int>(pset.getParameter<edm::InputTag>("channel"));
  modesToken_ = consumes<std::vector<int> >(pset.getParameter<edm::InputTag>("modes"));

  edm::Service<TFileService> fs;

  const std::vector<std::vector<double> > bins = {
    {0, 60, 100, 150, 200, 260, 320, 400, 500}, // d15
    {0, 60, 100, 150, 200, 260, 320, 400, 500}, // d16
    {-2.5,-1.6,-1.2,-0.8,-0.4, 0.0, 0.4, 0.8, 1.2, 1.6, 2.5}, // d17
    {0,2,2.75,3,3.15}, // d18
    {0,60,100,150,200,260,320,400,500}, //d19
    {0,60,100,150,200,260,320,400,500}, //d20
    {0.0,20,45,75,120,190,255}, //d21
    {-2.5,-1.3,-0.9,-0.6,-0.3,0,0.3,0.6,0.9,1.3,2.5}, //d22
    {345,400,470,550,650,800,1100,1600}, //d23
    {0,65,125,200,290,400}, //d24
    {0,60,115,190,275,380,500}, //d25
    {-2.5,-1.6,-1,-0.5,0,0.5,1,1.6,2.5}, //d26
    {0,1.89,2.77,3.05,3.15}, //d27
    {0,75,130,200,290,400}, //d28
    {0,55,120,200,290,400}, //d29
    {0,30,80,170,300},
    {-2.5,-1.5,-1,-0.5,0,0.5,1,1.5,2.5},
    {340,380,470,620,820,1100,1600}
  };

  const std::vector<std::string> names = {
    "SL_topPt", "SL_topPtTtbarSys", "SL_topY", "SL_ttbarDelPhi",
    "SL_topPtLead", "SL_topPtSubLead",
    "SL_ttbarPt", "SL_ttbarY", "SL_ttbarMass",

    "DL_topPt", "DL_topPtTtbarSys", "DL_topY", "DL_ttbarDelPhi",
    "DL_topPtLead", "DL_topPtSubLead",
    "DL_ttbarPt", "DL_ttbarY", "DL_ttbarMass",
  };

  const std::vector<std::string> titles = {
    "top p_{T} (GeV)", "top p_{T} at CM frame (GeV)", "top rapidity", "#delta#phi(top1, top2)",
    "Leading top p_{T} (GeV)", "Subleading top p_{T} (GeV)",
    "t#bar{T} p_{T} (GeV)", "t#bar{t} rapidity (GeV)", "t#bar{t} mass (GeV)",

    "top p_{T} (GeV)", "top p_{T} at CM frame (GeV)", "top rapidity", "#delta#phi(top1, top2)",
    "Leading top p_{T} (GeV)", "Subleading top p_{T} (GeV)",
    "t#bar{T} p_{T} (GeV)", "t#bar{t} rapidity (GeV)", "t#bar{t} mass (GeV)",
  };

  auto dirFulParton = fs->mkdir("FulParton");
  auto dirFidParton = fs->mkdir("FiducialParton");
  auto dirPseudo = fs->mkdir("Particle");
  auto dirFidPseudo = fs->mkdir("FiducialParticle");

  for ( size_t i=0; i<18; ++i ) {
    const auto name = names[i].c_str();
    const auto title = (names[i] + ";" + titles[i]).c_str();
    const int nbins = bins[i].size()-1;
    const double* binPtr = &bins[i][0];
    hFulParton_.push_back(dirFulParton.make<TH1F>(name, title, nbins, binPtr));
    hFidParton_.push_back(dirFidParton.make<TH1F>(name, title, nbins, binPtr));
    hPseudo_.push_back(dirPseudo.make<TH1F>(name, title, nbins, binPtr));
    hFidPseudo_.push_back(dirFidPseudo.make<TH1F>(name, title, nbins, binPtr));
    const auto name2 = ("resp_"+names[i]).c_str();
    const auto title2 = (names[i] + ";Particle level " + title + ";Parton level " + title).c_str();
    h2_.push_back(dirPseudo.make<TH2F>(name2, title2, nbins, binPtr, nbins, binPtr));
    h2Fid_.push_back(dirFidPseudo.make<TH2F>(name2, title2, nbins, binPtr, nbins, binPtr));
  }

}

void CATGenLevelAnalysis::analyze(const edm::Event& event, const edm::EventSetup& eventSetup)
{
  edm::Handle<int> channelHandle;
  event.getByToken(channelToken_, channelHandle);
  const int channel = *channelHandle;
  if ( channel == 0 ) return;

  edm::Handle<std::vector<int> > modesHandle;
  event.getByToken(modesToken_, modesHandle);

  edm::Handle<reco::GenParticleCollection> partonTopHandle;
  event.getByToken(partonTopToken_, partonTopHandle);
  if ( partonTopHandle->empty() ) return;

  // Find all parton level top decay chain
  // Get Top quark pairs first
  const auto partonTop1 = &partonTopHandle->at(0);
  const auto partonTop2 = &partonTopHandle->at(1);
  if ( !partonTop1 or !partonTop2 ) return;
  // Get W and b quarks
  // Prdering is fixed from the PartonTopProducer, W first
  const auto partonW1 = partonTop1->daughter(0);
  const auto partonB1 = partonTop1->daughter(1);
  const auto partonW2 = partonTop2->daughter(0);
  const auto partonB2 = partonTop2->daughter(1);
  if ( !partonW1 or !partonB2 or !partonB1 or !partonB2 ) return;
  // Get W daughters
  // Ordering is fixed from the PartonTopProducer, lepton first.
  auto partonW11 = partonW1->daughter(0);
  //const auto partonW12 = partonW1->daughter(1);
  auto partonW21 = partonW2->daughter(0);
  const auto partonW22 = partonW2->daughter(1);
  // Continue to daughter for leptonically decaying taus
  if ( abs(partonW11->pdgId()) == 15 and
       partonW11->numberOfDaughters() > 0 and
       abs(partonW11->daughter(0)->pdgId()) > 10 ) partonW11 = partonW11->daughter(0);
  if ( abs(partonW21->pdgId()) == 15 and
       partonW21->numberOfDaughters() > 0 and
       abs(partonW21->daughter(0)->pdgId()) > 10 ) partonW21 = partonW21->daughter(0);
  const auto partonTT = partonTop1->p4()+partonTop2->p4();
  const double partonTopPtAtCM = ROOT::Math::Boost(partonTT.BoostToCM())(partonTop1->p4()).pt();

  // Fill parton top plots
  if ( channel == 2 ) {
    hFulParton_[SL_topPt]->Fill(partonTop1->pt());
    hFulParton_[SL_topPt]->Fill(partonTop2->pt());
    hFulParton_[SL_topY]->Fill(partonTop1->p4().Rapidity());
    hFulParton_[SL_topY]->Fill(partonTop2->p4().Rapidity());
    hFulParton_[SL_ttbarDelPhi]->Fill(reco::deltaPhi(partonTop1->phi(), partonTop2->phi()));
    hFulParton_[SL_topPtLead]->Fill(std::max(partonTop1->pt(), partonTop2->pt()));
    hFulParton_[SL_topPtSubLead]->Fill(std::min(partonTop1->pt(), partonTop2->pt()));
    hFulParton_[SL_ttbarPt]->Fill(partonTT.pt());
    hFulParton_[SL_ttbarY]->Fill(partonTT.Rapidity());
    hFulParton_[SL_ttbarMass]->Fill(partonTT.mass());
    hFulParton_[SL_topPtTtbarSys]->Fill(partonTopPtAtCM);
  }
  else if ( channel == 3 ) {
    hFulParton_[DL_topPt]->Fill(partonTop1->pt());
    hFulParton_[DL_topPt]->Fill(partonTop2->pt());
    hFulParton_[DL_topY]->Fill(partonTop1->p4().Rapidity());
    hFulParton_[DL_topY]->Fill(partonTop2->p4().Rapidity());
    hFulParton_[DL_ttbarDelPhi]->Fill(reco::deltaPhi(partonTop1->phi(), partonTop2->phi()));
    hFulParton_[DL_topPtLead]->Fill(std::max(partonTop1->pt(), partonTop2->pt()));
    hFulParton_[DL_topPtSubLead]->Fill(std::min(partonTop1->pt(), partonTop2->pt()));
    hFulParton_[DL_ttbarPt]->Fill(partonTT.pt());
    hFulParton_[DL_ttbarY]->Fill(partonTT.Rapidity());
    hFulParton_[DL_ttbarMass]->Fill(partonTT.mass());
    hFulParton_[DL_topPtTtbarSys]->Fill(partonTopPtAtCM);
  }

  // Fill parton top plots in fiducial phase space
  if ( channel == 2 and isAcceptedSemiLept(partonW11, partonW21, partonW22, partonB1, partonB2) ) {
    hFidParton_[SL_topPt]->Fill(partonTop1->pt());
    hFidParton_[SL_topPt]->Fill(partonTop2->pt());
    hFidParton_[SL_topY]->Fill(partonTop1->p4().Rapidity());
    hFidParton_[SL_topY]->Fill(partonTop2->p4().Rapidity());
    hFidParton_[SL_ttbarDelPhi]->Fill(reco::deltaPhi(partonTop1->phi(), partonTop2->phi()));
    hFidParton_[SL_topPtLead]->Fill(std::max(partonTop1->pt(), partonTop2->pt()));
    hFidParton_[SL_topPtSubLead]->Fill(std::min(partonTop1->pt(), partonTop2->pt()));
    hFidParton_[SL_ttbarPt]->Fill(partonTT.pt());
    hFidParton_[SL_ttbarY]->Fill(partonTT.Rapidity());
    hFidParton_[SL_ttbarMass]->Fill(partonTT.mass());
    hFidParton_[SL_topPtTtbarSys]->Fill(partonTopPtAtCM);
  }
  else if ( channel == 3 and isAcceptedFullLept(partonW11, partonW21, partonB1, partonB2) ) {
    hFidParton_[DL_topPt]->Fill(partonTop1->pt());
    hFidParton_[DL_topPt]->Fill(partonTop2->pt());
    hFidParton_[DL_topY]->Fill(partonTop1->p4().Rapidity());
    hFidParton_[DL_topY]->Fill(partonTop2->p4().Rapidity());
    hFidParton_[DL_ttbarDelPhi]->Fill(reco::deltaPhi(partonTop1->phi(), partonTop2->phi()));
    hFidParton_[DL_topPtLead]->Fill(std::max(partonTop1->pt(), partonTop2->pt()));
    hFidParton_[DL_topPtSubLead]->Fill(std::min(partonTop1->pt(), partonTop2->pt()));
    hFidParton_[DL_ttbarPt]->Fill(partonTT.pt());
    hFidParton_[DL_ttbarY]->Fill(partonTT.Rapidity());
    hFidParton_[DL_ttbarMass]->Fill(partonTT.mass());
    hFidParton_[DL_topPtTtbarSys]->Fill(partonTopPtAtCM);
  }

  edm::Handle<reco::GenParticleCollection> pseudoTopHandle;
  event.getByToken(pseudoTopToken_, pseudoTopHandle);
  if ( pseudoTopHandle->empty() )
  {
    // Fill parton top only (but no pseudoTop) plots
    return;
  }

  // Find all particle level top decay chain
  // Get Top quark pairs first
  const auto pseudoTop1 = &pseudoTopHandle->at(0);
  const auto pseudoTop2 = &pseudoTopHandle->at(1);

  // Get W and b quarks
  // Ordering is fixed, W first
  if ( !pseudoTop1 or !pseudoTop2 ) return;
  const auto pseudoW1 = pseudoTop1->daughter(0);
  const auto pseudoB1 = pseudoTop1->daughter(1);
  const auto pseudoW2 = pseudoTop2->daughter(0);
  const auto pseudoB2 = pseudoTop2->daughter(1);
  if ( !pseudoW1 or !pseudoW2 or !pseudoB1 or !pseudoB2 ) return;
  // Get W daughters
  // Ordering is fixed from the PartonTopProducer, lepton first.
  // There's no tau in PseudoTopProducer
  const auto pseudoW11 = pseudoW1->daughter(0);
  //const auto pseudoW12 = pseudoW1->daughter(1);
  const auto pseudoW21 = pseudoW2->daughter(0);
  const auto pseudoW22 = pseudoW2->daughter(1);

  const bool isLeptonic1 = abs(pseudoW11->pdgId()) > 10;
  const bool isLeptonic2 = abs(pseudoW21->pdgId()) > 10;
  if ( !isLeptonic1 and !isLeptonic2 ) return; // Skip full hadronic channel

  const auto pseudoTT = pseudoTop1->p4()+pseudoTop2->p4();
  const double pseudoTopPtAtCM = ROOT::Math::Boost(pseudoTT.BoostToCM())(pseudoTop1->p4()).pt();

  // Fill pseudo top plots
  if ( (!isLeptonic1 or !isLeptonic2) and
       isAcceptedSemiLept(pseudoW11, pseudoW21, pseudoW22, pseudoB1, pseudoB2) ) {
    // Additional acceptance cut for L+J channel
    hPseudo_[SL_topPt]->Fill(pseudoTop1->pt());
    hPseudo_[SL_topPt]->Fill(pseudoTop2->pt());
    hPseudo_[SL_topY]->Fill(pseudoTop1->p4().Rapidity());
    hPseudo_[SL_topY]->Fill(pseudoTop2->p4().Rapidity());
    hPseudo_[SL_ttbarDelPhi]->Fill(reco::deltaPhi(pseudoTop1->phi(), pseudoTop2->phi()));
    hPseudo_[SL_topPtLead]->Fill(std::max(pseudoTop1->pt(), pseudoTop2->pt()));
    hPseudo_[SL_topPtSubLead]->Fill(std::min(pseudoTop1->pt(), pseudoTop2->pt()));
    hPseudo_[SL_ttbarPt]->Fill(pseudoTT.pt());
    hPseudo_[SL_ttbarY]->Fill(pseudoTT.Rapidity());
    hPseudo_[SL_ttbarMass]->Fill(pseudoTT.mass());
    hPseudo_[SL_topPtTtbarSys]->Fill(pseudoTopPtAtCM);

    // Fill response matrix no matter what parton level object acceptance is
    h2_[SL_topPt]->Fill(pseudoTop1->pt(), partonTop1->pt());
    h2_[SL_topPt]->Fill(pseudoTop2->pt(), partonTop2->pt());
    h2_[SL_topY]->Fill(pseudoTop1->p4().Rapidity(), partonTop1->p4().Rapidity());
    h2_[SL_topY]->Fill(pseudoTop2->p4().Rapidity(), partonTop1->p4().Rapidity());
    h2_[SL_ttbarDelPhi]->Fill(reco::deltaPhi(pseudoTop1->phi(), pseudoTop2->phi()), reco::deltaPhi(partonTop1->phi(), partonTop2->phi()));
    h2_[SL_topPtLead]->Fill(std::max(pseudoTop1->pt(), pseudoTop2->pt()), std::max(partonTop1->pt(), partonTop2->pt()));
    h2_[SL_topPtSubLead]->Fill(std::min(pseudoTop1->pt(), pseudoTop2->pt()), std::min(partonTop1->pt(), partonTop2->pt()));
    h2_[SL_ttbarPt]->Fill(pseudoTT.pt(), partonTT.pt());
    h2_[SL_ttbarY]->Fill(pseudoTT.Rapidity(), partonTT.Rapidity());
    h2_[SL_ttbarMass]->Fill(pseudoTT.mass(), partonTT.mass());
    h2_[SL_topPtTtbarSys]->Fill(pseudoTopPtAtCM, partonTopPtAtCM);

    // Fill pseudo top plots within parton level acceptance cut
    if ( channel == 2 and isAcceptedSemiLept(partonW11, partonW21, partonW22, partonB1, partonB2) ) {
      hFidPseudo_[SL_topPt]->Fill(pseudoTop1->pt());
      hFidPseudo_[SL_topPt]->Fill(pseudoTop2->pt());
      hFidPseudo_[SL_topY]->Fill(pseudoTop1->p4().Rapidity());
      hFidPseudo_[SL_topY]->Fill(pseudoTop2->p4().Rapidity());
      hFidPseudo_[SL_ttbarDelPhi]->Fill(reco::deltaPhi(pseudoTop1->phi(), pseudoTop2->phi()));
      hFidPseudo_[SL_topPtLead]->Fill(std::max(pseudoTop1->pt(), pseudoTop2->pt()));
      hFidPseudo_[SL_topPtSubLead]->Fill(std::min(pseudoTop1->pt(), pseudoTop2->pt()));
      hFidPseudo_[SL_ttbarPt]->Fill(pseudoTT.pt());
      hFidPseudo_[SL_ttbarY]->Fill(pseudoTT.Rapidity());
      hFidPseudo_[SL_ttbarMass]->Fill(pseudoTT.mass());
      hFidPseudo_[SL_topPtTtbarSys]->Fill(pseudoTopPtAtCM);

      // Fill response matrix no matter what parton level object acceptance is
      h2Fid_[SL_topPt]->Fill(pseudoTop1->pt(), partonTop1->pt());
      h2Fid_[SL_topPt]->Fill(pseudoTop2->pt(), partonTop2->pt());
      h2Fid_[SL_topY]->Fill(pseudoTop1->p4().Rapidity(), partonTop1->p4().Rapidity());
      h2Fid_[SL_topY]->Fill(pseudoTop2->p4().Rapidity(), partonTop1->p4().Rapidity());
      h2Fid_[SL_ttbarDelPhi]->Fill(reco::deltaPhi(pseudoTop1->phi(), pseudoTop2->phi()), reco::deltaPhi(partonTop1->phi(), partonTop2->phi()));
      h2Fid_[SL_topPtLead]->Fill(std::max(pseudoTop1->pt(), pseudoTop2->pt()), std::max(partonTop1->pt(), partonTop2->pt()));
      h2Fid_[SL_topPtSubLead]->Fill(std::min(pseudoTop1->pt(), pseudoTop2->pt()), std::min(partonTop1->pt(), partonTop2->pt()));
      h2Fid_[SL_ttbarPt]->Fill(pseudoTT.pt(), partonTT.pt());
      h2Fid_[SL_ttbarY]->Fill(pseudoTT.Rapidity(), partonTT.Rapidity());
      h2Fid_[SL_ttbarMass]->Fill(pseudoTT.mass(), partonTT.mass());
      h2Fid_[SL_topPtTtbarSys]->Fill(pseudoTopPtAtCM, partonTopPtAtCM);
    }
  }
  else if ( isAcceptedFullLept(pseudoW11, pseudoW21, pseudoB1, pseudoB2) ) {
    hPseudo_[DL_topPt]->Fill(pseudoTop1->pt());
    hPseudo_[DL_topPt]->Fill(pseudoTop2->pt());
    hPseudo_[DL_topY]->Fill(pseudoTop1->p4().Rapidity());
    hPseudo_[DL_topY]->Fill(pseudoTop2->p4().Rapidity());
    hPseudo_[DL_ttbarDelPhi]->Fill(reco::deltaPhi(pseudoTop1->phi(), pseudoTop2->phi()));
    hPseudo_[DL_topPtLead]->Fill(std::max(pseudoTop1->pt(), pseudoTop2->pt()));
    hPseudo_[DL_topPtSubLead]->Fill(std::min(pseudoTop1->pt(), pseudoTop2->pt()));
    hPseudo_[DL_ttbarPt]->Fill(pseudoTT.pt());
    hPseudo_[DL_ttbarY]->Fill(pseudoTT.Rapidity());
    hPseudo_[DL_ttbarMass]->Fill(pseudoTT.mass());
    hPseudo_[DL_topPtTtbarSys]->Fill(pseudoTopPtAtCM);

    // Fill response matrix no matter what parton level object acceptance is
    h2_[DL_topPt]->Fill(pseudoTop1->pt(), partonTop1->pt());
    h2_[DL_topPt]->Fill(pseudoTop2->pt(), partonTop2->pt());
    h2_[DL_topY]->Fill(pseudoTop1->p4().Rapidity(), partonTop1->p4().Rapidity());
    h2_[DL_topY]->Fill(pseudoTop2->p4().Rapidity(), partonTop1->p4().Rapidity());
    h2_[DL_ttbarDelPhi]->Fill(reco::deltaPhi(pseudoTop1->phi(), pseudoTop2->phi()), reco::deltaPhi(partonTop1->phi(), partonTop2->phi()));
    h2_[DL_topPtLead]->Fill(std::max(pseudoTop1->pt(), pseudoTop2->pt()), std::max(partonTop1->pt(), partonTop2->pt()));
    h2_[DL_topPtSubLead]->Fill(std::min(pseudoTop1->pt(), pseudoTop2->pt()), std::min(partonTop1->pt(), partonTop2->pt()));
    h2_[DL_ttbarPt]->Fill(pseudoTT.pt(), partonTT.pt());
    h2_[DL_ttbarY]->Fill(pseudoTT.Rapidity(), partonTT.Rapidity());
    h2_[DL_ttbarMass]->Fill(pseudoTT.mass(), partonTT.mass());
    h2_[DL_topPtTtbarSys]->Fill(pseudoTopPtAtCM, partonTopPtAtCM);

    if ( channel == 3 and isAcceptedFullLept(partonW11, partonW21, partonB1, partonB2) ) {
      hFidPseudo_[DL_topPt]->Fill(pseudoTop1->pt());
      hFidPseudo_[DL_topPt]->Fill(pseudoTop2->pt());
      hFidPseudo_[DL_topY]->Fill(pseudoTop1->p4().Rapidity());
      hFidPseudo_[DL_topY]->Fill(pseudoTop2->p4().Rapidity());
      hFidPseudo_[DL_ttbarDelPhi]->Fill(reco::deltaPhi(pseudoTop1->phi(), pseudoTop2->phi()));
      hFidPseudo_[DL_topPtLead]->Fill(std::max(pseudoTop1->pt(), pseudoTop2->pt()));
      hFidPseudo_[DL_topPtSubLead]->Fill(std::min(pseudoTop1->pt(), pseudoTop2->pt()));
      hFidPseudo_[DL_ttbarPt]->Fill(pseudoTT.pt());
      hFidPseudo_[DL_ttbarY]->Fill(pseudoTT.Rapidity());
      hFidPseudo_[DL_ttbarMass]->Fill(pseudoTT.mass());
      hFidPseudo_[DL_topPtTtbarSys]->Fill(pseudoTopPtAtCM);

      // Fill response matrix no matter what parton level object acceptance is
      h2Fid_[DL_topPt]->Fill(pseudoTop1->pt(), partonTop1->pt());
      h2Fid_[DL_topPt]->Fill(pseudoTop2->pt(), partonTop2->pt());
      h2Fid_[DL_topY]->Fill(pseudoTop1->p4().Rapidity(), partonTop1->p4().Rapidity());
      h2Fid_[DL_topY]->Fill(pseudoTop2->p4().Rapidity(), partonTop1->p4().Rapidity());
      h2Fid_[DL_ttbarDelPhi]->Fill(reco::deltaPhi(pseudoTop1->phi(), pseudoTop2->phi()), reco::deltaPhi(partonTop1->phi(), partonTop2->phi()));
      h2Fid_[DL_topPtLead]->Fill(std::max(pseudoTop1->pt(), pseudoTop2->pt()), std::max(partonTop1->pt(), partonTop2->pt()));
      h2Fid_[DL_topPtSubLead]->Fill(std::min(pseudoTop1->pt(), pseudoTop2->pt()), std::min(partonTop1->pt(), partonTop2->pt()));
      h2Fid_[DL_ttbarPt]->Fill(pseudoTT.pt(), partonTT.pt());
      h2Fid_[DL_ttbarY]->Fill(pseudoTT.Rapidity(), partonTT.Rapidity());
      h2Fid_[DL_ttbarMass]->Fill(pseudoTT.mass(), partonTT.mass());
      h2Fid_[DL_topPtTtbarSys]->Fill(pseudoTopPtAtCM, partonTopPtAtCM);
    }
  }

}

DEFINE_FWK_MODULE(CATGenLevelAnalysis);


import FWCore.ParameterSet.Config as cms

pileupWeightMap = {
#from SimGeneral/MixingModule/python/mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi.py
"2016_25ns_SpringMC":cms.vdouble(
0.000829312873542,0.00124276120498 ,0.00339329181587 ,0.00408224735376,0.00383036590008,
0.00659159288946 ,0.00816022734493 ,0.00943640833116 ,0.0137777376066 ,0.017059392038  ,
0.0213193035468  ,0.0247343174676  ,0.0280848773878  ,0.0323308476564 ,0.0370394341409 ,
0.0456917721191  ,0.0558762890594  ,0.0576956187107  ,0.0625325287017 ,0.0591603758776 ,
0.0656650815128  ,0.0678329011676  ,0.0625142146389  ,0.0548068448797 ,0.0503893295063 ,
0.040209818868   ,0.0374446988111  ,0.0299661572042  ,0.0272024759921 ,0.0219328403791 ,
0.0179586571619  ,0.0142926728247  ,0.00839941654725 ,0.00522366397213,0.00224457976761,
0.000779274977993,0.000197066585944,7.16031761328e-05,0.0,0.0,
0.0,0.0,0.0,0.0,0.0,
0.0,0.0,0.0,0.0,0.0
),
#pileupCalc.py -i Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 71300 --maxPileupBin 50 --numPileupBins 50 PileUpData.root 
"Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON":cms.vdouble(
1.782745e+03,2.690151e+04,1.782663e+05,4.714121e+05,7.607781e+05,
1.024960e+06,1.477429e+06,7.351446e+06,2.295777e+07,3.753777e+07,
6.011602e+07,9.317925e+07,1.406152e+08,2.089582e+08,2.876763e+08,
3.531492e+08,3.932633e+08,4.086864e+08,3.995285e+08,3.689304e+08,
3.231239e+08,2.686611e+08,2.116473e+08,1.570575e+08,1.087794e+08,
6.962796e+07,4.086064e+07,2.188573e+07,1.069935e+07,4.796977e+06,
1.991051e+06,7.759526e+05,2.898794e+05,1.074600e+05,4.219007e+04,
1.950952e+04,1.162912e+04,8.731487e+03,7.497940e+03,6.849602e+03,
6.443459e+03,6.164290e+03,5.962505e+03,5.806678e+03,5.667294e+03,
5.528681e+03,5.378081e+03,5.206208e+03,5.008454e+03,4.783922e+03,
),
#pileupCalc.py -i Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 74865 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root 
"Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON_Up":cms.vdouble(
1.107849e+03,2.261339e+04,1.527120e+05,3.756942e+05,6.859520e+05,
9.168775e+05,1.129660e+06,3.687673e+06,1.557209e+07,2.930107e+07,
4.505088e+07,7.028203e+07,1.047705e+08,1.548708e+08,2.221351e+08,
2.924343e+08,3.466806e+08,3.786899e+08,3.894950e+08,3.791143e+08,
3.505225e+08,3.089284e+08,2.597274e+08,2.079864e+08,1.578937e+08,
1.127605e+08,7.510117e+07,4.630099e+07,2.629516e+07,1.373814e+07,
6.620171e+06,2.961507e+06,1.242537e+06,4.960967e+05,1.926378e+05,
7.554768e+04,3.205173e+04,1.621956e+04,1.040205e+04,8.119239e+03,
7.082606e+03,6.511396e+03,6.143724e+03,5.886598e+03,5.698458e+03,
5.553034e+03,5.425446e+03,5.300648e+03,5.168296e+03,5.019533e+03,
),
#pileupCalc.py -i Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 67735 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root 
"Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON_Dn":cms.vdouble(
2.620963e+03,3.378270e+04,2.115512e+05,5.769433e+05,8.612473e+05,
1.133396e+06,2.486344e+06,1.374395e+07,3.093915e+07,4.990281e+07,
8.123655e+07,1.259242e+08,1.931671e+08,2.791304e+08,3.575930e+08,
4.080549e+08,4.294270e+08,4.221082e+08,3.893581e+08,3.386685e+08,
2.780744e+08,2.149965e+08,1.553911e+08,1.038413e+08,6.344461e+07,
3.514593e+07,1.758808e+07,7.967131e+06,3.292463e+06,1.258110e+06,
4.534820e+05,1.591855e+05,5.779299e+04,2.422217e+04,1.322781e+04,
9.459536e+03,7.967598e+03,7.225058e+03,6.774019e+03,6.469837e+03,
6.252807e+03,6.084769e+03,5.931423e+03,5.775533e+03,5.601990e+03,
5.401304e+03,5.169621e+03,4.907362e+03,4.617921e+03,4.306564e+03,
),
#pileupCalc.py -i Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 71300 --maxPileupBin 50 --numPileupBins 50 PileUpData.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T":cms.vdouble(
1.811381e+03,6.485605e+04,3.417245e+05,6.874719e+05,1.082006e+06,
1.523413e+06,2.138897e+06,8.857555e+06,3.003975e+07,6.281511e+07,
1.140486e+08,1.677066e+08,2.217580e+08,2.923082e+08,3.771719e+08,
4.576940e+08,5.164267e+08,5.435015e+08,5.394139e+08,5.110522e+08,
4.631278e+08,3.999488e+08,3.272788e+08,2.513622e+08,1.795783e+08,
1.191379e+08,7.378382e+07,4.295570e+07,2.366711e+07,1.243875e+07,
6.293865e+06,3.089516e+06,1.476147e+06,6.858958e+05,3.094330e+05,
1.360321e+05,5.939191e+04,2.707284e+04,1.407670e+04,9.048308e+03,
7.126813e+03,6.361481e+03,6.015268e+03,5.819755e+03,5.670293e+03,
5.529317e+03,5.378206e+03,5.206230e+03,5.008458e+03,4.783923e+03,
),
#pileupCalc.py -i Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 74865 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T_Up":cms.vdouble(
1.133932e+03,4.934046e+04,3.012609e+05,5.652183e+05,9.740640e+05,
1.338666e+06,1.711585e+06,4.610255e+06,1.912919e+07,4.363280e+07,
8.250602e+07,1.324371e+08,1.795169e+08,2.328994e+08,3.025979e+08,
3.805292e+08,4.501609e+08,4.984780e+08,5.187115e+08,5.125787e+08,
4.859050e+08,4.424071e+08,3.856057e+08,3.202340e+08,2.513639e+08,
1.849316e+08,1.271613e+08,8.201375e+07,4.991480e+07,2.883355e+07,
1.590832e+07,8.448003e+06,4.351374e+06,2.184805e+06,1.070474e+06,
5.110310e+05,2.375402e+05,1.081302e+05,4.924224e+04,2.358105e+04,
1.286644e+04,8.540255e+03,6.809974e+03,6.091136e+03,5.757096e+03,
5.568717e+03,5.429356e+03,5.301556e+03,5.168493e+03,5.019572e+03,
),
#pileupCalc.py -i Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 67735 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T_Dn":cms.vdouble(
2.653297e+03,8.448778e+04,3.886269e+05,8.288347e+05,1.230064e+06,
1.713876e+06,3.300952e+06,1.666090e+07,4.500962e+07,9.132205e+07,
1.519768e+08,2.097347e+08,2.800227e+08,3.706619e+08,4.631331e+08,
5.343865e+08,5.702064e+08,5.690479e+08,5.389221e+08,4.858616e+08,
4.151975e+08,3.340203e+08,2.501234e+08,1.727172e+08,1.099819e+08,
6.503945e+07,3.600609e+07,1.881295e+07,9.370906e+06,4.496100e+06,
2.091381e+06,9.439111e+05,4.124838e+05,1.747790e+05,7.297079e+04,
3.152934e+04,1.553047e+04,9.622158e+03,7.475129e+03,6.658714e+03,
6.299603e+03,6.095419e+03,5.933647e+03,5.775958e+03,5.602064e+03,
5.401316e+03,5.169623e+03,4.907363e+03,4.617921e+03,4.306564e+03,
),
#pileupCalc.py -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 69200 --maxPileupBin 50 --numPileupBins 50 PileUpData.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON":cms.vdouble(
1.827642e+03,6.059128e+04,3.396887e+05,6.519469e+05,1.074047e+06,
1.501117e+06,1.982683e+06,6.470305e+06,2.366553e+07,4.922270e+07,
9.055294e+07,1.422713e+08,1.906575e+08,2.448287e+08,3.150670e+08,
3.938074e+08,4.633652e+08,5.107552e+08,5.316173e+08,5.285932e+08,
5.070718e+08,4.702726e+08,4.207972e+08,3.626679e+08,3.000539e+08,
2.368030e+08,1.772530e+08,1.256785e+08,8.467061e+07,5.445397e+07,
3.358021e+07,1.994934e+07,1.148344e+07,6.446069e+06,3.547477e+06,
1.919327e+06,1.020838e+06,5.328258e+05,2.725589e+05,1.369243e+05,
6.823034e+04,3.457581e+04,1.867349e+04,1.143212e+04,8.249688e+03,
6.895534e+03,6.335506e+03,6.108908e+03,6.015830e+03,5.969526e+03,
),
#pileupCalc.py -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 72383 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_Up":cms.vdouble(
1.201548e+03,4.676716e+04,3.008725e+05,5.420738e+05,9.804709e+05,
1.318758e+06,1.700310e+06,3.673068e+06,1.513481e+07,3.574484e+07,
6.596769e+07,1.110088e+08,1.571718e+08,2.017265e+08,2.565703e+08,
3.250449e+08,3.963534e+08,4.556627e+08,4.940383e+08,5.091794e+08,
5.040965e+08,4.832648e+08,4.491942e+08,4.040599e+08,3.512362e+08,
2.942352e+08,2.362509e+08,1.808398e+08,1.317071e+08,9.145469e+07,
6.078689e+07,3.882864e+07,2.392876e+07,1.429309e+07,8.320747e+06,
4.746313e+06,2.662791e+06,1.471227e+06,7.999008e+05,4.272497e+05,
2.240457e+05,1.156925e+05,5.946075e+04,3.116776e+04,1.739840e+04,
1.092001e+04,7.969211e+03,6.664344e+03,6.102269e+03,5.865247e+03,
),
#pileupCalc.py -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 66016 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root 
"Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_Dn":cms.vdouble(
2.621526e+03,7.787448e+04,3.814820e+05,7.840881e+05,1.194340e+06,
1.689306e+06,2.643789e+06,1.180856e+07,3.476272e+07,6.900734e+07,
1.223743e+08,1.775351e+08,2.323706e+08,3.028372e+08,3.881155e+08,
4.690477e+08,5.273554e+08,5.555278e+08,5.553688e+08,5.332745e+08,
4.934138e+08,4.389367e+08,3.746769e+08,3.056256e+08,2.364744e+08,
1.725352e+08,1.186676e+08,7.726892e+07,4.788712e+07,2.839110e+07,
1.619692e+07,8.954894e+06,4.831820e+06,2.556327e+06,1.327713e+06,
6.759631e+05,3.366890e+05,1.642298e+05,7.915958e+04,3.866586e+04,
2.013510e+04,1.199229e+04,8.551242e+03,7.147703e+03,6.592690e+03,
6.377959e+03,6.291914e+03,6.245973e+03,6.199073e+03,6.128442e+03,
),
}

pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_Plus_DCSOnly_275282-275376_JSON"] = pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON"]
pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_Plus_DCSOnly_275282-275376_JSON_Up"] = pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON_Up"]
pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_Plus_DCSOnly_275282-275376_JSON_Dn"] = pileupWeightMap["Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON_Dn"]

#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt --minBiasXsec 69200 --calcMode true --maxPileupBin 50 --numPileupBins 50 PileUpData.root 
pileupWeightMap["Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON"] = cms.vdouble(
2.174516e+03,2.278790e+05,8.101597e+05,1.507252e+06,2.392582e+06,
3.270745e+06,4.258598e+06,9.049921e+06,2.993084e+07,7.216534e+07,
1.508306e+08,2.673255e+08,4.082804e+08,5.609675e+08,7.138942e+08,
8.619335e+08,9.843070e+08,1.067037e+09,1.112454e+09,1.126326e+09,
1.113098e+09,1.075168e+09,1.016672e+09,9.427759e+08,8.559270e+08,
7.567600e+08,6.480709e+08,5.364947e+08,4.300848e+08,3.349132e+08,
2.538812e+08,1.875071e+08,1.350574e+08,9.508705e+07,6.564294e+07,
4.454067e+07,2.971334e+07,1.944297e+07,1.242074e+07,7.697645e+06,
4.596443e+06,2.627970e+06,1.431516e+06,7.406041e+05,3.637266e+05,
1.702833e+05,7.706896e+04,3.494570e+04,1.709334e+04,9.984803e+03,
)
#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt --minBiasXsec 72383 --calcMode true --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root 
pileupWeightMap["Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON_Up"] = cms.vdouble(
1.332754e+03,1.911576e+05,7.159829e+05,1.273585e+06,2.191584e+06,
2.873294e+06,3.776664e+06,5.976629e+06,1.888261e+07,4.888698e+07,
1.041302e+08,1.956129e+08,3.137658e+08,4.492471e+08,5.893358e+08,
7.287625e+08,8.596536e+08,9.628074e+08,1.030882e+09,1.067243e+09,
1.076749e+09,1.062843e+09,1.027461e+09,9.741449e+08,9.072802e+08,
8.290513e+08,7.399401e+08,6.418204e+08,5.397329e+08,4.404572e+08,
3.497452e+08,2.708392e+08,2.047547e+08,1.512130e+08,1.092429e+08,
7.740074e+07,5.392587e+07,3.699721e+07,2.498063e+07,1.655374e+07,
1.071623e+07,6.738141e+06,4.090747e+06,2.385119e+06,1.329968e+06,
7.073868e+05,3.587500e+05,1.740842e+05,8.175405e+04,3.822246e+04,
)
#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt --minBiasXsec 66016 --calcMode true --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root 
pileupWeightMap["Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON_Dn"] = cms.vdouble(
3.502731e+03,2.744482e+05,9.121306e+05,1.790556e+06,2.644803e+06,
3.710883e+06,5.099947e+06,1.509146e+07,4.635991e+07,1.079477e+08,
2.161984e+08,3.596716e+08,5.241620e+08,6.924560e+08,8.583820e+08,
1.002983e+09,1.103990e+09,1.160875e+09,1.180386e+09,1.168251e+09,
1.127514e+09,1.063040e+09,9.809543e+08,8.840087e+08,7.731105e+08,
6.523933e+08,5.305046e+08,4.168191e+08,3.175082e+08,2.349205e+08,
1.689708e+08,1.183516e+08,8.098941e+07,5.432922e+07,3.577769e+07,
2.309300e+07,1.454243e+07,8.873525e+06,5.205365e+06,2.914069e+06,
1.547637e+06,7.768143e+05,3.682685e+05,1.657289e+05,7.205097e+04,
3.167397e+04,1.545143e+04,9.359210e+03,7.195216e+03,6.429707e+03,
)

#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt --minBiasXsec 69200 --calcMode true --maxPileupBin 50 --numPileupBins 50 PileUpData.root
pileupWeightMap["Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON"] = cms.vdouble(
2.174516e+03,2.281855e+05,8.533645e+05,1.587530e+06,2.529077e+06,
3.387696e+06,4.381229e+06,9.149864e+06,3.006044e+07,7.236560e+07,
1.511572e+08,2.682617e+08,4.119672e+08,5.720751e+08,7.354401e+08,
8.911121e+08,1.017227e+09,1.103631e+09,1.154568e+09,1.174014e+09,
1.163890e+09,1.126234e+09,1.066573e+09,9.913133e+08,9.033366e+08,
8.033106e+08,6.941101e+08,5.825506e+08,4.766771e+08,3.821276e+08,
3.010687e+08,2.333676e+08,1.779921e+08,1.335789e+08,9.852626e+07,
7.117468e+07,5.006790e+07,3.406612e+07,2.227537e+07,1.392498e+07,
8.291331e+06,4.692094e+06,2.521527e+06,1.287388e+06,6.256920e+05,
2.907934e+05,1.305357e+05,5.788891e+04,2.662319e+04,1.381208e+04,
)
#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt --minBiasXsec 72383 --calcMode true --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root
pileupWeightMap["Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON_Up"] = cms.vdouble(
1.332754e+03,1.912830e+05,7.497989e+05,1.341387e+06,2.322004e+06,
2.985227e+06,3.899921e+06,6.071934e+06,1.899185e+07,4.904670e+07,
1.043694e+08,1.960944e+08,3.154195e+08,4.550334e+08,6.035213e+08,
7.521956e+08,8.887848e+08,9.949601e+08,1.066723e+09,1.108329e+09,
1.122773e+09,1.111488e+09,1.076279e+09,1.021896e+09,9.537765e+08,
8.744924e+08,7.845594e+08,6.858994e+08,5.837039e+08,4.848116e+08,
3.947141e+08,3.160843e+08,2.493280e+08,1.937815e+08,1.484086e+08,
1.119604e+08,8.304654e+07,6.032534e+07,4.267745e+07,2.923080e+07,
1.927919e+07,1.219245e+07,7.371585e+06,4.253599e+06,2.341098e+06,
1.229573e+06,6.173375e+05,2.974456e+05,1.386735e+05,6.369108e+04,
)
#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt --minBiasXsec 66016 --calcMode true --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root
pileupWeightMap["Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON_Dn"] = cms.vdouble(
3.502732e+03,2.751936e+05,9.647037e+05,1.887629e+06,2.782925e+06,
3.838709e+06,5.215774e+06,1.520353e+07,4.652205e+07,1.082016e+08,
2.167405e+08,3.618004e+08,5.320964e+08,7.112540e+08,8.870782e+08,
1.036673e+09,1.141415e+09,1.204039e+09,1.229825e+09,1.221378e+09,
1.181045e+09,1.115293e+09,1.031722e+09,9.335695e+08,8.217784e+08,
7.006050e+08,5.788963e+08,4.658955e+08,3.671075e+08,2.839836e+08,
2.158030e+08,1.611134e+08,1.181154e+08,8.480326e+07,5.929117e+07,
4.006572e+07,2.596860e+07,1.604062e+07,9.398724e+06,5.209266e+06,
2.728040e+06,1.350415e+06,6.332750e+05,2.828448e+05,1.218085e+05,
5.205780e+04,2.350772e+04,1.242591e+04,8.315999e+03,6.821517e+03,
)

#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt --minBiasXsec 69200 --calcMode true --maxPileupBin 50 --numPileupBins 50 PileUpData.root
pileupWeightMap["Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON"] = cms.vdouble(
1.534099e+04,4.547505e+05,1.445036e+06,2.383235e+06,3.475685e+06,
4.764327e+06,5.851250e+06,1.074243e+07,3.200313e+07,7.605884e+07,
1.647928e+08,3.183543e+08,5.225338e+08,7.491542e+08,9.831612e+08,
1.229340e+09,1.440446e+09,1.583017e+09,1.663537e+09,1.699110e+09,
1.705559e+09,1.692768e+09,1.660566e+09,1.606273e+09,1.529092e+09,
1.428639e+09,1.307896e+09,1.174192e+09,1.035179e+09,8.956330e+08,
7.580590e+08,6.249498e+08,5.000051e+08,3.874110e+08,2.904245e+08,
2.105521e+08,1.475592e+08,9.991560e+07,6.532965e+07,4.122368e+07,
2.509346e+07,1.473324e+07,8.345725e+06,4.563732e+06,2.411463e+06,
1.232937e+06,6.112354e+05,2.949004e+05,1.394867e+05,6.569939e+04,
)
#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt --minBiasXsec 72383 --calcMode true --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root
pileupWeightMap["Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON_Up"] = cms.vdouble(
1.213710e+04,3.906587e+05,1.277139e+06,2.076156e+06,3.174079e+06,
4.228452e+06,5.297430e+06,7.542597e+06,2.064224e+07,5.159869e+07,
1.108393e+08,2.225923e+08,3.872754e+08,5.869655e+08,7.955235e+08,
1.014870e+09,1.236469e+09,1.414739e+09,1.531985e+09,1.597624e+09,
1.626109e+09,1.630388e+09,1.618173e+09,1.588983e+09,1.540504e+09,
1.472079e+09,1.383244e+09,1.275888e+09,1.155687e+09,1.029366e+09,
9.016521e+08,7.750232e+08,6.513360e+08,5.332660e+08,4.242899e+08,
3.276569e+08,2.454607e+08,1.783166e+08,1.255679e+08,8.567186e+07,
5.660428e+07,3.619907e+07,2.239978e+07,1.341100e+07,7.770645e+06,
4.359834e+06,2.370638e+06,1.250716e+06,6.413813e+05,3.206494e+05,
)
#pileupCalc.py -i /CATTools/CatProducer/data/LumiMask/Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt --minBiasXsec 66016 --calcMode true --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root
pileupWeightMap["Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON_Dn"] = cms.vdouble(
2.060997e+04,5.352429e+05,1.626431e+06,2.746354e+06,3.864680e+06,
5.334032e+06,6.779786e+06,1.694061e+07,4.904381e+07,1.146948e+08,
2.465197e+08,4.474277e+08,6.904622e+08,9.429871e+08,1.211910e+09,
1.460114e+09,1.634397e+09,1.733958e+09,1.778649e+09,1.787952e+09,
1.774585e+09,1.738877e+09,1.677700e+09,1.590086e+09,1.475868e+09,
1.339591e+09,1.190564e+09,1.037280e+09,8.844656e+08,7.348842e+08,
5.921027e+08,4.610276e+08,3.463198e+08,2.508123e+08,1.750379e+08,
1.176498e+08,7.611066e+07,4.735914e+07,2.832902e+07,1.628696e+07,
9.001732e+06,4.786056e+06,2.450571e+06,1.210284e+06,5.779961e+05,
2.681473e+05,1.220185e+05,5.563009e+04,2.654281e+04,1.421956e+04,
)

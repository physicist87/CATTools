import FWCore.ParameterSet.Config as cms

pileupWeightMap = {
"Startup2015_25ns":cms.vdouble(
    4.8551E-07 , 1.74806E-06, 3.30868E-06, 1.62972E-05, 4.95667E-05,
    0.000606966, 0.003307249, 0.010340741, 0.022852296, 0.041948781,
    0.058609363, 0.067475755, 0.072817826, 0.075931405, 0.076782504,
    0.076202319, 0.074502547, 0.072355135, 0.069642102, 0.064920999,
    0.05725576 , 0.047289348, 0.036528446, 0.026376131, 0.017806872,

    0.011249422, 0.006643385, 0.003662904, 0.001899681, 0.00095614,
    0.00050028 , 0.000297353, 0.000208717, 0.000165856, 0.000139974,
    0.000120481, 0.000103826, 8.88868E-05, 7.53323E-05, 6.30863E-05,
    5.21356E-05, 4.24754E-05, 3.40876E-05, 2.69282E-05, 2.09267E-05,
    1.5989E-05 , 4.8551E-06 , 2.42755E-06, 4.8551E-07, 2.42755E-07,

    1.21378E-07, 4.8551E-08,
),
"Startup2015_50ns":cms.vdouble(
    4.71E-09, 2.86E-06, 4.85E-06, 1.53E-05, 3.14E-05,
    6.28E-05, 1.26E-04, 3.93E-04, 1.42E-03, 6.13E-03,
    1.40E-02, 2.18E-02, 2.94E-02, 4.00E-02, 5.31E-02,
    6.53E-02, 7.64E-02, 8.42E-02, 8.43E-02, 7.68E-02,
    6.64E-02, 5.69E-02, 4.94E-02, 4.35E-02, 3.84E-02,

    3.37E-02, 2.92E-02, 2.49E-02, 2.10E-02, 1.74E-02,
    1.43E-02, 1.16E-02, 9.33E-03, 7.41E-03, 5.81E-03,
    4.49E-03, 3.43E-03, 2.58E-03, 1.91E-03, 1.39E-03,
    1.00E-03, 7.09E-04, 4.93E-04, 3.38E-04, 2.28E-04,
    1.51E-04, 9.83E-05, 6.29E-05, 3.96E-05, 2.45E-05,

    1.49E-05, 4.71E-06, 2.36E-06
),
## based on Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt
#pileupCalc.py -i Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt \
# --inputLumiJSON pileup_JSON_10-28-2015.txt \
# --calcMode true --minBiasXsec 69900 --maxPileupBin 50 --numPileupBins 50 pu.root
"Run2015_25nsV1":cms.vdouble(
    5.784264635e+04, 3.510369942e+05, 3.622903177e+05, 4.773636472e+05, 7.070508127e+05,
    1.136638713e+06, 3.491737096e+06, 2.173135103e+07, 8.021722511e+07, 1.553061868e+08,
    2.207327430e+08, 2.512420657e+08, 2.284340642e+08, 1.633101615e+08, 9.145582404e+07,
    4.054899528e+07, 1.454868131e+07, 4.369129759e+06, 1.158234546e+06, 2.935596118e+05,
    7.844338154e+04, 2.436635167e+04, 9.379132734e+03, 4.347098515e+03, 2.198380378e+03,
    1.117872131e+03, 5.494434772e+02, 2.573455120e+02, 1.143731565e+02, 4.817999154e+01,
    1.923242175e+01, 7.274470595e+00, 2.607128065e+00, 8.853479056e-01, 2.848750387e-01,
    8.685255587e-02, 2.508985765e-02, 6.867543911e-03, 1.781120224e-03, 4.376984859e-04,
    1.019175344e-04, 2.248626707e-05, 4.700923096e-06, 9.312187342e-07, 1.747940650e-07,
    3.108764812e-08, 5.241531875e-09, 8.360538928e-10, 1.271913685e-10, 1.894207013e-11,
),
## based on Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt
#pileupCalc.py -i Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt \
# --inputLumiJSON pileup_JSON_10-28-2015.txt \
# --calcMode true --minBiasXsec 73395 --maxPileupBin 50 --numPileupBins 50 pu.root
"Run2015Up_25nsV1":cms.vdouble(
    4.938693848e+04, 3.169282485e+05, 3.592472735e+05, 4.137154986e+05, 6.313814766e+05,
    9.033466601e+05, 2.112785963e+06, 1.063493882e+07, 4.962012428e+07, 1.156155119e+08,
    1.816270587e+08, 2.291626043e+08, 2.369946302e+08, 1.986114959e+08, 1.333632122e+08,
    7.184707832e+07, 3.144042804e+07, 1.141578903e+07, 3.550271355e+06, 9.935281860e+05,
    2.687188291e+05, 7.648332191e+04, 2.492660311e+04, 9.859560910e+03, 4.653572488e+03,
    2.412617920e+03, 1.271738276e+03, 6.538880787e+02, 3.225849356e+02, 1.518637293e+02,
    6.811668249e+01, 2.909835185e+01, 1.183743270e+01, 4.585752028e+00, 1.691702176e+00,
    5.942861120e-01, 1.988036490e-01, 6.333001109e-02, 1.921105065e-02, 5.549443618e-03,
    1.526530507e-03, 3.998717062e-04, 9.974632379e-05, 2.369389304e-05, 5.359719807e-06,
    1.154554864e-06, 2.368488946e-07, 4.627101141e-08, 8.607176027e-09, 1.525916615e-09,
),
## based on Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt
#pileupCalc.py -i Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt \
# --inputLumiJSON pileup_JSON_10-28-2015.txt \
# --calcMode true --minBiasXsec 66405 --maxPileupBin 50 --numPileupBins 50 pu.root
"Run2015Dn_25nsV1":cms.vdouble(
    6.753888900e+04, 3.885655211e+05, 3.725583872e+05, 5.529133741e+05, 8.016186247e+05,
    1.534956709e+06, 6.827598011e+06, 4.254334114e+07, 1.197729050e+08, 2.005647576e+08,
    2.561532639e+08, 2.564830599e+08, 1.981260239e+08, 1.167974368e+08, 5.293261123e+07,
    1.885245021e+07, 5.469053336e+06, 1.368547366e+06, 3.229823947e+05, 8.048786044e+04,
    2.373082045e+04, 8.877932729e+03, 4.031313912e+03, 1.978563288e+03, 9.642092231e+02,
    4.497806367e+02, 1.984669758e+02, 8.257595619e+01, 3.237265757e+01, 1.195628709e+01,
    4.159998181e+00, 1.363527832e+00, 4.210234627e-01, 1.224667996e-01, 3.355825760e-02,
    8.662622542e-03, 2.106536968e-03, 4.825696060e-04, 1.041415859e-04, 2.117213217e-05,
    4.054934599e-06, 7.316271900e-07, 1.243570567e-07, 1.991664511e-08, 3.003042592e-09,
    4.254817054e-10, 6.660622054e-11, 0.000000000e+00, 0.000000000e+00, 0.000000000e+00,
),
## based on Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON.txt
"Run2015_25ns":cms.vdouble(
3.562366e+04, 2.626834e+05, 3.560686e+05, 3.237645e+05, 5.103119e+05,
6.756850e+05, 1.133830e+06, 3.213949e+06, 1.628510e+07, 5.743382e+07,
1.144710e+08, 1.695310e+08, 2.095693e+08, 2.191489e+08, 1.921836e+08,
1.398997e+08, 8.442993e+07, 4.255114e+07, 1.815900e+07, 6.696812e+06,
2.198639e+06, 6.718743e+05, 2.028372e+05, 6.466618e+04, 2.322280e+04,
9.823330e+03, 4.848262e+03, 2.625057e+03, 1.460976e+03, 8.029910e+02,
4.279394e+02, 2.195906e+02, 1.082387e+02, 5.121299e+01, 2.325526e+01,
1.013406e+01, 4.237992e+00, 1.700783e+00, 6.550108e-01, 2.420793e-01,
8.585708e-02, 2.922157e-02, 9.544221e-03, 2.991489e-03, 8.997987e-04,
2.597262e-04, 7.194492e-05, 1.912496e-05, 4.878867e-06, 1.194420e-06,
2.806225e-07, 6.327691e-08, 1.368838e-08, 2.847973e-09, 5.616552e-10,
1.112978e-10, 2.192513e-11, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
),
"Run2015_25nsUp":cms.vdouble(
2.300807e+04, 2.101571e+05, 3.389636e+05, 2.641974e+05, 3.952283e+05,
5.421029e+05, 7.140553e+05, 1.324331e+06, 4.032592e+06, 1.803465e+07,
5.435155e+07, 1.016893e+08, 1.478461e+08, 1.844194e+08, 2.003241e+08,
1.886962e+08, 1.527183e+08, 1.057464e+08, 6.278739e+07, 3.220962e+07,
1.444583e+07, 5.757923e+06, 2.087777e+06, 7.122946e+05, 2.390273e+05,
8.292867e+04, 3.126089e+04, 1.335274e+04, 6.554439e+03, 3.590548e+03,
2.082400e+03, 1.222783e+03, 7.081796e+02, 3.995497e+02, 2.184857e+02,
1.155801e+02, 5.911195e+01, 2.922222e+01, 1.396275e+01, 6.448239e+00,
2.878197e+00, 1.241675e+00, 5.177286e-01, 2.086426e-01, 8.126619e-02,
3.059306e-02, 1.113121e-02, 3.914431e-03, 1.330463e-03, 4.370642e-04,
1.387707e-04, 4.258546e-05, 1.263101e-05, 3.620999e-06, 1.003314e-06,
2.686983e-07, 6.955533e-08, 1.740177e-08, 4.204790e-09, 9.861214e-10,
2.197106e-10, 6.461720e-11, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
),
"Run2015_25nsDn":cms.vdouble(
5.264662e+04, 3.300800e+05, 3.599620e+05, 4.376687e+05, 6.602346e+05,
9.828107e+05, 2.532948e+06, 1.415339e+07, 6.072109e+07, 1.307227e+08,
1.972495e+08, 2.394131e+08, 2.360435e+08, 1.863759e+08, 1.168122e+08,
5.839727e+07, 2.365859e+07, 7.967812e+06, 2.318762e+06, 6.193743e+05,
1.649212e+05, 4.797363e+04, 1.656919e+04, 7.023570e+03, 3.454207e+03,
1.795846e+03, 9.260977e+02, 4.603714e+02, 2.183999e+02, 9.857803e+01,
4.230067e+01, 1.725331e+01, 6.688621e+00, 2.464532e+00, 8.631042e-01,
2.872907e-01, 9.088840e-02, 2.732899e-02, 7.810292e-03, 2.121486e-03,
5.477014e-04, 1.343940e-04, 3.134375e-05, 6.947995e-06, 1.463890e-06,
2.931590e-07, 5.580575e-08, 1.009423e-08, 1.737620e-09, 2.793669e-10,
5.466738e-11, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
),
## based on Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON_v2.txt
"Run2015_50ns":cms.vdouble(
7.087483e+03, 9.511030e+03, 2.352521e+04, 2.352527e+04, 2.257047e+04,
2.557498e+04, 4.700163e+04, 8.057339e+04, 1.346229e+05, 1.982567e+05,
2.680645e+05, 3.933959e+05, 6.857333e+05, 1.218917e+06, 1.943049e+06,
2.766453e+06, 3.617301e+06, 4.400833e+06, 5.024569e+06, 5.459438e+06,
5.721149e+06, 5.821773e+06, 5.751740e+06, 5.491088e+06, 5.032006e+06,
4.400538e+06, 3.659264e+06, 2.889582e+06, 2.167181e+06, 1.545090e+06,
1.048105e+06, 6.769912e+05, 4.167884e+05, 2.449436e+05, 1.377560e+05,
7.442186e+04, 3.883143e+04, 1.970785e+04, 9.812407e+03, 4.837342e+03,
2.381747e+03, 1.178858e+03, 5.883288e+02, 2.958213e+02, 1.492868e+02,
7.519977e+01, 3.759447e+01, 1.855839e+01, 9.009822e+00, 4.289080e+00,
1.997948e+00, 9.094299e-01, 4.041284e-01, 1.752161e-01, 7.409085e-02,
3.054807e-02, 1.227905e-02, 4.811366e-03, 1.837705e-03, 6.842000e-04,
2.483114e-04, 8.784810e-05, 3.029786e-05, 1.018740e-05, 3.339771e-06,
1.067602e-06, 3.327926e-07, 1.011640e-07, 2.999845e-08, 8.679126e-09,
2.449543e-09, 6.777441e-10, 1.866632e-10, 4.884032e-11, 1.703637e-12,
1.703637e-12, 0.000000e+00, 0.000000e+00, 0.000000e+00,
),
"Run2015_50nsUp":cms.vdouble(
6.313388e+03, 6.873685e+03, 2.040178e+04, 2.153487e+04, 2.128849e+04,
1.978332e+04, 2.968305e+04, 5.074694e+04, 8.268386e+04, 1.300567e+05,
1.828830e+05, 2.400294e+05, 3.346819e+05, 5.427883e+05, 9.294613e+05,
1.481114e+06, 2.133116e+06, 2.832513e+06, 3.527184e+06, 4.145578e+06,
4.632956e+06, 4.978331e+06, 5.194458e+06, 5.289911e+06, 5.259125e+06,
5.088332e+06, 4.767672e+06, 4.305167e+06, 3.733339e+06, 3.103193e+06,
2.471319e+06, 1.886189e+06, 1.380707e+06, 9.699768e+05, 6.543571e+05,
4.242004e+05, 2.645363e+05, 1.589529e+05, 9.225591e+04, 5.190222e+04,
2.843593e+04, 1.525993e+04, 8.074851e+03, 4.242736e+03, 2.227830e+03,
1.174800e+03, 6.237129e+02, 3.333398e+02, 1.789068e+02, 9.605829e+01,
5.137098e+01, 2.725037e+01, 1.428766e+01, 7.383642e+00, 3.753153e+00,
1.873652e+00, 9.176902e-01, 4.406644e-01, 2.073552e-01, 9.558182e-02,
4.315141e-02, 1.907709e-02, 8.258229e-03, 3.500233e-03, 1.452551e-03,
5.901861e-04, 2.347879e-04, 9.145415e-05, 3.488095e-05, 1.302719e-05,
4.764445e-06, 1.706485e-06, 5.986087e-07, 2.056516e-07, 6.922008e-08,
2.281658e-08, 7.369969e-09, 2.331993e-09, 7.278612e-10,
),
"Run2015_50nsDn":cms.vdouble(
7.701593e+03, 1.400052e+04, 2.640035e+04, 2.601043e+04, 2.456513e+04,
4.149829e+04, 7.730425e+04, 1.384450e+05, 2.163236e+05, 3.036261e+05,
4.767971e+05, 9.023773e+05, 1.649800e+06, 2.608330e+06, 3.653546e+06,
4.660816e+06, 5.479877e+06, 6.042584e+06, 6.366013e+06, 6.467527e+06,
6.330346e+06, 5.926308e+06, 5.259078e+06, 4.394366e+06, 3.446484e+06,
2.536274e+06, 1.753016e+06, 1.139454e+06, 6.972594e+05, 4.022479e+05,
2.192863e+05, 1.134122e+05, 5.598878e+04, 2.661314e+04, 1.231535e+04,
5.618047e+03, 2.556987e+03, 1.171485e+03, 5.422320e+02, 2.530415e+02,
1.183292e+02, 5.501693e+01, 2.524473e+01, 1.136303e+01, 4.995234e+00,
2.138247e+00, 8.895267e-01, 3.591945e-01, 1.406829e-01, 5.341853e-02,
1.965893e-02, 7.010925e-03, 2.422721e-03, 8.112106e-04, 2.631926e-04,
8.274545e-05, 2.521020e-05, 7.444037e-06, 2.130509e-06, 5.910894e-07,
1.589893e-07, 4.146700e-08, 1.048559e-08, 2.575663e-09, 6.121236e-10,
1.480270e-10, 2.868034e-11, 1.703637e-12, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
0.000000e+00, 0.000000e+00, 0.000000e+00, 0.000000e+00,
),
#pileupCalc.py -i Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69000 --maxPileupBin 50 --numPileupBins 50 PileUpData.root
"Run2015_25nsSilver":cms.vdouble(
9.373792e+04, 5.147748e+05, 5.477386e+05, 7.272656e+05, 9.528581e+05,
1.594241e+06, 5.994059e+06, 3.688192e+07, 1.337298e+08, 2.646688e+08,
3.566119e+08, 3.752351e+08, 3.201104e+08, 2.175155e+08, 1.165450e+08,
4.982125e+07, 1.818759e+07, 7.115496e+06, 3.802231e+06, 2.238755e+06,
1.082882e+06, 3.899426e+05, 1.035763e+05, 2.127373e+04, 4.110165e+03,
1.110691e+03, 4.444823e+02, 1.968216e+02, 8.462925e+01, 3.452794e+01,
1.333227e+01, 4.871099e+00, 1.683953e+00, 5.508210e-01, 1.704775e-01,
4.992282e-02, 1.383267e-02, 3.626510e-03, 8.995978e-04, 2.111478e-04,
4.689276e-05, 9.853920e-06, 1.959294e-06, 3.686198e-07, 6.562482e-08,
1.105342e-08, 1.762478e-09, 2.614969e-10, 4.768003e-11, 0.000000e+00,
),
#pileupCalc.py -i Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 72450 --maxPileupBin 50 --numPileupBins 50 PileUpDataUp.root
"Run2015_25nsSilverUp":cms.vdouble(
7.893101e+04, 4.684151e+05, 5.290962e+05, 6.458729e+05, 8.704214e+05,
1.224246e+06, 3.418512e+06, 1.852572e+07, 8.223574e+07, 1.962966e+08,
3.040807e+08, 3.569436e+08, 3.442281e+08, 2.729589e+08, 1.750935e+08,
9.054778e+07, 3.844931e+07, 1.454236e+07, 6.162293e+06, 3.487670e+06,
2.100740e+06, 1.050937e+06, 4.019842e+05, 1.164671e+05, 2.645202e+04,
5.431173e+03, 1.410622e+03, 5.475743e+02, 2.502406e+02, 1.138022e+02,
4.952263e+01, 2.050837e+01, 8.077706e+00, 3.025884e+00, 1.078004e+00,
3.652502e-01, 1.176960e-01, 3.606893e-02, 1.051249e-02, 2.913933e-03,
7.681675e-04, 1.925913e-04, 4.592234e-05, 1.041407e-05, 2.246101e-06,
4.607372e-07, 8.988719e-08, 1.667630e-08, 2.942386e-09, 4.960389e-10,
),
#pileupCalc.py -i Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 68827 --maxPileupBin 50 --numPileupBins 50 PileUpDataDn.root
"Run2015_25nsSilverDn":cms.vdouble(
9.453443e+04, 5.172013e+05, 5.488862e+05, 7.316891e+05, 9.575754e+05,
1.619101e+06, 6.187616e+06, 3.815594e+07, 1.367797e+08, 2.682355e+08,
3.589656e+08, 3.755619e+08, 3.181626e+08, 2.143289e+08, 1.137139e+08,
4.813486e+07, 1.747653e+07, 6.893342e+06, 3.722577e+06, 2.179011e+06,
1.037810e+06, 3.667765e+05, 9.555545e+04, 1.933479e+04, 3.752038e+03,
1.041156e+03, 4.218684e+02, 1.864341e+02, 7.972045e+01, 3.232314e+01,
1.239948e+01, 4.499465e+00, 1.544464e+00, 5.014779e-01, 1.540215e-01,
4.474717e-02, 1.229715e-02, 3.196678e-03, 7.860492e-04, 1.828349e-04,
4.022806e-05, 8.372651e-06, 1.648401e-06, 3.070010e-07, 5.408534e-08,
9.014751e-09, 1.417573e-09, 2.107582e-10, 3.776435e-11, 0.000000e+00,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69000 --maxPileupBin 50 --numPileupBins 50 PileUpData.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON":cms.vdouble(
1.220587e+05,5.831995e+05,8.283072e+05,1.195209e+06,2.112880e+06,
4.961396e+06,1.551333e+07,6.006134e+07,1.649140e+08,2.803063e+08,
3.620212e+08,3.869629e+08,3.411577e+08,2.426751e+08,1.388794e+08,
6.531371e+07,2.692979e+07,1.135401e+07,5.679176e+06,3.030398e+06,
1.402960e+06,5.120442e+05,1.467754e+05,3.530236e+04,8.271279e+03,
2.235610e+03,7.213805e+02,2.588496e+02,9.727087e+01,3.687161e+01,
1.372748e+01,4.931712e+00,1.692408e+00,5.518936e-01,1.706013e-01,
4.993580e-02,1.383391e-02,3.626617e-03,8.996063e-04,2.111484e-04,
4.689276e-05,9.853920e-06,1.959294e-06,3.686198e-07,6.562482e-08,
1.105342e-08,1.762478e-09,2.614969e-10,4.768003e-11,0.000000e+00,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 72450 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Up":cms.vdouble(
1.029516e+05,5.286883e+05,7.668740e+05,1.061053e+06,1.735315e+06,
3.657311e+06,9.973390e+06,3.526300e+07,1.114776e+08,2.196883e+08,
3.115377e+08,3.636366e+08,3.592381e+08,2.952095e+08,1.988841e+08,
1.103235e+08,5.170482e+07,2.197805e+07,9.831562e+06,5.166228e+06,
2.836901e+06,1.361640e+06,5.264128e+05,1.630398e+05,4.259070e+04,
1.058456e+04,2.923748e+03,9.556848e+02,3.513003e+02,1.367717e+02,
5.431361e+01,2.142533e+01,8.238738e+00,3.051831e+00,1.081840e+00,
3.657705e-01,1.177607e-01,3.607632e-02,1.051327e-02,2.914007e-03,
7.681742e-04,1.925918e-04,4.592234e-05,1.041407e-05,2.246101e-06,
4.607372e-07,8.988719e-08,1.667630e-08,2.942386e-09,4.960389e-10,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 68827 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Dn":cms.vdouble(
1.230562e+05,5.861159e+05,8.317676e+05,1.202910e+06,2.135561e+06,
5.044260e+06,1.589329e+07,6.168769e+07,1.679286e+08,2.834574e+08,
3.644021e+08,3.876037e+08,3.394957e+08,2.395611e+08,1.358982e+08,
6.337816e+07,2.600405e+07,1.099952e+07,5.532071e+06,2.939116e+06,
1.343685e+06,4.827610e+05,1.362991e+05,3.246134e+04,7.612338e+03,
2.075276e+03,6.739759e+02,2.423396e+02,9.099397e+01,3.439010e+01,
1.274402e+01,4.551673e+00,1.551656e+00,5.023785e-01,1.541240e-01,
4.475778e-02,1.229815e-02,3.196763e-03,7.860559e-04,1.828352e-04,
4.022806e-05,8.372651e-06,1.648401e-06,3.070010e-07,5.408534e-08,
9.014751e-09,1.417573e-09,2.107582e-10,3.776435e-11,0.000000e+00,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69000 --maxPileupBin 50 --numPileupBins 50 PileUpData.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver":cms.vdouble(
1.478825e+05,6.665130e+05,8.865608e+05,1.317971e+06,2.238593e+06,
5.098929e+06,1.653031e+07,6.737825e+07,1.983429e+08,3.545547e+08,
4.471784e+08,4.534807e+08,3.840413e+08,2.665228e+08,1.499735e+08,
6.941467e+07,2.810179e+07,1.161328e+07,5.724702e+06,3.036999e+06,
1.403774e+06,5.121296e+05,1.467829e+05,3.530288e+04,8.271308e+03,
2.235611e+03,7.213805e+02,2.588496e+02,9.727087e+01,3.687161e+01,
1.372748e+01,4.931712e+00,1.692408e+00,5.518936e-01,1.706013e-01,
4.993580e-02,1.383391e-02,3.626617e-03,8.996063e-04,2.111484e-04,
4.689276e-05,9.853920e-06,1.959294e-06,3.686198e-07,6.562482e-08,
1.105342e-08,1.762478e-09,2.614969e-10,4.768003e-11,0.000000e+00,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 72450 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver_Up":cms.vdouble(
1.245894e+05,6.115229e+05,8.139674e+05,1.174556e+06,1.861536e+06,
3.757996e+06,1.046677e+07,3.878034e+07,1.299670e+08,2.738493e+08,
3.926627e+08,4.385425e+08,4.132558e+08,3.288866e+08,2.171753e+08,
1.186414e+08,5.474429e+07,2.285530e+07,1.003267e+07,5.203763e+06,
2.842808e+06,1.362444e+06,5.265071e+05,1.630491e+05,4.259147e+04,
1.058461e+04,2.923751e+03,9.556849e+02,3.513003e+02,1.367717e+02,
5.431361e+01,2.142533e+01,8.238738e+00,3.051831e+00,1.081840e+00,
3.657705e-01,1.177607e-01,3.607632e-02,1.051327e-02,2.914007e-03,
7.681742e-04,1.925918e-04,4.592234e-05,1.041407e-05,2.246101e-06,
4.607372e-07,8.988719e-08,1.667630e-08,2.942386e-09,4.960389e-10,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 68827 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver_Dn":cms.vdouble(
1.491022e+05,6.694280e+05,8.906790e+05,1.326163e+06,2.261106e+06,
5.184996e+06,1.694926e+07,6.928090e+07,2.022952e+08,3.586372e+08,
4.495250e+08,4.535943e+08,3.817982e+08,2.629327e+08,1.466714e+08,
6.731367e+07,2.711365e+07,1.124152e+07,5.573984e+06,2.945115e+06,
1.344416e+06,4.828365e+05,1.363056e+05,3.246179e+04,7.612363e+03,
2.075277e+03,6.739760e+02,2.423396e+02,9.099397e+01,3.439010e+01,
1.274402e+01,4.551673e+00,1.551656e+00,5.023785e-01,1.541240e-01,
4.475778e-02,1.229815e-02,3.196763e-03,7.860559e-04,1.828352e-04,
4.022806e-05,8.372651e-06,1.648401e-06,3.070010e-07,5.408534e-08,
9.014751e-09,1.417573e-09,2.107582e-10,3.776435e-11,0.000000e+00,
),
#from SimGeneral/MixingModule/python/mix_2015_25ns_FallMC_matchData_PoissonOOTPU_cfi.py
"2015_25ns_FallMC":cms.vdouble(
0.000108643,0.000388957,0.000332882,0.00038397, 0.000549167,
0.00105412, 0.00459007, 0.0210314,  0.0573688,  0.103986,
0.142369,   0.157729,   0.147685,   0.121027,   0.08855,
0.0582866,  0.0348526,  0.019457,   0.0107907,  0.00654313,
0.00463195, 0.00370927, 0.0031137,  0.00261141, 0.00215499,
0.00174491, 0.00138268, 0.00106731, 0.000798828,0.00057785,
0.00040336, 0.00027161, 0.000176535,0.00011092, 6.75502e-05,
4.00323e-05,2.32123e-05,1.32585e-05,7.51611e-06,4.25902e-06,
2.42513e-06,1.39077e-06,8.02452e-07,4.64159e-07,2.67845e-07,
1.5344e-07,8.68966e-08,4.84931e-08,2.6606e-08,  1.433e-08
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69000 --maxPileupBin 50 --numPileupBins 50 PileUpData.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2":cms.vdouble(
1.220587e+05,5.832009e+05,8.283427e+05,1.195815e+06,2.119613e+06,
5.010293e+06,1.574703e+07,6.080965e+07,1.665951e+08,2.832551e+08,
3.667106e+08,3.940118e+08,3.501486e+08,2.514499e+08,1.451475e+08,
6.855432e+07,2.814645e+07,1.168906e+07,5.747825e+06,3.041060e+06,
1.404243e+06,5.121667e+05,1.467848e+05,3.530294e+04,8.271308e+03,
2.235611e+03,7.213805e+02,2.588496e+02,9.727087e+01,3.687161e+01,
1.372748e+01,4.931712e+00,1.692408e+00,5.518936e-01,1.706013e-01,
4.993580e-02,1.383391e-02,3.626617e-03,8.996063e-04,2.111484e-04,
4.689276e-05,9.853920e-06,1.959294e-06,3.686198e-07,6.562482e-08,
1.105342e-08,1.762478e-09,2.614969e-10,4.768003e-11,0.000000e+00,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 72450 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_Up":cms.vdouble(
1.029516e+05,5.286893e+05,7.668968e+05,1.061415e+06,1.739212e+06,
3.685831e+06,1.011571e+07,3.575284e+07,1.126743e+08,2.219109e+08,
3.150947e+08,3.690681e+08,3.668535e+08,3.040033e+08,2.066842e+08,
1.155051e+08,5.426949e+07,2.292858e+07,1.009788e+07,5.223375e+06,
2.846450e+06,1.362907e+06,5.265489e+05,1.630518e+05,4.259158e+04,
1.058462e+04,2.923751e+03,9.556849e+02,3.513003e+02,1.367717e+02,
5.431361e+01,2.142533e+01,8.238738e+00,3.051831e+00,1.081840e+00,
3.657705e-01,1.177607e-01,3.607632e-02,1.051327e-02,2.914007e-03,
7.681742e-04,1.925918e-04,4.592234e-05,1.041407e-05,2.246101e-06,
4.607372e-07,8.988719e-08,1.667630e-08,2.942386e-09,4.960389e-10,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 68827 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_Dn":cms.vdouble(
1.230562e+05,5.861173e+05,8.318040e+05,1.203532e+06,2.142487e+06,
5.094521e+06,1.613290e+07,6.245185e+07,1.696378e+08,2.864484e+08,
3.691590e+08,3.947410e+08,3.485420e+08,2.483031e+08,1.420676e+08,
6.652413e+07,2.716754e+07,1.131482e+07,5.595598e+06,2.948814e+06,
1.344833e+06,4.828685e+05,1.363072e+05,3.246184e+04,7.612363e+03,
2.075277e+03,6.739760e+02,2.423396e+02,9.099397e+01,3.439010e+01,
1.274402e+01,4.551673e+00,1.551656e+00,5.023785e-01,1.541240e-01,
4.475778e-02,1.229815e-02,3.196763e-03,7.860559e-04,1.828352e-04,
4.022806e-05,8.372651e-06,1.648401e-06,3.070010e-07,5.408534e-08,
9.014751e-09,1.417573e-09,2.107582e-10,3.776435e-11,0.000000e+00,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver_v2.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69000 --maxPileupBin 50 --numPileupBins 50 PileUpData.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver_v2":cms.vdouble(
1.478826e+05,6.665143e+05,8.865964e+05,1.318577e+06,2.245325e+06,
5.147825e+06,1.676401e+07,6.812656e+07,2.000240e+08,3.575035e+08,
4.518679e+08,4.605295e+08,3.930321e+08,2.752975e+08,1.562416e+08,
7.265527e+07,2.931845e+07,1.194832e+07,5.793352e+06,3.047662e+06,
1.405058e+06,5.122521e+05,1.467923e+05,3.530347e+04,8.271338e+03,
2.235613e+03,7.213806e+02,2.588496e+02,9.727087e+01,3.687161e+01,
1.372748e+01,4.931712e+00,1.692408e+00,5.518936e-01,1.706013e-01,
4.993580e-02,1.383391e-02,3.626617e-03,8.996063e-04,2.111484e-04,
4.689276e-05,9.853920e-06,1.959294e-06,3.686198e-07,6.562482e-08,
1.105342e-08,1.762478e-09,2.614969e-10,4.768003e-11,0.000000e+00,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver_v2.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 72450 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver_v2_Up":cms.vdouble(
1.245894e+05,6.115238e+05,8.139901e+05,1.174917e+06,1.865434e+06,
3.786516e+06,1.060908e+07,3.927018e+07,1.311636e+08,2.760719e+08,
3.962197e+08,4.439740e+08,4.208711e+08,3.376804e+08,2.249754e+08,
1.238230e+08,5.730897e+07,2.380584e+07,1.029899e+07,5.260911e+06,
2.852357e+06,1.363710e+06,5.266432e+05,1.630612e+05,4.259235e+04,
1.058467e+04,2.923753e+03,9.556850e+02,3.513003e+02,1.367717e+02,
5.431361e+01,2.142533e+01,8.238738e+00,3.051831e+00,1.081840e+00,
3.657705e-01,1.177607e-01,3.607632e-02,1.051327e-02,2.914007e-03,
7.681742e-04,1.925918e-04,4.592234e-05,1.041407e-05,2.246101e-06,
4.607372e-07,8.988719e-08,1.667630e-08,2.942386e-09,4.960389e-10,
),
#pileupCalc.py -i Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver_v2.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 68827 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root
"Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver_v2_Dn":cms.vdouble(
1.491022e+05,6.694294e+05,8.907154e+05,1.326785e+06,2.268031e+06,
5.235257e+06,1.718887e+07,7.004505e+07,2.040044e+08,3.616282e+08,
4.542819e+08,4.607317e+08,3.908445e+08,2.716747e+08,1.528409e+08,
7.045964e+07,2.827714e+07,1.155682e+07,5.637511e+06,2.954814e+06,
1.345563e+06,4.829440e+05,1.363137e+05,3.246229e+04,7.612387e+03,
2.075278e+03,6.739760e+02,2.423396e+02,9.099397e+01,3.439010e+01,
1.274402e+01,4.551673e+00,1.551656e+00,5.023785e-01,1.541240e-01,
4.475778e-02,1.229815e-02,3.196763e-03,7.860559e-04,1.828352e-04,
4.022806e-05,8.372651e-06,1.648401e-06,3.070010e-07,5.408534e-08,
9.014751e-09,1.417573e-09,2.107582e-10,3.776435e-11,0.000000e+00,
),
#pileupCalc.py -i Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69000 --maxPileupBin 50 --numPileupBins 50 PileUpData.root
"Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON":cms.vdouble(
1.220587e+05,5.832009e+05,8.283427e+05,1.195815e+06,2.119613e+06,
5.010293e+06,1.574703e+07,6.080965e+07,1.665951e+08,2.832551e+08,
3.667106e+08,3.940118e+08,3.501486e+08,2.514499e+08,1.451475e+08,
6.855432e+07,2.814645e+07,1.168906e+07,5.747825e+06,3.041060e+06,
1.404243e+06,5.121667e+05,1.467848e+05,3.530294e+04,8.271308e+03,
2.235611e+03,7.213805e+02,2.588496e+02,9.727087e+01,3.687161e+01,
1.372748e+01,4.931712e+00,1.692408e+00,5.518936e-01,1.706013e-01,
4.993580e-02,1.383391e-02,3.626617e-03,8.996063e-04,2.111484e-04,
4.689276e-05,9.853920e-06,1.959294e-06,3.686198e-07,6.562482e-08,
1.105342e-08,1.762478e-09,2.614969e-10,4.768003e-11,0.000000e+00,
),
#pileupCalc.py -i Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 72450 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root
"Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Up":cms.vdouble(
1.029516e+05,5.286893e+05,7.668968e+05,1.061415e+06,1.739212e+06,
3.685831e+06,1.011571e+07,3.575284e+07,1.126743e+08,2.219109e+08,
3.150947e+08,3.690681e+08,3.668535e+08,3.040033e+08,2.066842e+08,
1.155051e+08,5.426949e+07,2.292858e+07,1.009788e+07,5.223375e+06,
2.846450e+06,1.362907e+06,5.265489e+05,1.630518e+05,4.259158e+04,
1.058462e+04,2.923751e+03,9.556849e+02,3.513003e+02,1.367717e+02,
5.431361e+01,2.142533e+01,8.238738e+00,3.051831e+00,1.081840e+00,
3.657705e-01,1.177607e-01,3.607632e-02,1.051327e-02,2.914007e-03,
7.681742e-04,1.925918e-04,4.592234e-05,1.041407e-05,2.246101e-06,
4.607372e-07,8.988719e-08,1.667630e-08,2.942386e-09,4.960389e-10,
),
#pileupCalc.py -i Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 65550 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root 
"Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Dn":cms.vdouble(
1.427749e+05,6.444441e+05,9.061017e+05,1.372617e+06,2.672389e+06,
7.173998e+06,2.649289e+07,1.020630e+08,2.326072e+08,3.478602e+08,
4.102728e+08,3.953585e+08,3.037469e+08,1.832171e+08,8.777292e+07,
3.521316e+07,1.375593e+07,6.377487e+06,3.262943e+06,1.447631e+06,
4.949894e+05,1.300750e+05,2.860943e+04,6.333355e+03,1.680793e+03,
5.330460e+02,1.853835e+02,6.666463e+01,2.386620e+01,8.286543e+00,
2.746726e+00,8.620617e-01,2.551907e-01,7.113181e-02,1.865672e-02,
4.603238e-03,1.068332e-03,2.332118e-04,4.788436e-05,9.247787e-06,
1.679908e-06,2.870404e-07,4.613098e-08,6.975087e-09,9.940954e-10,
1.331527e-10,1.596040e-11,0.000000e+00,0.000000e+00,0.000000e+00,
),
#pileupCalc.py -i Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69000 --maxPileupBin 50 --numPileupBins 50 PileUpData.root
"Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver":cms.vdouble(
1.478826e+05,6.665143e+05,8.865964e+05,1.318577e+06,2.245325e+06,
5.147825e+06,1.676401e+07,6.812656e+07,2.000240e+08,3.575035e+08,
4.518679e+08,4.605295e+08,3.930321e+08,2.752975e+08,1.562416e+08,
7.265527e+07,2.931845e+07,1.194832e+07,5.793352e+06,3.047662e+06,
1.405058e+06,5.122521e+05,1.467923e+05,3.530347e+04,8.271338e+03,
2.235613e+03,7.213806e+02,2.588496e+02,9.727087e+01,3.687161e+01,
1.372748e+01,4.931712e+00,1.692408e+00,5.518936e-01,1.706013e-01,
4.993580e-02,1.383391e-02,3.626617e-03,8.996063e-04,2.111484e-04,
4.689276e-05,9.853920e-06,1.959294e-06,3.686198e-07,6.562482e-08,
1.105342e-08,1.762478e-09,2.614969e-10,4.768003e-11,0.000000e+00,
),
#pileupCalc.py -i Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 72450 --maxPileupBin 50 --numPileupBins 50 PileUpData_Up.root
"Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver_Up":cms.vdouble(
1.245894e+05,6.115238e+05,8.139901e+05,1.174917e+06,1.865434e+06,
3.786516e+06,1.060908e+07,3.927018e+07,1.311636e+08,2.760719e+08,
3.962197e+08,4.439740e+08,4.208711e+08,3.376804e+08,2.249754e+08,
1.238230e+08,5.730897e+07,2.380584e+07,1.029899e+07,5.260911e+06,
2.852357e+06,1.363710e+06,5.266432e+05,1.630612e+05,4.259235e+04,
1.058467e+04,2.923753e+03,9.556850e+02,3.513003e+02,1.367717e+02,
5.431361e+01,2.142533e+01,8.238738e+00,3.051831e+00,1.081840e+00,
3.657705e-01,1.177607e-01,3.607632e-02,1.051327e-02,2.914007e-03,
7.681742e-04,1.925918e-04,4.592234e-05,1.041407e-05,2.246101e-06,
4.607372e-07,8.988719e-08,1.667630e-08,2.942386e-09,4.960389e-10,
),
#pileupCalc.py -i Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 65550 --maxPileupBin 50 --numPileupBins 50 PileUpData_Dn.root 
"Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver_Dn":cms.vdouble(
1.732157e+05,7.273319e+05,9.789258e+05,1.505933e+06,2.793073e+06,
7.418148e+06,2.869753e+07,1.173119e+08,2.878188e+08,4.371210e+08,
4.908524e+08,4.500305e+08,3.350005e+08,1.981389e+08,9.338476e+07,
3.680859e+07,1.409690e+07,6.433635e+06,3.270392e+06,1.448456e+06,
4.950657e+05,1.300808e+05,2.860977e+04,6.333371e+03,1.680793e+03,
5.330460e+02,1.853835e+02,6.666463e+01,2.386620e+01,8.286543e+00,
2.746726e+00,8.620617e-01,2.551907e-01,7.113181e-02,1.865672e-02,
4.603238e-03,1.068332e-03,2.332118e-04,4.788436e-05,9.247787e-06,
1.679908e-06,2.870404e-07,4.613098e-08,6.975087e-09,9.940954e-10,
1.331527e-10,1.596040e-11,0.000000e+00,0.000000e+00,0.000000e+00,
),
}

#pileupWeight.reweightMethod = "NVertex"
#pileupWeight.simpleWeights = [ # Weights starts from 1-vertex
#    1,
#    9.571429, 1.692308, 0.610811, 0.372213, 0.433144,
#    0.440753, 0.415084, 0.432604, 0.437338, 0.443846,
#    0.440794, 0.450929, 0.445799, 0.443721, 0.438115,
#    0.431091, 0.423091, 0.412340, 0.379626, 0.361282,
#    0.327449, 0.296309, 0.261543, 0.241164, 0.196814,
#    0.162705, 0.137715, 0.118497, 0.098170, 0.077295,
#    0.074979, 0.056573, 0.040787, 0.039046, 0.032877,
#    0.020677, 0.026087, 0.023438, 0.030675, 0.008475, 0.010638,
#]

# SatQuMA_UI

**INTRODUCTION**

User Interface (V1) to support interaction with SatQuMA. The version for SatQuMA used is a bespoke version 
that enables users to write values for three parameters. These parameters are:

Mu1 - Intensity value of signal state,
Mu2 - Intensity value of decoy state, and
PxB - Receiver basis bias.

SatQuMA_UI enables user input and returns the maximised finite key, by optimising over the remaining BB84 
WCP QKD protocol parameter space. For details of this, see dedicated SatQuMA documentation, which is being 
maintained at arXiv:2109.01686 (https://arxiv.org/abs/2109.01686).

All output optimised parameters are printed to screen via SatQuMA_UI on different tabs. The Tabs are:

Satellite Overpass: Parameter that specify the satellite overpass,
Security Properties: All security parameters for the QKD protocol,
Channel Properties: All loss parameters,
System Properties: All transmitter and receiver parameters, and
Resources: A list of resources for background material.

Further tabs will be added to increase functionality. If you have any suggestions for improvements, please 
send them to jsmdrsidhu@gmail.com.


**RUNNING SATQUMA_UI**

TKinter is an open-source package supported by Python. A current download of Python 3 will have all the 
supporting packages required to run SatQuMA_UI.

Download the root directory and run main.py. This will generate a UI that runs SatQuMA.


**BUGS and COMMENTS**

Please report any bugs or comments to jsmdrsidhu@gmail.com.

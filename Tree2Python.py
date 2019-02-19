import numpy as np
import math
#import matplotlib as plt
from matplotlib import pylab as plt
from ROOT import TTree, TFile, TH2D, TCanvas, TH1F, gROOT
from root_numpy import array2hist, hist2array, fill_hist, tree2array,root2array

inputFile="PSBoxPS.root"
E_kinetic=root2array(inputFile,treename="PhaseSpace", branches="Ekine")

plt.hist(E_kinetic)
plt.pause(0.01)
input("press enter to exit")

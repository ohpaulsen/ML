from matplotlib.pyplot import *
import numpy as np

#input from files...
X, Y, Z = np.genfromtxt(r'test.txt', unpack=True)
X2, Y2 = np.genfromtxt(r'test2.txt', unpack=True)

#length of the input values
N = len(X)
N2 = len(X2)

#Linspace calculation for the percent axis
XI = np.linspace(X.min(), X.max(), N)
YI = np.linspace(Y.min(), Y.max(), N)

#percent range for x-axis on stackplot
percent = YI / YI.sum(axis=0).astype(float) * 100

#Range for the x-axis on stackplot
Xrange = np.arange(N)

#Nan to groups based on Z value
test1 = np.where(Z == 1, Z, np.nan)
test2 = np.where(Z == 2, Z, np.nan)

#Scatter plot
scatter(X,Y,Z)

#creating the figures
fig, ax = subplots()
fig2, ax2 = subplots()

#Stackplot
ax.stackplot(X2,Y2)
ax.stackplot(Xrange,X,Y)
ax2.stackplot(percent,X,Y)

#Zoom for the stackplots
ax2.margins(0,0)
ax.margins(0,0)

show(block=True)

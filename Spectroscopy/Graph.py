#This code produces the Beer Graph for the spectroscopy lab
import matplotlib.pyplot as plt
import numpy as np

#Data
Concentration=np.array([2, 4, 6, 8, 10, 15])
Absorbance=np.array([0.064, 0.117, 0.177, 0.240, 0.302, 0.440])

#Plot
figAbsorb, axg =plt.subplots(figsize=(8,8))
plt.scatter(Concentration, Absorbance, color='b')
plt.xlabel('Concentration (ppm)')
plt.ylabel('Absorbance Reading')

#X intercept and Slope
m, b = np.polyfit(Concentration, Absorbance, 1)
xseq = np.linspace(0,17, num=100)

#Unknown Cu solution
#y=mx+b
y=0.125
UnkCon=(y-b)/m

#Plot Unknown
plt.scatter(UnkCon, y, color='g', label='Unknown Cu Solution')
UnkStr="line of best fit; y = "+str(m)+"x "+str(b)

#Regression Line
axg.plot(xseq, m * xseq + b, color='r', label=UnkStr)

#R^2 Value
actual=[m*Concentration[0]+b,m*Concentration[1]+b, m*Concentration[2]+b, m*Concentration[3]+b, m*Concentration[4]+b, m*Concentration[5]+b]
corr_matrix=np.corrcoef(actual, Absorbance)
corr= corr_matrix[0,1]
R_sq = corr**2
Rstr="R squared = "+str(R_sq)
axg.text(0,0.46,Rstr)

#ScatterPlot Graph
figAbsorb.suptitle('Absorbance reading of Different Concentrations')
axg.legend()
plt.show()
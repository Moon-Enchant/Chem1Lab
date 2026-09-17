#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt

#Data
measurements=['1','2','3','4','5']
DensityGrad=[0.926,0.989,1.001,0.911,0.983]
DensityPipe=[0.9,1.0,0.9,1.0,0.9]
AverageGrad= [0.926,0.926,0.926,0.926,0.926]
AveragePipe=[0.94,0.94,0.94,0.94,0.94]
Reference=[0.998,0.998,0.998,0.998,0.998]
StdDevGrad=[0.041,0.041,0.041,0.041,0.041]
StdDevPipe=[0.055,0.055,0.055,0.055,0.055]

#Plot
figGrad, axg = plt.subplots()
figPipe, axp = plt.subplots()
plt.xlabel('Measurements')
plt.ylabel('Density (g/ml)')

#Graduated cylinder graph
figGrad.suptitle('Density of water 21°C from a Graduated Cylinder')
axg.bar(measurements,DensityGrad,color='b')
axg.plot(measurements,AverageGrad,'--', color='r',label='Average=0.962±0.041 g/ml')
axg.plot(measurements,Reference,color='g', label='Reference=0.998 g/ml')
axg.errorbar(measurements,DensityGrad,yerr=StdDevGrad, fmt='o', linewidth=2, capsize=6)
axg.legend()

#Volumetric pipette graph
figPipe.suptitle('Density of water at 3°C from a Volumetric Pipette')
axp.bar(measurements,DensityPipe,color='b')
axp.plot(measurements,AveragePipe,'--', color='r',label='Average=0.94±0.055 g/ml')
axp.plot(measurements,Reference,color='g', label='Reference=0.998 g/ml')
axp.errorbar(measurements,DensityPipe, yerr=StdDevPipe, fmt='o', linewidth=2, capsize=6)
axp.legend()

#Show plot
plt.show()
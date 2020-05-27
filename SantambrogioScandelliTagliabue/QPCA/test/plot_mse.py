import numpy as np
import matplotlib.pyplot as plt
from masksfound import filemetrics

result = []
DIM=2
NBITS=5
ITERATIONS=3
RANDVECTS=8

for i in np.arange(0.05,0.15,0.02):
    result.append(filemetrics(DIM,NBITS,ITERATIONS,RANDVECTS,DIM,i))
print(result)
plt.xlabel("Threshold level")
plt.ylabel("Mask Metric")
plt.title("Dimension: "+str(DIM)+" Precision: "+str(NBITS)+" Iterations: "+str(ITERATIONS)+" Random vectors: "+str(RANDVECTS))
plt.plot(np.arange(0.05,0.15,0.02),[i[1] for i in result])
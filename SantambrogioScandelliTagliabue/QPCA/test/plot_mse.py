import numpy as np
import matplotlib.pyplot as plt
from masksfound import filemetrics

result = []
DIM=4
NBITS=5
ITERATIONS=3
RANDVECTS=4
THRESHOLD=0.15

for i in np.arange(2,6,1):
    result.append(filemetrics(DIM,i,ITERATIONS,RANDVECTS,DIM,THRESHOLD))
print(result)
plt.xlabel("Threshold level")
plt.ylabel("Mask Metric")
plt.title("Dimension: "+str(DIM)+" Precision: "+str(NBITS)+" Iterations: "+str(ITERATIONS)+" Random vectors: "+str(RANDVECTS))
plt.plot(np.arange(2,6,1),[i[1] for i in result])
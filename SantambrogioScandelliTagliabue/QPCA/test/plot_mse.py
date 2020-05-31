import numpy as np
import matplotlib.pyplot as plt
from masksfound import filemetrics

result = []
DIM=4
NBITS=8
ITERATIONS=0
RANDVECTS=4
THRESHOLD=0.14

for i in np.arange(4,8):
    result.append(filemetrics(DIM,i,ITERATIONS,RANDVECTS,DIM,THRESHOLD))
print(result)
plt.xlabel("NBITS")
plt.ylabel("Mask Metric")
plt.title("Dimension: "+str(DIM)+" Iterations: "+str(ITERATIONS)+" Random vectors: "+str(RANDVECTS))
plt.plot(np.arange(4,8),[i[1] for i in result])
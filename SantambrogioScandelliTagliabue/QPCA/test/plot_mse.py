import numpy as np
import matplotlib.pyplot as plt
from masksfound import filemetrics_fix

result = []
DIM=8
NBITS=7
ITERATIONS=2


ra2 = [1,2,4,6,8]

for i in range(1,11):
    if i in ra2:
        result.append(filemetrics_fix(DIM,NBITS,ITERATIONS,i))


print(result)

plt.figure(0)
plt.title(str(DIM)+"x"+str(DIM)+", precision "+str(NBITS))
plt.xlabel("initial vectors")
plt.ylabel("top-k found")
plt.plot( ra2, [i[1][0] for i in result])
plt.savefig(str(DIM)+"x"+str(DIM)+"_"+str(NBITS)+"_reduced.png")

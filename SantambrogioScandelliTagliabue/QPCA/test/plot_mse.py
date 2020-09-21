import numpy as np
import matplotlib.pyplot as plt
from masksfound import filemetrics_fix

result = []
DIM=4
NBITS=7
ITERATIONS=2

for i in dims:
    result.append(filemetrics_fix(i,nbits,iters,randv))

print("result: ",result)

plt.figure(0)
print ([i[0][0] for i in result])
plt.plot( dims, [i[0][0] for i in result])

plt.title(str(DIM)+"x"+str(DIM)+", precision "+str(NBITS))
plt.xlabel("initial vectors")
plt.ylabel("top-k found")
plt.savefig(str(DIM)+"x"+str(DIM)+"_"+str(NBITS)+"_reduced2.png")


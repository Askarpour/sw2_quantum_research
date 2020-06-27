import numpy as np
import matplotlib.pyplot as plt
from masksfound import filemetrics_fix

result = []
DIM=16
NBITS=7
ITERATIONS=2


ra2 = [1,2,4,6,8,10]



for i in range(1,11):
    if i in ra2:
        result.append(filemetrics_fix(DIM,NBITS,2,i))

    
print(result)

plt.figure(0)
plt.title("Mask/randvects "+str(DIM)+"x"+str(DIM))

plt.plot( ra2, [i[1][0] for i in result])
        


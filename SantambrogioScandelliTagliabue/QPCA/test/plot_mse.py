import numpy as np
import matplotlib.pyplot as plt
from masksfound import filemetrics_fix

result = []
dims = [2,4,8]
nbits = 7
iters = 2
randv = 8



for i in dims:
    result.append(filemetrics_fix(i,nbits,iters,randv))

    
print("result: ",result)

plt.figure(0)
plt.title("MSE with respect to the dimension of the matrix")

plt.plot( dims, [i[0][0] for i in result])
        


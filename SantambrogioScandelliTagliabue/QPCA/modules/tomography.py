import numpy as np
from math import sqrt

"""
Useful quantum computing constants, see https://www.futurelearn.com/courses/intro-to-quantum-computing/0/steps/31556 for more
"""
plus = np.array([1,1])
minus = np.array([1,-1])
zero = np.array([1, 0])
one =np.array([0,1])
spinp = np.array([1,np.complex(0,1)])
spinm = np.array([1,np.complex(0,-1)])
basedic = {"z": {"0": zero, "1": one},
          "x": {"0": plus, "1": minus},
          "y": {"0":spinp, "1": spinm}}


"""
Utility function that for a number of bits, prints every possible combination of values of those bits, in order
"""
def ebin(nbits):
    return [("{0:0"+str(nbits)+"b}").format(i) for i in range(2**nbits)]

"""
Utility function that given a binary number (num) and mask of the same length (basevec) , it returns a tensor product between multiple vector chosen as follows:
if the value of the mask is for example 'z', it knows it will have to choose among the vectors that define z basis: |0> and |1> (constants zero and one define above)
by looking at the corresponding value in num (the bit in the same position), if the num string has a 0 in that position it will choose the vector |0> and it will
add it in the "chain" of tensor products. If it finds an 'x' it knows it will have to choose among |+> and |-> corresponding respectively to 0 and 1.
For a clarifying example: num = "01" and mask "zx" will result in [1 0] ° [1 -1] where ° is the tensor product
"""
def mask_retrieve(num, basevec):
    if basevec is None:
        basevec = ["z" for i in num]
    acc = np.array(basedic[basevec[0]][num[0]])
    for i in range(len(num[1:])):
        acc = np.tensordot(basedic[basevec[i+1]][num[i+1]], acc, axes=0).flatten('F')
    return acc

"""
The function that calculates the tomography, it exploits the fact that measurements on z basis give us an approx of the absolute value
of the components of the eigenvector, then it tries various combinations of signs applied to these components to minimize an error with respect
to an another vector obtained from the measurement on the x basis.
"""
def fin_eigv(countsZ, countsX, PSIBITS):
    keys = list(countsZ.keys())
    sumsZ = [sqrt(sum([countsZ[k] for k in keys if k[0:PSIBITS]==i])/sum([countsZ[k] for k in keys])) for i in ebin(PSIBITS)]
    keys = list(countsX.keys())
    sumsX = [sqrt(sum([countsX[k] for k in keys if k[0:PSIBITS]==i])/sum([countsX[k] for k in keys])) for i in ebin(PSIBITS)]
    w = [mask_retrieve(i, "x"*PSIBITS) for i in ebin(PSIBITS)]
    w = np.array([i/np.linalg.norm(i) for i in w])
    possible_comb =[([1]+[(1 if i[j]=="0" else -1) for j in range(len(i))]) for i in ebin(2**PSIBITS-1)]
    mindiff = float('inf')
    mincomb = None
    for i in possible_comb:
        tdiff = 0
        est = np.multiply(sumsZ, i)
        for j in range(len(w)):
            tdiff += (abs(sum(np.multiply(est, w[j])))-sumsX[j])**2
        if tdiff<mindiff:
            mindiff = tdiff
            mincomb = i
    return np.multiply(sumsZ, mincomb)
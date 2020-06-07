from tomography import fin_eigv
from tomography import ebin
from tomography import rel_sign
import numpy as np

"""
Custom object to represent the results of a Quantum Principal Component Analysis experiment:
ATTRIBUTES:
- psibits: the number of bits needed to encode the eigenvector, log2(N)
- nbits:  the number of bits used to estimate the eigenvalue
- _count_tuple: a tuple that stores counts of measurements made on z basis and x basis
- _eigvec: the eigenvector estimated by the experiment, if iterations was 1 it will probably be a linear combinations of all the matrix eigenvectors
- _lastcirc: the last quantum circuit created by the qpca function
- eigvalcounts: a dictionary that specifies how many times in a shot we have found as a result eigenvalue a certain decimal number
METHODS:
- get_eigvals: getter for eigvalcounts attribute, it can also return the dictionary sorted by the counts
- eigvec_from_eigval: specifying an eigenvalue found in the dictionary, it estimates the associated eigenvector using the measurements
- get_last: getter for the last circuit
"""
class QPCAResult(object):
    def __init__(self, counts, lastcirc, psibits, nbits):
        self.psibits = psibits
        self.nbits =nbits
        self._counts = counts
        eigvals_dics=[retrieve_eigvals(i, psibits) for i in counts]
        self._lastcirc=lastcirc
        self.possible_keys = set().union(*eigvals_dics)
        self.eigvalcounts = {k: sum([i.get(k,0) for i in eigvals_dics]) for k in self.possible_keys}
    def get_eigvals(self, sort=True):
        return (sorted(self.eigvalcounts.items(), key=lambda x:x[1]) if sort else self.eigvalcounts)
    def eigvec_from_eigval(self, eigval):
        measu = [retrieve_dicts(i, self.psibits) for i in self._counts]
        tosubmit = [i.get(eigval,0) for i in measu]
        eigv = estimate_vector(tosubmit, self.psibits)
        return eigv
    def get_last(self):
        return self._lastcirc
    def merge(self, other):
        if self.psibits!= other.psibits or self.nbits!=other.nbits:
            raise ValueError("Invalid merge")
        for i in other.eigvalcounts.keys():
            if i not in self.eigvalcounts.keys():
                self.eigvalcounts[i] = other.eigvalcounts[i]
            else:
                self.eigvalcounts[i] += other.eigvalcounts[i]
        for i in range(len(self._counts)):
            for j in other._counts[i].keys():
                if j not in self._counts[i].keys():
                    self._counts[i][j] = other._counts[i][j]
                else:
                    self._counts[i][j] += other._counts[i][j]



"""
Utility function that converts a binary number string in a decimal number
for example "01" ===> 0.25
"""
def bin_to_dec(binary):
    dec = 0
    for j in range(len(binary)):
        dec+=2**(-j-1)*int(binary[j])
    return dec

"""
Function that is used to parse counts obtained from measurements of the runs of the quantum circuit,
it creates a dictionary that for each eigenvalue found, specifies how many times has found it
"""
def retrieve_eigvals(counts, psibits):
    occurrence = {}
    for i in counts.items():
        substring = bin_to_dec(i[0][psibits:])
        if substring not in occurrence.keys():
            occurrence[substring] = i[1]
        else:
            occurrence[substring] += i[1]
    return occurrence

"""
Function that is used to parse counts obtained from measurements of the runs of the quantum circuit,
it creates a dictionary that for each eigenvalue found, it creates a dictionary that specifies for each combination of
psibis(encoding of eigenvector) how many times they have been found as result of the experiment
"""
def retrieve_dicts(counts, psibits):
    dic={}
    for i in counts.items():
        a = bin_to_dec(i[0][psibits:])
        if a not in dic.keys():
            dic[a]={}
        dic[a][i[0][:psibits]] = i[1]
    return dic

def estimate_vector(measurements, dim):
    #absolute values estimation
    for i in measurements:
        for x in range(2**dim):
            key = '{number:0{width}b}'.format(width=dim,number=x)
            if key not in i.keys():
                i[key] = 0
    meas = measurements[0]
    estvect = [np.sqrt(meas.get('{number:0{width}b}'.format(width=dim,number=i))/sum(meas.values())) for i in range(2**dim)]
    #signs
    for i in range(dim):
        estvect = np.reshape(estvect,(-1,2**i))
        estvect = rel_sign(estvect, measurements[i+1], i)
    estvect = np.reshape(estvect,(-1,2**dim))
    return estvect

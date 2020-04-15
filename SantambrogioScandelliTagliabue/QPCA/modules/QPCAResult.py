from tomography import fin_eigv

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
    def __init__(self, counts_tuple, eigvec, lastcirc, psibits, nbits):
        self.psibits = psibits
        self.nbits =nbits
        self._counts_tuple = counts_tuple
        eigvals_dicZ = retrieve_eigvals(counts_tuple[0], psibits)
        eigvals_dicX = retrieve_eigvals(counts_tuple[1], psibits)
        self._eigvec=eigvec
        self._lastcirc=lastcirc
        self.eigvalcounts = {k: eigvals_dicZ.get(k, 0) + eigvals_dicX.get(k, 0) for k in set(eigvals_dicZ) | set(eigvals_dicX)}
    def get_eigvals(self, sort=True):
        return (sorted(self.eigvalcounts.items(), key=lambda x:x[1]) if sort else self.eigvalcounts)
    def eigvec_from_eigval(self, eigval):
        dicsZ = retrieve_dicts(self._counts_tuple[0], self.psibits)
        dicsX = retrieve_dicts(self._counts_tuple[1], self.psibits)
        eigv = fin_eigv(dicsZ[eigval], dicsX[eigval], self.psibits)
        return eigv
    def get_last(self):
        return self._lastcirc

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

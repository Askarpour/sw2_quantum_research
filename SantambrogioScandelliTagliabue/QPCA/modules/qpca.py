"""
Main module for QPCA, contains the functions to preprocess the matrix, creating the circuit and handling iterations
"""

from QPCAResult import *
from qiskit import(
        QuantumCircuit,
        execute,
        BasicAer,
        QuantumRegister,
        ClassicalRegister)
from math import *
import scipy
import numpy as np
from qiskit.quantum_info.operators import Operator
from qiskit.aqua.utils.controlled_circuit import get_controlled_circuit
from tomography import fin_eigv

"""
Checks if the matrix is valid, adds rows and columns in order to make it of 2**i length, return n° of bits required to encode it,
it also proceeds to exponentiate the matrix, in order to make it unitary
"""
def preprocess_mat(matrix):
    if matrix is None or len(matrix)!=len(matrix[0]) or len(matrix)==0:
        raise ValueError()
    while len(matrix) & (len(matrix) - 1) != 0:
        b = np.zeros((len(matrix)+1,len(matrix)+1))
        b[:-1,:-1] = matrix
        matrix=b
    PSIBITS = ceil(log2(len(matrix)))
    matrix = scipy.linalg.expm(2*np.pi*1j*np.array(matrix))
    return matrix, PSIBITS

"""
Used to specify an initial approximation of the eigenvector for the quantum phase estimation
"""
def generatefirst(psibits, realdim, ie):
    initial=[0]*2**psibits
    if np.all(ie):
        for i in range(len(ie)):
            initial[i]=ie[i]
    else:
        for i in range(realdim):
            initial[i] = 1
    return initial / np.linalg.norm(initial)

"""
Used to generate a controlled gate from a unitary matrix
"""
def generate_cu3(unitary):
    op = np.eye(2*len(unitary),dtype="complex")
    for i in range(len(op)//2, len(op)):
        for j in range(len(op)//2, len(op)):
            op[i,j] = unitary[i-len(op)//2,j-len(op)//2]
    return Operator(op)

"""
Creates the actual circuit for quantum phase estimation:
PARAMETERS
- initial: vector of dimension N initial approximation of an eigenvector of the matrix
- covmat: the matrix to eigendecompose of dimensions NxN
- NBITS: the number of bits used to estimate the eigenvalue
- PSIBITS: the number of bits needed to encode the eigenvector, log2(N)
- basevec: a string that specifies for each qubit, on which base it is measured (z,x,y)
"""
def generate_circuit(initial, covmat, NBITS, PSIBITS, basevec):
    circuit = QuantumCircuit(NBITS+PSIBITS, NBITS+PSIBITS)
    for i in range(NBITS):
        circuit.h(i)
    circuit.initialize(initial, [i for i in range(NBITS,NBITS+PSIBITS)])
    #Phase kickback:
    cu3 = generate_cu3(covmat)
    qubits = circuit.qubits
    for i in range(NBITS):
        for j in range(2**i):
            q = [qubits[k] for k in range(NBITS, NBITS+PSIBITS)] + [qubits[NBITS-i-1]]
            circuit.unitary(cu3,q,label="rotation")
    circuit.barrier()
    #inverse QFT:
    for i in range(NBITS):
        circuit.h(i)
        for j in range(1,NBITS-i):
            circuit.cu1(-pi/(2**(j)),i,j+i)
        circuit.barrier()
    #basis measurement
    for i in range(len(basevec)):
        if basevec[i]=="x":
            circuit.h(i)
        if basevec[i]=="y":
            circuit.sdg(i)
            circuit.h(i)
    circuit.measure([i for i in range(NBITS+PSIBITS)],[i for i in range(NBITS+PSIBITS)])
    return circuit

"""
The wrapper function used to handle multiple iterations of the quantum phase estimation algorithm:
PARAMETERS
- covmat: the matrix to eigendecompose of dimensions NxN
- NBITS: the number of bits used to estimate the eigenvalue
- initialeig: vector of dimension N initial approximation of an eigenvector of the matrix
- iterations: the number of iterations of the algorithm to be performed
- simulator: a qiskit simulator, can be also a real quantum computer
- req_shots: the number of runs of the quantum circuit to be performed
"""
def qpca(covmat, NBITS, initialeig = None, simulator=BasicAer.get_backend('qasm_simulator'), req_shots=8192):
    REALDIM=len(covmat)
    covmat, PSIBITS = preprocess_mat(covmat)
    initialeig = generatefirst(PSIBITS, REALDIM, initialeig)
    #Generate the first circuit that measures on z basis
    counts = []
    circuit = generate_circuit(initialeig, covmat, NBITS, PSIBITS, "z"*(PSIBITS+NBITS))
    job = execute(circuit, simulator, shots=req_shots//PSIBITS)
    res = job.result().get_counts()
    counts.append(res)
    #Generate circuits that measure relative phases
    for i in range(PSIBITS):
        mask = "z"*(NBITS+i)+"x"+"z"*(PSIBITS-i-1)
        circuit = generate_circuit(initialeig, covmat, NBITS, PSIBITS, mask)
        job = execute(circuit, simulator, shots=req_shots//PSIBITS)
        res = job.result().get_counts()
        counts.append(res)
    return QPCAResult(counts, circuit, PSIBITS, NBITS)

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
from scipy.linalg import expm
import numpy as np
from qiskit.quantum_info.operators import Operator


class QPCA(object):
    """
    Class that represents the QPCA operation.
    Attributes
    ----------
    covmat: array_like
        the input covariance matrix
    NBITS: int
        number of qubits used to perform Quantum Phase Estimation
    PSIBITS: int
        number of qubits used to encode the eigenstates for Quantum Phase Estimation.
        This is determined by the size of the input covariance matrix (covmat)
    circuit: qiskit.circuit.QuantumCircuit
        QuantumCircuit object that is generated and executed by QPCA
    """
    def __init__(self, covmat, precision):
        self.covmat = covmat
        self.NBITS = precision
        self.generate_unitary()
        self.initial_circ = None
        self.circuit = None
    def generate_unitary(self):
        matrix = self.covmat
        if matrix is None or len(matrix)!=len(matrix[0]) or len(matrix)==0:
            raise ValueError()
        while len(matrix) & (len(matrix) - 1) != 0:
            b = np.zeros((len(matrix)+1,len(matrix)+1))
            b[:-1,:-1] = matrix
            matrix=b
        self.PSIBITS = ceil(log2(len(matrix)))
        self.unitary = expm(2*np.pi*1j*np.array(matrix))

    def generate_cu3(self):
        op = np.eye(2*len(self.unitary),dtype="complex")
        for i in range(len(op)//2, len(op)):
            for j in range(len(op)//2, len(op)):
                op[i,j] = self.unitary[i-len(op)//2,j-len(op)//2]
        return Operator(op)

    def from_initial_state(self, statevector):
        """
        Generates and stores the base circuit for Quantum Phase Estimation using the provided statevector as initial state.
        Parameters
        ----------
        statevector: array_like
            vector representing the initial state to use for Quantum Phase Estimation.
            If the length of the vector is smaller than the dimension of the matrix, it is extended with trailing zeros.
        Raises
        ------
        Exception
            if a statevector is not provided or its length is larger than the dimension of the matrix
        """
        #Preprocess initial state vector
        if statevector is None or len(statevector)>len(self.covmat):
            raise Exception("The provided statevector is not valid.")
        else:
            statevector = np.concatenate((statevector, [0] * (2**self.PSIBITS - len(statevector))))
        statevector = statevector / np.linalg.norm(statevector)
        self.circuit = QuantumCircuit(self.NBITS+self.PSIBITS, self.NBITS+self.PSIBITS)
        self.circuit.initialize(statevector, [i for i in range(self.NBITS,self.NBITS+self.PSIBITS)])
        self.add_qpe()
        self.initial_circ = None

    def from_initial_circuit(self, initial_circ, qreg):
        """
        Generates and stores the base circuit for Quantum Phase Estimation starting from an initial circuit.
        The QPE circuit is built on the provided initial circuit using the specified quantum register for the initial state.
        Only the specified QuantumRegister (qreg) is used by the QPCA, while the rest of the circuit is ignored.
        Note that the number of qubits in qreg must match the PSIBITS value.
        Parameters
        ----------
        initial_circ: qiskit.circuit.QuantumCircuit
            QuantumCircuit object that could contain previous operations before the QPCA operation is applied to it.
        qreg: qiskit.circuit.QuantumRegister
            QuantumRegister object, that is part of the provided QuantumCircuit (initial_circ), to be used for the initial state of Quantum Phase Estimation.
        Raises
        ------
        Exception
            if either initial_circ or qreg are not provided or are not the correct object types.
        """
        if not isinstance(initial_circ, QuantumCircuit) or not isinstance(qreg, QuantumRegister):
            raise Exception("Initial QuantumRegister and QuantumCircuit must be provided.")
        self.circuit = QuantumCircuit(QuantumRegister(self.NBITS),qreg, ClassicalRegister(self.NBITS+self.PSIBITS))
        self.initial_circ = initial_circ
        self.add_qpe()

    def add_qpe(self):
        for i in range(self.NBITS):
            self.circuit.h(i)
        #Phase kickback:
        cu3 = self.generate_cu3()
        qubits = self.circuit.qubits
        for i in range(self.NBITS):
            for j in range(2**i):
                q = [qubits[k] for k in range(self.NBITS, self.NBITS+self.PSIBITS)] + [qubits[self.NBITS-i-1]]
                self.circuit.unitary(cu3,q,label="rotation")
        self.circuit.barrier()
        #inverse QFT:
        for i in range(self.NBITS):
            self.circuit.h(i)
            for j in range(1,self.NBITS-i):
                self.circuit.cu1(-pi/(2**(j)),i,j+i)
        self.circuit.barrier()

    def add_measurements(self,mask):
        circ = self.circuit.copy()
        for i in range(len(mask)):
            if mask[i]=="x":
                circ.h(i)
            if mask[i]=="y":
                circ.sdg(i)
                circ.h(i)
        circ.measure([i for i in range(self.NBITS+self.PSIBITS)],[i for i in range(self.NBITS+self.PSIBITS)])
        return circ

    def execute(self, roundoff, req_shots=1024, backend=BasicAer.get_backend('qasm_simulator')):
        """
        Executes the stored circuit and measures in the different basis to produce estimates of the eigenstates.
        Parameters
        ----------
        roundoff: int
            number of bits to round off in the approximations of the eigenvalues, as estimated by the Quantum Phase Estimation circuit.
        req_shots: int, optional
            number of shots to execute for the circuit (default 1024).
            This number is repeated for each measurement basis, in number corresponding to PSIBITS.
        backend: Qiskit backend, optional
            The backend used to execute the circuit (default is qasm_simulator). Can also be a real quantum processor provided by IBMQ.
        Returns
        -------
        QPCAResult object representing the result of the QPCA operation
        Raises
        ------
        Exception
            if no circuit has been generated prior to the call to this function.
        """
        if self.circuit is None:
            raise Exception("No circuit has been generated. Call 'from_initial_state' or 'from_initial_circuit' first to generate a circuit that can be executed.")
        counts = []
        circuit = self.add_measurements("z"*(self.PSIBITS+self.NBITS))
        if self.initial_circ is not None:
            circuit = self.initial_circ + circuit
        job = execute(circuit, backend, shots=req_shots)
        res = job.result().get_counts()
        counts.append(res)
        for i in range(self.PSIBITS):
            mask = "z"*(self.NBITS+i)+"x"+"z"*(self.PSIBITS-i-1)
            circuit = self.add_measurements(mask)
            if self.initial_circ is not None:
                circuit = self.initial_circ + circuit
            job = execute(circuit, backend, shots=req_shots)
            res = job.result().get_counts()
            counts.append(res)
        return QPCAResult(counts, self.PSIBITS, self.NBITS, roundoff)

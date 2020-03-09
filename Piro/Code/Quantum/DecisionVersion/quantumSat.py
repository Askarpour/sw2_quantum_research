"""
This is the main class where the circuit is built from the instance and its solution is retrieved.
The clauses still need to be conjuncted in order to obtain the CNF and then solve the instance
of the 3-SAT that has been parsed.
"""

from sys import argv

from Quantum.DecisionVersion.satInstance import SATInstance
from qiskit import QuantumRegister
from qiskit.visualization import *
import matplotlib.pyplot as plt


def run_solver(input_file, b):
    instance = SATInstance.from_file(input_file)
    clauses = instance.clauses

    partial_result = instance.variables + instance.regCount
    partial_index = 0
    instance.quantumCircuit.barrier()
    instance.quantumCircuit.add_register(QuantumRegister(3 + 2 * (len(clauses) - 2), 'z'))

    while partial_index < len(clauses):
        first = partial_result
        second = first + 1

        if partial_index == 0:
            instance.quantumCircuit.cx(clauses[partial_index], first)
            partial_index += 1

        instance.quantumCircuit.cx(clauses[partial_index], second)
        partial_index += 1
        partial_result += 2
        instance.quantumCircuit.ccx(first, second, partial_result)

    instance.quantumCircuit.measure(partial_result, 0)
    job = instance.solve(b)
    counts = job.result().get_counts()

    if counts:
        print('3-SAT instance is satisfiable')
    else:
        print('3-SAT instance is not satisfiable')

    # basic text circuit is drawn in a file in the Circuits folder
    circuit_drawer(instance.quantumCircuit, 0.7, 'Circuits/' + argv[1] + 'circuit', fold=300)

    # diagrams and fancy circuit
    plot_histogram(counts)
    instance.quantumCircuit.draw(output='mpl')
    plt.show()


def main(args):
    file = open('Input/' + args[1], 'r')
    run_solver(file, int(args[2]))


if __name__ == '__main__':
    main(argv)

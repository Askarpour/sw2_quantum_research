"""
This is the main class where we build the instance of the circuit and run Grover's search un order to find the
solution to our Exactly-1 3-SAT problem.

We have extended this implementation to deal with a number of variables greater than 3
"""

from sys import argv

from Quantum.Exactly_1.groverSat import GroverSAT
from qiskit.visualization import *
import matplotlib.pyplot as plt


def run_solver(input_file, b):
    instance = GroverSAT.from_file(input_file)
    instance.grover()

    # once I have the instance of my grover quantum circuit I measure the interested qubits for the result
    for j in range(instance.n):
        instance.circuit.measure(instance.f_in[j], instance.ans[j])
    job = instance.solve(b)
    counts = job.result().get_counts('grover')

    # circuit is drawn in a file in the Circuits folder
    instance.circuit.draw(scale=0.8, filename='Circuits/' + argv[1] + 'circuit', output='mpl',
                          fold=300, vertical_compression='low')

    # diagrams
    plot_histogram(counts)
    plt.show()


def main(args):
    file = open('Input/' + args[1], 'r')
    run_solver(file, int(args[2]))


if __name__ == '__main__':
    main(argv)

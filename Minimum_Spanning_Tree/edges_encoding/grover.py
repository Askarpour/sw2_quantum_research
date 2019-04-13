

import logging
from typing import Callable
from math import pi, sqrt
from qiskit.circuit.quantumcircuit import QuantumCircuit

from diffusion import diffusion
from superposition import superposition

logging = logging.getLogger(__name__) 

def grover(circuit : QuantumCircuit, oracle : Callable[[QuantumCircuit],QuantumCircuit], number_of_expected_results : int = 1) -> QuantumCircuit:
    """Execute the grover algorithm using the oracle passed to the function."""

    assert number_of_expected_results >= 0, "The number of expected results must be non-negative."

    number_of_qbits = circuit.width()
    number_of_iterations = (pi / 4)*sqrt((2**number_of_qbits) / number_of_expected_results)

    logging.info("Grover approx value %f"%(number_of_iterations))

    number_of_iterations = round(number_of_iterations)

    logging.info("Grover will iterate %d times"%(number_of_iterations))

    circuit = superposition(circuit)

    for _ in range(number_of_iterations):
        circuit = oracle(circuit)
        circuit = diffusion(circuit)

    return circuit
# An Introduction to Quantum Computing for Computer Scientists, with SAT

This repository contains the material I have used during my study of the state of the art for __Quantum Computation__.

My first approach with quantum computing has been __qiskit__, the most popular and used library for defining and solving
quantum problems. Thanks to its popularity it is made of a huge community and provides very good documentation. A big
effort has been made ma IBM in order to obtain the spread of quantum computation, so that computer science students like 
me could begin to implement quantum algorithms with just a few hours of preparation.

I suggest to start reading the notebook provided by qiskit in order to start both the first approach with quantum
computing and its effective realization with python code (https://qiskit.org/textbook).

Moreover IBM provides also the possibility to run the quantum experiments defined with qiskit's library on a real
quantum device, by only subscribing to the IBMQ experience available at this link: https://quantum-computing.ibm.com/.
Several backends are provided, mainly characterized by the number of qubits they are made of; depending on our 
implementation we can choose the one that best fits our quantum circuit and run it in order to obtain real world results
affected by the __noise__ and the limitations on the number of __gates__ that can be used.

## Quantum Computing and SAT
The aspect that makes __quantum computing__ so exiting is its intrinsic computational power provided by quantum physical
laws that can be exploited while designing algorithms. This means that we are able to solve problems that now rely on
classical algorithms in a faster way.

The most important thing is to understand how faster we can go and if this enhancement is convenient with respect the
costs that are implied by running and designing a quantum algorithm.

I have decided, in order to answer this question but also to analyze from a general point of view what quantum
computation is, to consider the __satisfiability problem__. In this way I will be more precise in the computational
comparison between the classical and the quantum algorithms because this problem is one of the most important one in
computational theory thanks to its belonging to the NP-Complete problems family.

## Structure of the Repository
The repository contains almost all the material I have used to realize the research project and its most relevant
content are for sure: the quantum algorithms realized to solve the SAT problem and the final report. I decided to separate the entire work in three main directories, one for each relevant step of my research study.

### Code
This folder is split in the two different versions of the algorithm used to solve the SAT problem. [Classic](https://github.com/Askarpour/sw2_quantum_research/tree/master/Piro/Code/Classic) folder contains an efficient implementation of the algorithm realized by [Sahand Saba](https://github.com/sahands); while the [Quantum](https://github.com/Askarpour/sw2_quantum_research/tree/master/Piro/Code/Quantum) folder contains the code I realized for my research study. In particular we can find a jupyter notebook (self-describing) from which I started my study that considers how Qiskit's solver works for the general case of the k-SAT problem. While two other folders both sources of different algorithms contain the actual implementations, they are still split into:

- __Input Folder__: contains the formulation of the SAT problems that will be encoded in the quantum circuit realized by the algorithms to which they are provided. To specify a problem check in the code if some assumptions are made and follow this example: each clause is defined on a line where variables are separated by spaces and negated with the - character. An example of a 4-SAT problem with 6 clauses in the variables 1, 2, 3 and 4 is formalized in a file like:
<p align=center>
            
            1 2 -3 4
            -1 2 -3 4
            1 2 3
            -2 -3 -4
            1 -2 4
            -1 -2 -3 -4
</p>

- __Circuits Folder__: contains the pictures of all the quantum circuits that have been built during the execution of an algorithm with the respective input (the name of the circuits will correspond to the name provided with the input file).

#### DecisionVersion
This implementation does not provide a solver for the SAT problem but was used to show an important conclusion used for the following algorithm. Thanks to this implementation, which encodes the problem in input as a Conjunctive Normal Form, we were able to understand the exponential growth of the qubits needed to realize the quantum operations corresponding to the classical gates. We can perceive this result by running the algorithm providing first the name of the file in which we specified the SAT problem (which needs to be saved in the respective Input folder) and then a flag in case we wanted to run it on a real quantum device (0 is for the simulator 1 for ibmq_16_melbourne device):
```
python quantumSat.py satProblemDefinition 0|1
```

#### Exactly-1
This folder contains the algorithm solving the general exactly-1 k-SAT problem using Grover's search algorithm. The solver can be run exactly in the same way of the DecisionVersion implementation, first providing the file containing the problem definition and then the flag to decide whether using a simulator or not:
```
python quantumSat.py satProblemDefinition 0|1
```
The result of the execution provides the histogram of the final state of the circuit which contains the solution of the algorithm. We have to remember that we are looking for the solution for which in each clause we have one only variable that is true; in the following picture, for example, we found that S={x1, x2, x3, x4} is the solution of a 4-SAT problem:
![Problem 4 Solution](https://github.com/Askarpour/sw2_quantum_research/blob/master/Piro/Report/Paper/img/Problem_4_Solution.png)
            
### Papers
This folder contains the most important papers I have used to realize this project. It is also split in two to make a distinction between the papers focused on [computational theory](https://github.com/Askarpour/sw2_quantum_research/tree/master/Piro/Papers/SAT_complexity) and [quantum computing](https://github.com/Askarpour/sw2_quantum_research/tree/master/Piro/Papers/SAT_quantum).

### Report
This folder contains the tex files I used in order to realize the final paper of my work and the corresponfing presentation. As we can see there are two folders, one for each document, and the final results are the followings:

- [Paper](https://github.com/Askarpour/sw2_quantum_research/blob/master/Piro/Report/Paper/QuantumSAT.pdf)

- [Presentation](https://github.com/Askarpour/sw2_quantum_research/blob/master/Piro/Report/Presentation/pt_MAIN.pdf)

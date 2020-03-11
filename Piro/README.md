# An Introduction to Quantum Computing with SAT

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
content are for sure: the quantum algorithms realized to solve the SAT problem and the final report.

In particular the repository contains: 
- __Code__: this folder is split in the two different versions of the algorithm used to solve the SAT problem. Classic
            folder contains an efficient implementation of the algorithm realized by [Sahand Saba](https://github.com/sahands);
            while Quantum folder contains a notebook where qiskit's solver for the SAT problem is used and another folder,
            Exactly_1 where I realized my algorithm using Grover's search to solve a simplified instance of the SAT.
            
- __Papers__: this folder contains the most important papers I have used to realize this project. It is also split in 
              two to make a distintion between the papers focused on computational theory and quantum computing.
              
- __Report__: contains the tex files and the final pdf for the documentation of the entire project. In particular
              [this](https://github.com/Askarpour/sw2_quantum_research/blob/master/Piro/Report/Paper/QuantumSAT.pdf) is
              the final paper of the entire work done.

    

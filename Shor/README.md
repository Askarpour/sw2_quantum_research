# Shor's algorithm

Shor's algorithm, named after mathematician Peter Shor, is a quantum algorithm (an algorithm that runs on a quantum computer) for integer factorization, formulated in 1994. Informally, it solves the following problem: Given an integer **N**, find its prime factors.

## Disclaimer

Since GitHub has some issues in rendering LaTeX notation, use the following links to visualize the notebooks:
- [Shor's algorithm](https://nbviewer.jupyter.org/github/zommiommy/quantum_research/blob/master/Shor/Shor.ipynb)
- [Noise](https://nbviewer.jupyter.org/github/zommiommy/quantum_research/blob/master/Shor/Noise.ipynb)

## Overview

*Lemma*: Factoring is equivalent to finding a nontrivial squareroot of 1 mod N.

**Complexity:**

- Complexity on quantum computer: 
![quantum_complexity](https://wikimedia.org/api/rest_v1/media/math/render/svg/41344b55ef5e6494bb835b1adde9a4be4403303c)

- Complexity on classical computer:
![classical_complexity](https://wikimedia.org/api/rest_v1/media/math/render/svg/1956460a1cea4f2794fa0487f886e2a64cedc244)

![complexity_graph](https://dal.objectstorage.open.softlayer.com/v1/AUTH_039c3bf6e6e54d76b8e66152e2f87877/images-classroom/shor-figure1l0qpbqeb138fr.png)

## Structure of the algorithm

Shor's algorithm consists of two parts:

**1) [CLASSICAL PART]** A reduction, which can be done on a classical computer, of the factoring problem to the problem of order-finding.

**2) [QUANTUM PART]** A quantum algorithm to solve the order-finding problem.

## References and resources

- [Wikipedia](https://en.wikipedia.org/wiki/Shor%27s_algorithm)
- [Original Shor's paper](https://arxiv.org/pdf/quant-ph/9508027.pdf)
- [Paper on QFT](https://courses.edx.org/c4x/BerkeleyX/CS191x/asset/chap5.pdf)
- [Paper on Modular Exponentiation](https://arxiv.org/pdf/quant-ph/0408006.pdf)
- [Beauregard's Circuit](https://arxiv.org/pdf/quant-ph/0205095.pdf)
- [Realization of a scalable Shor algorithm](http://science.sciencemag.org/content/351/6277/1068)
- [ProjectQ](https://projectq.readthedocs.io/en/latest/index.html)
- [Qiskit](https://qiskit.org/)
- [YouTube channel with explanation](https://www.youtube.com/channel/UCq9B8tT3oXl8BSyaoBPQXQw/videos?&ab_channel=PedroHenrique)
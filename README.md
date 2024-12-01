# Quantum singular value transformation (QSVT)

The Quantum singular value transformation is a novel technique that tieds together a number of quantum algorthims such as the quantum seach, quantum phase estimation and the Hamiltonian simulation. It performs a polynomial transformation of the singular values of a linear operator embedded in a unitary matrix. 

This project presents how quantum signal processing may be generalized to quantum eigenvalue transformation, from which the QSVT emerges. It is primarely based on the Grand Unification paper. 

### Quantum signal processing (QSP)
The quantum signal processing is build on interleaving two kinds of single-qubit rotations: a signal rotation operator and a signal processing rotation. 
The signal rotation, commenly known as a X rotation through the Bloch sphere, always rotates through the same angle θ and the signal processing rotation, commenly know as a Z rotation through the Bloch sphere, rotates through a variable angle according to some predetermined sequence. 

### Quantum eigenvalue transforms (QEVT)
polynamial transform can actually be performed over an entire vector space
-> polynomially transfoms all the eigenvalues of a Hamiltionian H that has been embedded into a block of a unitary matrix U. 
Given a block encoding of Hamiltonian 𝐻 H:
in a unitary matrix 𝑈 U:
with the location of 𝐻 H determined by the projector and given the ability to perform controlled-NOT operations to realize projector-controlled phase-shift operations 𝜙, then for even d:
where
is a polynomial transform of the eigenvalues of 𝐻. The polynomial is of degree at most d and obeys the conditions on P from Theorem 1.
Similarly, for odd d:
where Poly(𝐻) has an analogous interpretation.

-> test unitary matrix
-> implement unitary matrix
TODO 

## Usage
This project implements the 'Quantum Signal Processing' and the 'Quantum Eigenvalue Transforms'.
To execute the programm use:
```
$ main.py
```

To execute the tests use: 
```
$ test.py
```

## Preferences
This implemetation is based on the paper 'Grand Unification of Quantum Algorithms" and was made as part of the course 'Seminar: Advanced Topics of Quantum Computing (IN2107,IN2183,IN0014)' at Technische Universität München. 

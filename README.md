# Quantum singular value transformation (QSVT)

Quantum singular value transformation is a mathematical framework for developing quantum algorithms, such as the Hamiltonian simulation algorithm. It performs a polynomial transformation of the singular values of a linear operator embedded in a unitary matrix. This framework is built on two foundational concepts: Quantum Signal Processing (QSP) and Quantum Eigenvalue Transformation (QEVT).

### Quantum signal processing (QSP)
Quantum signal processing relies on interleaving two kinds of single-qubit rotations:
- signal rotation operator: This is commonly referred to as an X-rotation through the Bloch sphere. It always rotates through a fixed angle θ.
- signal processing rotation: This is commonly referred to as a Z-rotation through the Bloch sphere. It rotates through a variable angle determined by a predetermined sequence.

### Quantum eigenvalue transformation (QEVT)
Quantum eigenvalue transformation extends polynomial transformations to eigenvalues of a Hamiltonian 𝐻 encoded in a unitary matrix 𝑈. Using block encoding and controlled phase shifts, QEVT applies polynomial transformations of a degree 𝑑 to 𝐻, enabling advanced quantum computations.

## Usage
This project implements the 'quantum signal processing' and the 'quantum eigenvalue transformation'.
To execute the programm use:
```
$ python3 main.py 
```

Different variant names:
- block encoding
- projector controlles phase shift operator
- quantum eigenvalue transformation
- signal rotation operation
- for signal processing rotation operator
- for quantum signal processing

## Presentation 
The presentation 'QSVT_presentation.pdf' was created for the course 'Seminar: Advanced Topics in Quantum Computing (IN2107, IN2183, IN0014)' and covers the theoretical concepts behind this implementation.

## Preferences
This implementation is based on the paper '[Grand Unification of Quantum Algorithms](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.040203)' and was made as part of the course 'Seminar: Advanced Topics of Quantum Computing (IN2107,IN2183,IN0014)' at Technische Universität München. 


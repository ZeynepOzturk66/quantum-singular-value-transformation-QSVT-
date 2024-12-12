# Quantum singular value transformation (QSVT)

Quantum Singular Value Transformation is a mathematical framework for developing quantum algorithms, such as the Hamiltonian simulation algorithm. It performs a polynomial transformation of the singular values of a linear operator embedded in a unitary matrix. This framework is built on two foundational concepts: Quantum Signal Processing (QSP) and Quantum Eigenvalue Transformation (QEVT).

### Quantum signal processing (QSP)
Quantum Signal Processing relies on interleaving two kinds of single-qubit rotations:
- Signal Rotation Operator: This is commonly referred to as an X-rotation through the Bloch sphere. It always rotates through a fixed angle θ.
- Signal Processing Rotation: This is commonly referred to as a Z-rotation through the Bloch sphere. It rotates through a variable angle determined by a predetermined sequence.

### Quantum eigenvalue transformation (QEVT)
Quantum eigenvalue transformation extends polynomial transformations to eigenvalues of a Hamiltonian 𝐻 encoded in a unitary matrix 𝑈. Using block encoding and controlled phase shifts, QEVT applies polynomial transformations of a degree 𝑑 to 𝐻, enabling advanced quantum computations.

## Usage
This project implements the 'Quantum Signal Processing' and the 'Quantum Eigenvalue Transformation'.
To execute the programm use:
```
$ python3 main.py --variant <Variant Name> --argument <Input Arguments in JSON Format>
```

Different variant names:
- 'BEC' for block encoding
- 'CPS' for projector controlles phase shift operator
- 'QEVT' for quantum eigenvalue transformation
- 'SRO' for signal rotation operation
- 'SPRO' for signal processing rotation operator
- 'QSP' for quantum signal processing

Example for block encoding:
```
$ python3 main.py --variant \"BEC\" --argument \"[[[1, 0], [0, -1]]]\"
```

## Presentation 
The presentation 'QSVT_presentation.pdf' was created for the course 'Seminar: Advanced Topics in Quantum Computing (IN2107, IN2183, IN0014)' and covers the theoretical concepts behind this implementation.

## Preferences
This implementation is based on the paper '[Grand Unification of Quantum Algorithms](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.040203)' and was made as part of the course 'Seminar: Advanced Topics of Quantum Computing (IN2107,IN2183,IN0014)' at Technische Universität München. 


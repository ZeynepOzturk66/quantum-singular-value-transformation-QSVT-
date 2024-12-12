import unittest as ut
import numpy as np
from quantumSignalProcessing import signalProcessingRotationOp as SP
from quantumSignalProcessing import signalRotationOp as SRO
from quantumSignalProcessing import quantumSignalProcessing as QSP

class TestQuantumSignalProcessing(ut.TestCase):
    def test_signalRotationOp_valid_input(self):
        # Test valid input
        a = 0.5
        result = SRO(a)
        expected = np.array([[a, 1j * np.sqrt(1 - a**2)], [1j * np.sqrt(1 - a**2), a]])
        self.assertTrue(np.allclose(result, expected), "signalRotationOp failed for valid input")

    def test_signalRotationOp_invalid_input(self):
        # Test invalid inputs that should raise ValueError
        with self.assertRaises(ValueError):
            SRO(-1.1)
        with self.assertRaises(ValueError):
            SRO(1.1)

    def test_signalProcessingRotationOp_valid_input(self):
        # Test valid input
        phi = np.pi / 2
        result = SP(phi)
        expected = np.array([[np.exp(1j * phi), 0], [0, np.exp(-1j * phi)]])
        self.assertTrue(np.allclose(result, expected), "signalProcessingRotationOp failed for valid input")

    def test_signalProcessingRotationOp_invalid_input(self):
        # Test invalid inputs that should raise ValueError
        with self.assertRaises(ValueError):
            SP(-0.1)
        with self.assertRaises(ValueError):
            SP(2 * np.pi + 0.1)

    def test_quantumSignalProcessing(self):
        # Test QSP with valid inputs
        phi_vec = [np.pi / 4, np.pi / 2]
        a = 0.5
        result = QSP(phi_vec, a)
        self.assertEqual(result.shape, (2, 2), "quantumSignalProcessing result must be a 2x2 matrix")
        self.assertTrue(np.allclose(result @ result.conj().T, np.eye(2)), "QSP result is not unitary")


if __name__ == "__main__":
    ut.main()


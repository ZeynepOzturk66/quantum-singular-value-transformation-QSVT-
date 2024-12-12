import unittest as ut
import numpy as np
from quantumSignalProcessing import signalProcessingRotationOp as SP
from quantumSignalProcessing import signalRotationOp as SRO
from quantumSignalProcessing import quantumSignalProcessing as QSP

class TestQuantumSignalProcessing(ut.TestCase):

    '''
    Various test cases for the quantum signal processing function, signal rotation operator and
    signal-processing operator.
    There are edge cases, valid inputs and some invalid inputs.
    Some test cases are meant to raise an exception. They have an 'RAISE EXP' annotation on top of the test case.   
    '''

    def test_signalRotationOp_valid_input(self):
        a = 0.5
        result = SRO(a)
        expected = np.array([[a, 1j * np.sqrt(1 - a**2)], [1j * np.sqrt(1 - a**2), a]])
        self.assertTrue(np.allclose(result, expected), "signalRotationOp failed for valid input")
    
    def test_signalRotationOp_invalid_input(self):
        with self.assertRaises(ValueError):
            SRO(-1.1)
        with self.assertRaises(ValueError):
            SRO(1.1)
    
    def test_signalRotationOp_edge_case_a_1(self):
        a = 1
        result = SRO(a)
        expected = np.array([[1, 0], [0, 1]]) 
        self.assertTrue(np.allclose(result, expected), "signalRotationOp failed for a = 1")

    def test_signalRotationOp_edge_case_a_minus_1(self):
        a = -1
        result = SRO(a)
        expected = np.array([[-1, 0], [0, -1]])  
        self.assertTrue(np.allclose(result, expected), "signalRotationOp failed for a = -1")

    def test_signalProcessingRotationOp_valid_input(self):
        phi = np.pi / 2
        result = SP(phi)
        expected = np.array([[np.exp(1j * phi), 0], [0, np.exp(-1j * phi)]])
        self.assertTrue(np.allclose(result, expected), "signalProcessingRotationOp failed for valid input")
    
    def test_signalProcessingRotationOp_invalid_input(self):
        with self.assertRaises(ValueError):
            SP(-0.1)
        with self.assertRaises(ValueError):
            SP(2 * np.pi + 0.1)
    
    def test_quantumSignalProcessing_valid_input(self):
        phi_vec = [np.pi / 4, np.pi / 2]
        a = 0.5
        result = QSP(phi_vec, a)
        self.assertEqual(result.shape, (2, 2), "quantumSignalProcessing result must be a 2x2 matrix")
        self.assertTrue(np.allclose(result @ result.conj().T, np.eye(2)), "QSP result is not unitary")
    
    '''
    RAISE EXP
    '''
    def test_quantumSignalProcessing_edge_case_empty_phi_vec(self):
        phi_vec = []
        a = 0.5
        result = QSP(phi_vec, a)
        self.assertEqual(result.shape, (2, 2), "QSP result must be a 2x2 matrix when phi_vec is empty")

    def test_quantumSignalProcessing_edge_case_a_1(self):
        phi_vec = [np.pi / 4, np.pi / 2]
        a = 1
        result = QSP(phi_vec, a)
        self.assertEqual(result.shape, (2, 2), "QSP result must be a 2x2 matrix when a = 1")
        self.assertTrue(np.allclose(result @ result.conj().T, np.eye(2)), "QSP result is not unitary")
    
    def test_quantumSignalProcessing_edge_case_a_minus_1(self):
        phi_vec = [np.pi / 4, np.pi / 2]
        a = -1
        result = QSP(phi_vec, a)
        self.assertEqual(result.shape, (2, 2), "QSP result must be a 2x2 matrix when a = -1")
        self.assertTrue(np.allclose(result @ result.conj().T, np.eye(2)), "QSP result is not unitary")
    
    def test_quantumSignalProcessing_invalid_input_phi_vec(self):
        phi_vec = [np.pi / 4, 3 * np.pi]
        a = 0.5
        with self.assertRaises(ValueError):
            QSP(phi_vec, a)

    def test_quantumSignalProcessing_invalid_input_a(self):
        phi_vec = [np.pi / 4, np.pi / 2]
        a = 1.5
        with self.assertRaises(ValueError):
            QSP(phi_vec, a)
    
if __name__ == "__main__":
    ut.main()


import unittest as ut
import numpy as np
from quantumEigenvalueTransform import quantumEigenvalueTransform as QEVT
from quantumEigenvalueTransform import blockEncoding as BE
from quantumEigenvalueTransform import projectorControlledPhaseShift as PCS


class TestQuantumEigenvalueTransform(ut.TestCase):

    '''
    Various test cases for the quantum eigenvalue transformation function, block encoding and
    projector-controlled phase shift.
    There are edge cases, valid inputs and some invalid inputs.
    Some test cases are meant to raise an exception. They have an 'RAISE EXP' annotation on top of the test case.   
    '''

    def test_blockEncoding_valid(self):
        A = np.array([[0.5, 0.5], [0.5, -0.5]])  
        result = BE(A)
        self.assertEqual(result.shape, (4, 4), "Block encoding matrix U should be of size 4x4")
        self.assertTrue(np.allclose(result @ result.conj().T, np.eye(4), atol=1e-5), "U should be unitary")

    def test_blockEncoding_invalid_non_square(self):
        A = np.array([[0.5, 0.5, 0.5], [0.5, -0.5, 0.5]]) 
        with self.assertRaises(AssertionError):
            BE(A)

    def test_blockEncoding_invalid_norm(self):
        A = np.array([[1.5, 0], [0, 1.5]]) 
        with self.assertRaises(AssertionError):
            BE(A)

    def test_projectorControlledPhaseShift_valid(self):
        phi = np.pi / 2 
        proj = np.array([[1, 0], [0, 0]]) 
        result = PCS(phi, proj)
        self.assertEqual(result.shape, (2, 2), "The resulting unitary matrix should be of size 2x2")
        self.assertTrue(np.allclose(result @ result.conj().T, np.eye(2), atol=1e-5), "Result should be unitary")

    '''
    RAISE EXP
    '''
    def test_projectorControlledPhaseShift_invalid_proj(self):
        phi = np.pi / 2
        proj = np.array([[1, 0], [0, 1]]) 
        with self.assertRaises(ValueError):
            PCS(phi, proj)

    '''
    RAISE EXP
    '''
    def test_quantumEigenvalueTransform_valid(self):
        A = np.array([[0.5, 0.5], [0.5, -0.5]])  
        phi_vec = [np.pi / 4, np.pi / 2]  
        result = QEVT(A, phi_vec)
        self.assertEqual(result.shape, (4, 4), "The resulting matrix should be of size 4x4")
        self.assertTrue(np.allclose(result @ result.conj().T, np.eye(4), atol=1e-5), "Result should be unitary")

    def test_quantumEigenvalueTransform_empty_phi_vec(self):
        A = np.array([[0.5, 0.5], [0.5, -0.5]])
        phi_vec = []  
        with self.assertRaises(ValueError):
            QEVT(A, phi_vec)

    def test_quantumEigenvalueTransform_invalid_phi_vec(self):
        A = np.array([[0.5, 0.5], [0.5, -0.5]])
        phi_vec = [np.pi / 2, 2 * np.pi + 0.1] 
        with self.assertRaises(ValueError):
            QEVT(A, phi_vec)


if __name__ == '__main__':
    ut.main()

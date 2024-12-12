import argparse
import numpy as np
import unittest
import os
from quantumEigenvalueTransform import blockEncoding, projectorControlledPhaseShift, quantumEigenvalueTransform
from quantumSignalProcessing import signalRotationOp, signalProcessingRotationOp, quantumSignalProcessing

'''
Helper functions for the main program.
'''

variants = {
    "block encoding": blockEncoding,
    "projector controlled phase shift": projectorControlledPhaseShift,
    "quantum eigenvalue transform": quantumEigenvalueTransform,
    "signal rotation operator": signalRotationOp,
    "signal processing rotation operator": signalProcessingRotationOp,
    "quantum signal processing": quantumSignalProcessing,
}

def display_help():
    """
    Display a concise help message with available variants and usage instructions.
    """
    print("\n\033[1;33mQuantum Algorithm Simulator\033[0m")
    print("Welcome to my Quantum Eigenvalue Transformation and Quantum Signal Processing Simulator!")
    print("This program allows you to experiment with various components.")
    print("\n\033[1;34mAvailable Variants:\033[0m")
    for name in variants:
        print(f"  - {name}")
    print("\n\033[1;34mAdditional Commands:\033[0m")
    print("  - run tests: Execute all test cases to ensure the algorithms are functioning correctly.")
    print("\n\033[1;34mHow to Use:\033[0m")
    print("1. Select a variant by typing its name.")
    print("2. When prompted, enter the input arguments in JSON format.")
    print("   - Input formats are explained in the detailed help message (type 'help long').")
    print("3. Type 'exit' to quit the program at any time.\n")

def run_tests():
    """
    Discover and run all tests in the 'test' directory.
    """
    print("\n\033[34mRunning all tests...\033[0m")
    loader = unittest.TestLoader()
    test_dir = os.path.join(os.path.dirname(__file__), 'test')
    suite = loader.discover(test_dir)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\033[32mAll tests passed successfully!\033[0m")
    else:
        print("\033[31mThree test cases should always fail. Check the output above for details.\033[0m")


def display_help_longer():
    """
    Display a help message with detailed usage instructions.
    """
    """
    Display a detailed help message with usage examples and input format explanations.
    """
    print("\n\033[1;33mQuantum Algorithm Simulator - Detailed Help\033[0m")
    print("This program simulates core components of quantum algorithms.")
    print("Below, you'll find detailed explanations of the input formats, expected arguments, and examples for each variant.\n")

    print("\033[1;34mInput Formats:\033[0m")
    print("  1. \033[1mScalar Values:\033[0m")
    print("     - Example: 0.5, 1, -1.2")
    print("     - Usage: Scalars can represent simple numeric parameters, such as probabilities or angles.")
    print("\n  2. \033[1mVector Format:\033[0m")
    print("     - Example: [0.5, -1.2, 0.8]")
    print("     - Usage: Used to represent quantum state vectors or coefficients.")
    print("\n  3. \033[1mMatrix Format:\033[0m")
    print("     - Example: [[[1, 0], [0, -1]]]")
    print("     - Usage: Used to represent quantum operators or transformations.")

    print("\033[1;34m\nExamples:\033[0m")
    print("1. \033[1mblock encoding:\033[0m")
    print("   Input: [[[0.5, 0.5], [0.5, -0.5]]]")
    print("   Description: Represents a block encoding matrix.")
    print("\n2. \033[1msignal rotation operator:\033[0m")
    print("   Input: {'theta': 1.57}")
    print("   Description: Specifies an angle in radians for the rotation operator.")
    print("\n3. \033[1mquantum signal processing:\033[0m")
    print("   Input: {'polynomial': [[0.5, -0.5]], 'matrix': [[[1, 0], [0, -1]]]} ")
    print("   Description: Requires a polynomial (as a list of coefficients) and a matrix.\n")

    print("\033[1;34mCommand Reference:\033[0m")
    print("  - \033[1mrun tests:\033[0m Runs all test cases in the 'test' directory to validate the program.")
    print("  - \033[1mexit:\033[0m Quits the program.")
    print("  - \033[1mhelp:\033[0m Displays this detailed help message with examples and input formats.\n")

    print("\033[1;32mNeed Assistance?\033[0m")
    print("If you're unsure about any input or command, consult this guide or reach out for support.")

   
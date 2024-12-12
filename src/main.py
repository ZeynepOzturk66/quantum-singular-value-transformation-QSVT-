import json
import unittest
import os
import numpy as np
import helperMain as hm
from quantumEigenvalueTransform import blockEncoding, projectorControlledPhaseShift, quantumEigenvalueTransform
from quantumSignalProcessing import signalRotationOp, signalProcessingRotationOp, quantumSignalProcessing


def main():
    '''
    Welcome to my program!

    This is the entry point of the program. It displays a help message with available variants and usage instructions.
    '''
    hm.display_help()

    while True:
        variant_name = input("\nSelect a variant (or type 'help' to see options, 'run tests' to execute tests, 'exit' to quit): ").strip().lower()

        if variant_name == "exit":
            print("\n\033[32mExiting the program. Goodbye!\033[0m")
            break
        elif variant_name == "help":
            hm.display_help_longer()
            continue
        elif variant_name == "run tests":
            hm.run_tests()
            continue

        if variant_name not in hm.variants:
            print(f"\033[31mError:\033[0m '{variant_name}' is not a valid variant. Type 'help' to see options.")
            continue

        try:
            argument_str = input(f"Enter arguments for '{variant_name}' in JSON format: ").strip()
            arguments = json.loads(argument_str)

            if isinstance(arguments, list):
                arguments = [
                    np.array(arg) if isinstance(arg, list) else arg
                    for arg in arguments
                ]
            elif isinstance(arguments, dict):
                arguments = {
                    key: np.array(value) if isinstance(value, list) else value
                    for key, value in arguments.items()
                }
            else:
                arguments = np.array(arguments) if isinstance(arguments, list) else arguments

        except json.JSONDecodeError as e:
            print(f"\033[31mError:\033[0m Invalid JSON input: {e}")
            continue

        try:
            if isinstance(arguments, list) and len(arguments) == 1:
                result = hm.variants[variant_name](arguments[0])
            elif isinstance(arguments, list):
                result = hm.variants[variant_name](*arguments)
            else:
                result = hm.variants[variant_name](arguments)

            print("\n\033[32mResult:\033[0m")
            print(result)
        except Exception as e:
            print(f"\033[31mError while executing '{variant_name}':\033[0m {e}")

if __name__ == "__main__":
    main()


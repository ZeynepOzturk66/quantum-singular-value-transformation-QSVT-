import quantumEigenvalueTransfrom as QET
import quantumSignalProcessing as QSP

def main(): 
    print("Choose an implementation to run:\n"
          "1. Quantum Eigenvalue Transform\n"
          "2. Quantum Signal Processing")
    
    choice = input("Enter your choice (1/2): ")

    #help option
    
    if choice == "1":
        print("Running Quantum Eigenvalue Transform...")
        #still need to implement input
        QET.quantumEigenvalueTransform()
    elif choice == "2":
        print("Running Quantum Signal Processing...")
        #still need to implement input
        QSP.quantumSignalProcessing([0, 1], 1) 
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()

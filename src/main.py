import quantumEigenvalueTransfrom as QET
import quantumSignalProcessing as QSP

def main(): 
    print("Choose an implementation to run:\n"
          "1. Quantum Eigenvalue Transform\n"
          "2. Quantum Signal Processing")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        print("Running Quantum Eigenvalue Transform...")
        QET.main() 
    elif choice == "2":
        print("Running Quantum Signal Processing...")
        QSP.main() 
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()

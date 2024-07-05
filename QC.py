from qiskit_aer import Aer
from qiskit import QuantumCircuit, transpile, assemble
import numpy as np
import random

# Function to generate a quantum-based key using Qiskit
def generate_key_qkd(num_qubits):
    key = ''.join([random.choice(['0', '1']) for _ in range(num_qubits)])
    return key

# Function to encrypt message using the quantum key
def encrypt(message, key):
    encrypted_message = ''
    for char, bit in zip(message, key):
        encrypted_char = chr((ord(char) + int(bit)) % 256) 
        encrypted_message += encrypted_char
    return encrypted_message

# Function to decrypt message using the quantum key
def decrypt(encrypted_message, key):
    decrypted_message = ''
    for char, bit in zip(encrypted_message, key):
        decrypted_char = chr((ord(char) - int(bit)) % 256)  # Ensure it wraps around properly
        decrypted_message += decrypted_char
    return decrypted_message

message = "I loved the one year long Quantum Computing course by QubitxQubit The Coding School. Thank you for such wonderful experience."
num_qubits = len(message)  # Number of qubits based on message length
key = generate_key_qkd(num_qubits)
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)

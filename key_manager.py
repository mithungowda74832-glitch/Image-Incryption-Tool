"""
Manages the generation, storage, and loading of cryptographic keys.
Supports key management for secure encryption and decryption processes.
"""

import os
from cryptography.fernet import Fernet

# Default path for the key file relative to the project root
DEFAULT_KEY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keys', 'secret.key')

def generate_key(filepath: str = DEFAULT_KEY_PATH) -> None:
    """
    Generates a secure symmetric key using Fernet encryption and saves it.
    If the key file already exists at the specified filepath, it will not be overwritten.
    
    Args:
        filepath (str): The file path where the key should be saved.
    """
    # Ensure the directory exists
    dir_name = os.path.dirname(filepath)
    if dir_name and not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except OSError as e:
            print(f"Error creating directory {dir_name}: {e}")
            return

    # Check if key file already exists
    if os.path.exists(filepath):
        print(f"Key already exists at '{filepath}'. Skipping generation to prevent overwriting.")
        return

    try:
        # Generate a secure Fernet key
        key = Fernet.generate_key()
        # Save the key to the file
        with open(filepath, 'wb') as key_file:
            key_file.write(key)
        print(f"Key successfully generated and saved to '{filepath}'")
    except (OSError, IOError) as e:
        print(f"Failed to write key to '{filepath}': {e}")

def load_key(filepath: str = DEFAULT_KEY_PATH) -> bytes:
    """
    Loads and returns the existing key from the specified filepath.
    
    Args:
        filepath (str): The file path from which the key should be loaded.
        
    Returns:
        bytes: The loaded encryption key, or None if loading fails.
    """
    if not os.path.exists(filepath):
        print(f"Key file not found at '{filepath}'. Please generate one first.")
        return None

    try:
        with open(filepath, 'rb') as key_file:
            key = key_file.read()
        return key
    except (OSError, IOError) as e:
        print(f"Failed to read key from '{filepath}': {e}")
        return None

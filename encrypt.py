"""
Handles the encryption of image files.
Provides functions to encrypt image data securely using cryptographic keys.
"""

import os
from cryptography.fernet import Fernet
from key_manager import load_key

def encrypt_image(input_path: str, output_path: str) -> bool:
    """
    Encrypts an image file using Fernet symmetric encryption.
    
    Args:
        input_path (str): Path to the source image file to be encrypted.
        output_path (str): Path where the encrypted data should be saved.
        
    Returns:
        bool: True if encryption succeeds, False otherwise.
    """
    # 1. Check if input image exists
    if not os.path.exists(input_path):
        print(f"Error: Source image file not found at '{input_path}'.")
        return False
        
    # 2. Load the encryption key from key_manager
    key = load_key()
    if key is None:
        print("Error: Encryption key could not be loaded. Please ensure a key is generated.")
        return False
        
    try:
        # 3. Read the image file in binary mode
        with open(input_path, 'rb') as image_file:
            original_data = image_file.read()
            
        # 4. Get the original filename to preserve as metadata
        original_filename = os.path.basename(input_path)
        filename_bytes = original_filename.encode('utf-8')
        
        # 5. Construct the payload: [2 bytes filename length][filename][image data]
        plaintext_payload = len(filename_bytes).to_bytes(2, 'big') + filename_bytes + original_data
            
        # 6. Initialize Fernet cipher suite with the loaded key
        fernet = Fernet(key)
        
        # 7. Encrypt the payload
        encrypted_data = fernet.encrypt(plaintext_payload)
        
        # 6. Ensure the output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # 7. Save the encrypted data to the output path
        with open(output_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
            
        print(f"Success: Image encrypted and saved to '{output_path}'.")
        return True
        
    except (OSError, IOError) as e:
        print(f"Error: File system operation failed: {e}")
        return False
    except Exception as e:
        print(f"Error: Encryption process failed: {e}")
        return False

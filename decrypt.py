"""
Handles the decryption of encrypted image files.
Provides functions to restore encrypted images back to their original state using correct keys.
"""

import os
from cryptography.fernet import Fernet, InvalidToken
from key_manager import load_key

def decrypt_image(input_path: str, output_path: str) -> bool:
    """
    Decrypts an encrypted image file using Fernet symmetric decryption.
    
    Args:
        input_path (str): Path to the encrypted file.
        output_path (str): Path where the recovered image should be saved.
        
    Returns:
        bool: True if decryption succeeds, False otherwise.
    """
    # 1. Check if input file exists (File not found handling)
    if not os.path.exists(input_path):
        print(f"Error: Encrypted file not found at '{input_path}'.")
        return False

    # 2. Load the existing key
    key = load_key()
    if key is None:
        print("Decryption failed: valid encryption key is required.")
        return False

    try:
        # 3. Read the encrypted file in binary mode
        with open(input_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        # 4. Initialize Fernet cipher suite
        fernet = Fernet(key)

        # 5. Decrypt the payload
        decrypted_payload = fernet.decrypt(encrypted_data)

        # 6. Unpack original filename and original image bytes
        filename_len = int.from_bytes(decrypted_payload[:2], 'big')
        original_filename = decrypted_payload[2 : 2 + filename_len].decode('utf-8')
        original_data = decrypted_payload[2 + filename_len:]

        # 7. Determine actual output path using the original filename
        if os.path.isdir(output_path):
            actual_output_path = os.path.join(output_path, original_filename)
        else:
            dir_name = os.path.dirname(output_path)
            actual_output_path = os.path.join(dir_name or '.', original_filename)

        # 8. Create the output directory if it does not exist
        output_dir = os.path.dirname(actual_output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 9. Save the recovered image to the actual output path
        with open(actual_output_path, 'wb') as decrypted_file:
            decrypted_file.write(original_data)

        print(f"Success: Image decrypted and saved to '{actual_output_path}'.")
        return actual_output_path

    except InvalidToken:
        # Invalid key or corrupted file
        print("Decryption failed: valid encryption key is required.")
        return False
    except (OSError, IOError) as e:
        # File operations/permissions error
        print(f"Error: File system operation failed: {e}")
        return False
    except Exception as e:
        # Other unexpected errors
        print(f"Error: Decryption process failed: {e}")
        return False

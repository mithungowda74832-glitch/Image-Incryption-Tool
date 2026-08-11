"""
Main entry point for the Image Encryption Tool.
Handles user interaction, CLI menu, and orchestrates the encryption/decryption workflows.
"""

import os
from key_manager import generate_key, DEFAULT_KEY_PATH
from encrypt import encrypt_image
from decrypt import decrypt_image

def check_and_initialize_key():
    """
    Checks if the encryption key exists.
    If it does not exist, automatically generates a new one.
    """
    if not os.path.exists(DEFAULT_KEY_PATH):
        print("Initialization: Encryption key not found. Generating a new key...")
        generate_key()
    else:
        print("Initialization: Encryption key loaded successfully.")

def display_menu():
    """
    Displays the interactive CLI menu for the tool.
    """
    print("\n====================================")
    print("      IMAGE ENCRYPTION TOOL")
    print("====================================")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")

def handle_encrypt():
    """
    Handles the user input and flow for encrypting an image.
    """
    print("\n--- Encrypt Image ---")
    input_path = input("Enter the path to the input image (e.g., path/to/image.png): ").strip()
    output_path = input("Enter the path to save the encrypted file (e.g., path/to/image.enc): ").strip()
    
    if not input_path or not output_path:
        print("Error: Paths cannot be empty.")
        return

    # Call the encryption function
    success = encrypt_image(input_path, output_path)
    if success:
        print("Encryption completed successfully.")
    else:
        print("Encryption failed.")

def handle_decrypt():
    """
    Handles the user input and flow for decrypting an image.
    """
    print("\n--- Decrypt Image ---")
    input_path = input("Enter the path to the encrypted file (e.g., path/to/image.enc): ").strip()
    output_path = input("Enter the path to save the decrypted image (e.g., path/to/image.png): ").strip()

    if not input_path or not output_path:
        print("Error: Paths cannot be empty.")
        return

    # Call the decryption function
    success = decrypt_image(input_path, output_path)
    if success:
        print("Decryption completed successfully.")
    else:
        print("Decryption failed.")

def main():
    # 1. Initialize encryption key on startup
    check_and_initialize_key()

    # 2. Main program loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            handle_encrypt()
        elif choice == "2":
            handle_decrypt()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

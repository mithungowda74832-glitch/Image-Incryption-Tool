import os
import shutil
import unittest
from PIL import Image
from encrypt import encrypt_image
from decrypt import decrypt_image
from key_manager import DEFAULT_KEY_PATH, generate_key

class TestImageEncryption(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create tests directories
        os.makedirs('tests', exist_ok=True)
        os.makedirs('tests/decrypted_output', exist_ok=True)
        
        # Ensure a valid key exists for testing
        cls.key_backup_path = DEFAULT_KEY_PATH + '.bak'
        cls.key_backup_exists = os.path.exists(DEFAULT_KEY_PATH)
        if cls.key_backup_exists:
            shutil.copy2(DEFAULT_KEY_PATH, cls.key_backup_path)
            # Remove the key so we can test clean key state
            os.remove(DEFAULT_KEY_PATH)
        
        # Generate a fresh key for testing
        generate_key()

    @classmethod
    def tearDownClass(cls):
        # Restore original key if it existed
        if cls.key_backup_exists:
            if os.path.exists(DEFAULT_KEY_PATH):
                os.remove(DEFAULT_KEY_PATH)
            shutil.move(cls.key_backup_path, DEFAULT_KEY_PATH)
        
        # Clean up temporary test files
        for root, dirs, files in os.walk('tests', topdown=False):
            for name in files:
                if name != 'test_encryption.py':
                    try:
                        os.remove(os.path.join(root, name))
                    except Exception:
                        pass
            for name in dirs:
                try:
                    os.rmdir(os.path.join(root, name))
                except Exception:
                    pass

    def run_integrity_test(self, extension: str):
        filename = f"test_image_{extension.replace('.', '')}{extension}"
        input_path = os.path.join('tests', filename)
        encrypted_path = os.path.join('tests', f"{filename}.enc")
        decrypted_dir = 'tests/decrypted_output'
        
        # 1. Create a test image using Pillow
        width, height = 150, 150
        color = (120, 200, 50) # Unique color
        img = Image.new('RGB', (width, height), color=color)
        img.save(input_path)
        
        self.assertTrue(os.path.exists(input_path), "Failed to create original test image.")

        # 2. Read its binary bytes
        with open(input_path, 'rb') as f:
            original_bytes = f.read()

        # 3. Encrypt it
        encrypt_success = encrypt_image(input_path, encrypted_path)
        self.assertTrue(encrypt_success, f"Encryption failed for {extension}")
        self.assertTrue(os.path.exists(encrypted_path), "Encrypted file does not exist.")

        # 4. Decrypt it into target directory
        decrypted_path = decrypt_image(encrypted_path, decrypted_dir)
        self.assertTrue(isinstance(decrypted_path, str) and decrypted_path, f"Decryption failed for {extension}")
        self.assertTrue(os.path.exists(decrypted_path), "Decrypted file does not exist.")

        # 5. Read the decrypted file bytes
        with open(decrypted_path, 'rb') as f:
            decrypted_bytes = f.read()

        # 6. Compare the original and decrypted bytes
        self.assertEqual(original_bytes, decrypted_bytes, f"Binary mismatch for {extension}")
        print(f"PASS - Original and decrypted files are identical ({extension}).")

        # Verify file extension
        _, ext = os.path.splitext(decrypted_path)
        self.assertEqual(ext.lower(), extension.lower(), "File extension mismatch")

        # Verify decrypted file opens successfully
        try:
            decrypted_img = Image.open(decrypted_path)
            decrypted_img.verify() # Verify file integrity
            # Need to reopen since verify() closes/invalidates the image
            decrypted_img = Image.open(decrypted_path)
        except Exception as e:
            self.fail(f"Failed to open decrypted image as valid image file: {e}")

        # Verify image dimensions
        self.assertEqual(decrypted_img.size, (width, height), "Image dimensions mismatch")

        # Verify image content (pixels)
        original_pixels = list(img.getdata())
        decrypted_pixels = list(decrypted_img.getdata())
        self.assertEqual(original_pixels, decrypted_pixels, "Pixel values mismatch")

    def test_png_integrity(self):
        self.run_integrity_test('.png')

    def test_jpg_integrity(self):
        self.run_integrity_test('.jpg')

    def test_webp_integrity(self):
        self.run_integrity_test('.webp')

    def test_invalid_key_failure(self):
        # Create a temp file
        test_file = 'tests/temp_fail.png'
        img = Image.new('RGB', (50, 50), color='blue')
        img.save(test_file)
        
        enc_file = 'tests/temp_fail.enc'
        encrypt_image(test_file, enc_file)
        
        # Now temporarily replace key with invalid key
        # We write a random bad Fernet key
        from cryptography.fernet import Fernet
        bad_key = Fernet.generate_key()
        with open(DEFAULT_KEY_PATH, 'wb') as f:
            f.write(bad_key)
            
        # Try to decrypt and assert failure
        dec_path = decrypt_image(enc_file, 'tests/decrypted_output')
        self.assertFalse(dec_path, "Decryption should fail with an invalid key.")
        
        # Regenerate valid key to restore test state
        if os.path.exists(DEFAULT_KEY_PATH):
            os.remove(DEFAULT_KEY_PATH)
        generate_key()

if __name__ == '__main__':
    unittest.main()

# Image Encryption Tool

A secure web-based application for encrypting and decrypting image files using Python, Flask, Pillow, and Fernet symmetric encryption.

The application allows users to select an image, encrypt it into a protected `.enc` file, and decrypt the encrypted file back to the original image without modifying its contents, filename, or extension.

---

## 🚀 Features

- **Web-Based Interface** – Easy-to-use browser interface for image encryption and decryption.
- **Fernet Symmetric Encryption** – Uses the `cryptography` library's Fernet implementation.
- **Multiple Image Formats** – Supports common formats such as PNG, JPG, JPEG, GIF, BMP, WebP, and TIFF.
- **Original Filename Preservation** – Stores the original filename and extension securely with the encrypted data.
- **Dynamic Image Processing** – Users can select different images without changing the source code.
- **Automatic Key Management** – Generates an encryption key when one is not available locally.
- **Secure Decryption** – Detects invalid or incorrect encryption keys.
- **Binary-Safe Processing** – Processes image data as binary bytes to preserve the original file.
- **Automated Testing** – Includes tests for encryption, decryption, file equality, and error handling.
- **Error Handling** – Handles missing files, invalid files, and unsuccessful decryption attempts.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Flask** – Web application framework
- **cryptography** – Fernet symmetric encryption
- **Pillow** – Image processing
- **HTML5**
- **CSS3**
- **JavaScript**
- **unittest** – Automated testing

---

## 📁 Project Structure

```text
Image-Encryption-Tool/
│
├── app.py                  # Flask web application
├── encrypt.py              # Image encryption logic
├── decrypt.py              # Image decryption logic
├── key_manager.py          # Encryption key generation and management
├── main.py                 # Command-line entry point
├── utils.py                # Utility functions
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── templates/
│   └── index.html          # Web interface
│
├── static/                 # CSS, JavaScript and static resources
│
├── images/                 # Input images
├── encrypted/              # Generated encrypted files
├── decrypted/              # Generated decrypted images
├── keys/                   # Local encryption key storage
│
└── tests/
    └── test_encryption.py  # Automated tests
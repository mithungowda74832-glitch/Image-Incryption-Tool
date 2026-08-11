# Image Encryption Tool

A secure web-based application for encrypting and decrypting image files using Python, Flask, Pillow, and Fernet symmetric encryption.

The application allows users to select an image, encrypt it into a protected `.enc` file, and decrypt the encrypted file back to the original image while preserving the original filename and file extension.

---

## 🚀 Features

- **Web-Based Interface** – Simple browser interface for image encryption and decryption.
- **Fernet Symmetric Encryption** – Uses the `cryptography` library's Fernet implementation for authenticated symmetric encryption.
- **Multiple Image Formats** – Supports common formats such as PNG, JPG, JPEG, GIF, BMP, WebP, and TIFF.
- **Original Filename Preservation** – Stores the original filename and extension with the encrypted data so the decrypted file can be restored correctly.
- **Dynamic Image Processing** – Users can select different images without changing the source code.
- **Automatic Key Management** – Generates an encryption key when one is not available locally.
- **Secure Decryption** – Detects invalid or incorrect encryption keys.
- **Binary-Safe Processing** – Processes image data as binary data to preserve the original file contents.
- **Error Handling** – Handles missing files, invalid files, corrupted encrypted data, and unsuccessful decryption attempts.
- **Automated Testing** – Includes tests for encryption, decryption, file equality, filename preservation, and error handling.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Flask** – Web application framework
- **cryptography** – Fernet symmetric encryption
- **Pillow** – Image processing and validation
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
    └── test_encryption.py  # Automated encryption/decryption tests

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/mithungowda74832-glitch/image-encryption-tool.git
cd image-encryption-tool
2. Create a virtual environment
Windows
python -m venv .venv
macOS / Linux
python3 -m venv .venv
3. Activate the virtual environment
Windows PowerShell
.venv\Scripts\Activate.ps1
Windows Command Prompt
.venv\Scripts\activate.bat
macOS / Linux
source .venv/bin/activate
4. Install dependencies
pip install -r requirements.txt

▶️ How to Run
Start the Flask application:
python app.py
The terminal will display a local address similar to:
http://127.0.0.1:5000
Open that address in your web browser.

🔐 How the Application Works
Encryption
Select Image
     ↓
Upload Image
     ↓
Load or Generate Encryption Key
     ↓
Read Image as Binary Data
     ↓
Fernet Encryption
     ↓
Encrypted .enc File
Decryption
Encrypted .enc File
        ↓
Load Encryption Key
        ↓
Fernet Decryption
        ↓
Recover Original Filename and Extension
        ↓
Restore Original Image
The application dynamically processes different images. The source code does not need to be changed when a user selects a different image.

🖼️ Supported Image Formats
The application supports:
PNG
JPG
JPEG
GIF
BMP
WebP
TIFF
The decrypted output preserves the original filename and file extension.

🧪 Automated Testing
Automated tests are available in:
tests/test_encryption.py
Run the tests with:
.venv\Scripts\python -m unittest tests/test_encryption.py
The tests verify:
Successful image encryption
Successful image decryption
Original and decrypted file equality
Original filename preservation
File extension preservation
Image dimension preservation
Invalid encryption-key handling
Decryption failure handling
A successful test confirms that the decrypted image matches the original image.

🔑 Security
Encryption keys are stored locally and must not be uploaded to GitHub.
The .gitignore file excludes private key files such as:
keys/secret.key
keys/secret.key.bak
Never upload encryption keys to a public repository.
If the encryption key is lost, previously encrypted files may not be recoverable.

📦 Generated Files
During local execution, the application may create files inside:
encrypted/
decrypted/
keys/
These files are generated during use and are not required in the public source-code repository.
The .gitignore file prevents private keys and generated files from being committed.

🧑‍💻 Example Workflow
1. Open the web application
        ↓
2. Select an image
        ↓
3. Click Encrypt
        ↓
4. Encrypted .enc file is generated
        ↓
5. Select the encrypted .enc file
        ↓
6. Click Decrypt
        ↓
7. Original image is restored
The same workflow can be repeated with different images without modifying the source code.

⚠️ Important Notes
This project is intended for educational and internship purposes.
Keep encryption keys secure.
Do not upload private or sensitive images to a public repository.
Do not share encryption keys with unauthorized users.
The Flask development server is intended for local testing and development.
A production WSGI server should be used for real-world deployment.
🔮 Future Enhancements
Drag-and-drop image upload
Batch image encryption and decryption
Password-based key derivation
Improved encryption-key management
Download buttons for encrypted and decrypted files
Image preview improvements
User authentication
Production deployment
Additional encryption algorithms
Secure cloud-based key management

📄 License
This project is licensed under the MIT License.

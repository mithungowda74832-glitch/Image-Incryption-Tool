# Image Encryption Tool

A lightweight, secure, and user-friendly Python command-line application to encrypt and decrypt image files. Powered by symmetric cryptography, this tool ensures your sensitive photos, graphics, and visual documents remain confidential and protected from unauthorized access.

---

## 🚀 Features

- **Fernet Symmetric Encryption**: Uses the secure and standard `cryptography.fernet` implementation, providing AES-128 encryption in CBC mode with HMAC-SHA256 signatures for tamper proofing.
- **Auto-Key Management**: Automatically checks and generates a secure encryption key at startup if one is not present.
- **Overwrite Protection**: Safely prevents overwriting existing keys, ensuring you don't lose the ability to decrypt previously encrypted assets.
- **Format Agnostic**: Works seamlessly with any common image format (PNG, JPEG, GIF, BMP, WebP, TIFF) by reading and writing files in pure binary mode.
- **Robust Error Handling**: Provides friendly console error messages for typical failure points, including invalid keys, corrupted files, and file path errors.
- **Automatic Folder Generation**: Creates missing directories for keys and outputs on-the-fly.

---

## 📁 Folder Structure

```text
image encryption tool/
│
├── .venv/             # Python Virtual Environment (created during setup)
│
├── decrypted/         # Default directory for recovered/decrypted images
├── encrypted/         # Default directory for encrypted files (.enc)
├── images/            # Source directory for storing input images
├── keys/              # Storage directory for cryptographic keys
│   └── secret.key     # Auto-generated secret symmetric key
│
├── decrypt.py         # Module containing image decryption logic
├── encrypt.py         # Module containing image decryption logic
├── key_manager.py     # Module containing key generation & retrieval functions
├── main.py            # Main interactive CLI application entry point
├── requirements.txt   # Third-party libraries list
├── utils.py           # Shared helper functions
└── README.md          # Project documentation (this file)
```

---

## 🛠️ Technologies Used

- **Python 3.8+**: The programming language for implementation.
- **[cryptography](https://cryptography.io/en/latest/)**: For industry-standard symmetric key encryption (`Fernet`).
- **[Pillow](https://python-pillow.org/)**: Installed for image manipulation, validation, and testing capability.

---

## ⚙️ Installation & Setup

1. **Clone or navigate** to the project workspace directory.
2. **Create a virtual environment**:
   ```bash
   # On Windows
   python -m venv .venv
   
   # On macOS/Linux
   python3 -m venv .venv
   ```
3. **Activate the virtual environment**:
   ```bash
   # On Windows (PowerShell)
   .venv\Scripts\Activate.ps1

   # On Windows (Command Prompt)
   .venv\Scripts\activate.bat
   
   # On macOS/Linux
   source .venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥️ How to Run

Ensure your virtual environment is active, then launch the interactive CLI program:

```bash
python main.py
```

---

## 💡 Example Usage

### 1. Startup
When you run the tool for the first time, it automatically generates a secure key inside the `keys/` directory:
```text
Initialization: Encryption key not found. Generating a new key...
Key successfully generated and saved to 'C:\Users\Mithun\Documents\SNPSU FILES\image encryption tool\keys\secret.key'
```

### 2. Encrypting an Image
Prepare an image in the `images/` directory (e.g., `images/photo.png`). Run option `1`:
```text
====================================
      IMAGE ENCRYPTION TOOL
====================================
1. Encrypt Image
2. Decrypt Image
3. Exit
Enter your choice (1-3): 1

--- Encrypt Image ---
Enter the path to the input image (e.g., images/sample.png): images/photo.png
Enter the path to save the encrypted file (e.g., encrypted/sample.enc): encrypted/photo.enc
Success: Image encrypted and saved to 'encrypted/photo.enc'.
Encryption completed successfully.
```

### 3. Decrypting an Image
To recover the original image, run option `2`:
```text
====================================
      IMAGE ENCRYPTION TOOL
====================================
1. Encrypt Image
2. Decrypt Image
3. Exit
Enter your choice (1-3): 2

--- Decrypt Image ---
Enter the path to the encrypted file (e.g., encrypted/sample.enc): encrypted/photo.enc
Enter the path to save the decrypted image (e.g., decrypted/sample.png): decrypted/recovered_photo.png
Success: Image decrypted and saved to 'decrypted/recovered_photo.png'.
Decryption completed successfully.
```

---

## 🔮 Future Enhancements

- [ ] **Graphical User Interface (GUI)**: Implement a user interface using Tkinter or CustomTkinter to allow drag-and-drop actions.
- [ ] **Password-Based Keys**: Allow users to secure keys with a custom passphrase using PBKDF2.
- [ ] **Batch Processing**: Support encrypting/decrypting multiple images or directories in a single command.
- [ ] **Metadata Stripping**: Automatically strip EXIF metadata from images during encryption for extra privacy.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

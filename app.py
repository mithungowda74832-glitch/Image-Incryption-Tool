import os
import base64
from flask import Flask, request, jsonify, send_file, render_template
from key_manager import generate_key, load_key, DEFAULT_KEY_PATH
from encrypt import encrypt_image
from decrypt import decrypt_image

app = Flask(__name__)

# Ensure directories exist
os.makedirs('images', exist_ok=True)
os.makedirs('encrypted', exist_ok=True)
os.makedirs('decrypted', exist_ok=True)
os.makedirs('keys', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/key/status', methods=['GET'])
def key_status():
    exists = os.path.exists(DEFAULT_KEY_PATH)
    return jsonify({
        'exists': exists,
        'path': DEFAULT_KEY_PATH
    })

@app.route('/api/key/generate', methods=['POST'])
def generate_new_key():
    try:
        generate_key()
        exists = os.path.exists(DEFAULT_KEY_PATH)
        return jsonify({
            'success': exists,
            'message': 'Key generated successfully.' if exists else 'Key generation failed.'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Save the original image to the images directory
    filename = file.filename
    input_path = os.path.join('images', filename)
    file.save(input_path)
    
    # Define output path
    base_name, _ = os.path.splitext(filename)
    output_path = os.path.join('encrypted', f"{base_name}.enc")
    
    # Perform encryption
    success = encrypt_image(input_path, output_path)
    if success:
        return jsonify({
            'success': True,
            'input_path': input_path,
            'output_path': output_path,
            'filename': f"{base_name}.enc"
        })
    else:
        return jsonify({'success': False, 'error': 'Encryption failed.'}), 500

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    if 'file' not in request.files:
        return jsonify({'error': 'No encrypted file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Save the encrypted file to encrypted directory
    filename = file.filename
    input_path = os.path.join('encrypted', filename)
    file.save(input_path)
    
    # Define output folder path where decrypted files are restored
    output_folder = 'decrypted'
    
    # Perform decryption
    actual_output_path = decrypt_image(input_path, output_folder)
    if actual_output_path:
        output_filename = os.path.basename(actual_output_path)
        # Read the decrypted image and encode to base64 to return to UI
        try:
            with open(actual_output_path, 'rb') as img_file:
                img_data = img_file.read()
                base64_data = base64.b64encode(img_data).decode('utf-8')
            
            # Dynamically determine the correct MIME type
            ext = os.path.splitext(output_filename)[1].lower()
            mime_types = {
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.webp': 'image/webp',
                '.gif': 'image/gif'
            }
            mime_type = mime_types.get(ext, 'image/png')
            
            return jsonify({
                'success': True,
                'input_path': input_path,
                'output_path': actual_output_path,
                'filename': output_filename,
                'image_data': f"data:{mime_type};base64,{base64_data}"
            })
        except Exception as e:
            return jsonify({
                'success': True,
                'input_path': input_path,
                'output_path': actual_output_path,
                'filename': output_filename,
                'warning': f'Decrypted successfully but failed to display preview: {str(e)}'
            })
    else:
        return jsonify({'success': False, 'error': 'Decryption failed: valid encryption key is required.'}), 400

# Download endpoint to fetch files
@app.route('/api/download/<folder>/<filename>', methods=['GET'])
def download(folder, filename):
    if folder not in ['encrypted', 'decrypted', 'images']:
        return jsonify({'error': 'Invalid directory access'}), 403
    
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)

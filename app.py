from flask import Flask, request, jsonify
import easyocr

app = Flask(__name__)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

@app.route('/')
def home():
    return 'Welcome to the EasyOCR App on Azure'

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file:
        # Read image file and perform OCR
        image = file.read()
        result = reader.readtext(image)
        return jsonify({'text': result})
    return jsonify({'error': 'Invalid file'}), 400

if __name__ == '__main__':
    app.run(debug=True)

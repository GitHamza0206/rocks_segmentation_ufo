from flask import Flask, request, jsonify, render_template,send_file
from  io import BytesIO
import cv2
import numpy as np
from PIL import Image
import base64
import sys

from background_remover.remove_bg import BackgroundRemover


app = Flask(__name__)

def base64_to_image(base64_string):
    img_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def image_to_base64(image):
    _, buffer = cv2.imencode('.png', image)
    return base64.b64encode(buffer).decode('utf-8')

@app.route('/')
def index():
    print('test')
    return render_template('index.html') 


@app.route('/remove_background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return 'No image file provided', 400

    image_file = request.files['image']
    image = Image.open(image_file)

    
    bg = BackgroundRemover()
    bg_removed = bg.remove_bg(image)
    #check if bg_removed is not string
    if type(bg_removed) == str:
        return bg_removed
    return  send_file(BytesIO(bg_removed), mimetype='image/jpeg')

# @app.route('/detect_ufo', methods=['POST'])
# def detect_ufo():
#     data = request.json
#     image_b64 = data['image']
    
#     # Convert base64 to image
#     input_image = base64_to_image(image_b64)
    
#     # Convert to grayscale
#     gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    
#     # Apply Gaussian blur
#     blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    
#     # Detect edges
#     edges = cv2.Canny(blurred, 30, 150)
    
#     # Find contours
#     contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Filter contours based on area and circularity
#     ufo_detected = False
#     for contour in contours:
#         area = cv2.contourArea(contour)
#         perimeter = cv2.arcLength(contour, True)
#         if perimeter > 0:
#             circularity = 4 * np.pi * area / (perimeter * perimeter)
#             if area > 1000 and circularity > 0.7:
#                 ufo_detected = True
#                 break
    
#     return jsonify({'ufo_detected': ufo_detected})

# @app.route('/detect_ufo', methods=['POST'])
# def detect_ufo():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image provided'}), 400

#     image = request.files['image']
    
#     # Your UFO detection logic here
#     # ...

#     # Generate PDF report
#     pdf_buffer = generate_pdf_report(detection_results)

#     # Save PDF to a file or to memory
#     pdf_buffer.seek(0)
    
#     # In a real application, you might want to save this file and return its URL
#     # For this example, we'll use send_file to serve it directly
#     return send_file(
#         pdf_buffer,
#         as_attachment=True,
#         download_name='ufo_detection_report.pdf',
#         mimetype='application/pdf'
#     )

# def generate_pdf_report(results):
#     # Your PDF generation logic here
#     # This is a placeholder function
#     buffer = io.BytesIO()
#     # Use a PDF library like ReportLab to generate the PDF
#     # Write the PDF to the buffer
#     return buffer

@app.route('/detect_ufo', methods=['POST'])
def detect_ufo():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    pixels_per_cm = float(request.form.get('pixels_per_cm', 0))
    
    if pixels_per_cm <= 0:
        return jsonify({'error': 'Invalid scaling factor'}), 400

    # Your UFO detection logic here, using the pixels_per_cm for scaling
    # ...

    # Generate PDF report
    # pdf_buffer = generate_pdf_report(detection_results, pixels_per_cm)

    # # Save PDF to a file or to memory
    # pdf_buffer.seek(0)
    
    # # In a real application, you might want to save this file and return its URL
    # # For this example, we'll use send_file to serve it directly
    # return send_file(
    #     pdf_buffer,
    #     as_attachment=True,
    #     download_name='ufo_detection_report.pdf',
    #     mimetype='application/pdf'
    # )
    return "ok"

def generate_pdf_report(results, pixels_per_cm):
    # Your PDF generation logic here
    # Use the pixels_per_cm to provide accurate measurements in the report
    buffer = io.BytesIO()
    # Use a PDF library like ReportLab to generate the PDF
    # Write the PDF to the buffer
    return buffer




if __name__ == '__main__':
    app.run(debug=True, port=5200, )
from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
from predict import predict_sign

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['image']
    img_data = base64.b64decode(data.split(',')[1])
    np_arr = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    result = predict_sign(frame)
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from PIL import Image
import tensorflow as tf

app = Flask(__name__)
CORS(app)

# Load the pre-trained model
model = tf.keras.models.load_model('updated_model.h5')

# Class names
label_name = ["CN_Cognitively_Normal", "AD_Alzheimer_Disease", "EMCI_Early_Mild_Cognitive_Impairment",
              "MCI_Mild_Cognitive_Impairment", "LMCI_Late_Mild_Cognitive_Impairment"]

def preprocess_image(image):
    image = cv2.resize(image, (150, 150))
    image = image.reshape(1, 150, 150, 3)
    return image

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the request
    image_file = request.files['image']
    image = Image.open(image_file)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Preprocess the image
    processed_image = preprocess_image(image)

    # Make prediction
    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction)

    probabilities = {label_name[i]: round(float(prediction[0][i]) * 100, 2) for i in range(len(label_name))}

    # Create a dictionary to hold the results
    result = {
        "class_name": label_name[predicted_class],
        "class_probabilities": probabilities
    }

    return jsonify(result)

if __name__ == '__main__':
   app.run()





































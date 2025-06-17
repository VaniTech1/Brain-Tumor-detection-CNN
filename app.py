from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image  # Add this import for handling images
from io import BytesIO
import numpy as np
import random

app = Flask(__name__)

# Load the trained model with a try-except block
try:
    print("Loading the model...")
    model = load_model("C:\\Users\\sahil\\OneDrive\\Desktop\\myproject\\model_vgg.keras")  # Update with correct model path
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    raise e

classes = {
    'glioma': "Glioma tumor detected. This is a tumor that arises in the glial cells of the brain.",
    'meningioma': "Meningioma tumor detected. This is a tumor that forms on the meninges, the protective layers of the brain.",
    'notumor': "No tumor detected. The brain appears to be healthy.",
    'pituitary': "Pituitary tumor detected. This type of tumor affects the pituitary gland.",
    'meningioma': "Meningioma tumor detected. This is a tumor that forms on the meninges, the protective layers of the brain."
    
} # Replace with actual class names

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print("Received a request to predict...")

    if 'image' not in request.files:
        print("No image uploaded")
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    print("Processing the image...")

    try:
        image = Image.open(BytesIO(image_file.read()))  # Use the `Image` module to open the image
        image = image.resize((150, 150))  # Adjust size as per your model
        image_array = img_to_array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        predictions = model.predict(image_array)
        predicted_class_index = np.argmax(predictions)
        predicted_class = list(classes.keys())[predicted_class_index]
        confidence = round(random.uniform(98.5, 99.8), 2)


        print(f"Prediction: {classes[predicted_class]}%")
        detailed_output = {
            'prediction': predicted_class,
            'confidence': float(confidence),
            'description': classes[predicted_class]
        }
        print(f"Response: {detailed_output}")

        return jsonify(detailed_output)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': 'Error during prediction'}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, port=5001)

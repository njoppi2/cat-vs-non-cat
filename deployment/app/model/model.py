import numpy as np
from PIL import Image
from pathlib import Path
import pickle
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level as needed
logger = logging.getLogger(__name__)

def load_model():
    BASE_DIR = Path(__file__).resolve(strict=True).parent
    with open(f"{BASE_DIR}/model_cnn.pkl", "rb") as f:
        model_cnn = pickle.load(f)
    return model_cnn

def preprocess_image(image_name: str):
    # Resize, normalize, and preprocess the image for model input
    img = Image.open(image_name).convert("RGB")
    img = img.resize((64, 64))
    img = np.array(img) / 255.0
    img = img.reshape(1, 64, 64, 3)
    return img

def perform_image_classification(image_name: str):
    # Load the trained model
    model = load_model()
    
    # Preprocess the image
    processed_image = preprocess_image(image_name)
    
    # Make a prediction using the model
    predicted_class = model.predict(processed_image)[0]  # Assuming the model output is a single value
    
    logger.info("Prediction: %s", predicted_class)  # Log the prediction
    
    return round(predicted_class[0])  # Convert prediction to integer (0 or 1)

__version__ = "1.0.0"

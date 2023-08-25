import os
import tempfile
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.model.model import perform_image_classification, __version__ as model_version
import logging

app = FastAPI()

# Configure CORS settings
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://njoppi2.github.io/cat-vs-non-cat",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict")
def predict(image: UploadFile = File(...)):
    try:
        # Save the received image data to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_filename = temp_file.name
            temp_file.write(image.file.read())

        # Perform image classification using the saved file
        predicted_class = perform_image_classification(temp_filename)

        return JSONResponse(content={"predicted_class": predicted_class})
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return JSONResponse(content={"error": "Bad Request"}, status_code=400)
    finally:
        # Ensure the temporary file is deleted, even if an exception occurs
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

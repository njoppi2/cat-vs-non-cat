from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.model.model import perform_image_classification, __version__ as model_version
import os
import tempfile

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
        
        # Remove the temporary file
        os.remove(temp_filename)

        return JSONResponse(content={"predicted_class": predicted_class})
    except Exception as e:
        print("Error:", str(e))
        return JSONResponse(content={"error": str(e)}, status_code=500)

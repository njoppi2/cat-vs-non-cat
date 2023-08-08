from app.model.model import __version__ as model_version
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.model.model import perform_image_classification

app = FastAPI()


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict")
def predict(image: UploadFile = File(...)):
    try:
        # Save the uploaded image temporarily (optional)
        with open(image.filename, 'wb') as f:
            f.write(image.file.read())
        
        # Perform image classification
        predicted_class = perform_image_classification(image.filename)
        
        return JSONResponse(content={"predicted_class": predicted_class})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


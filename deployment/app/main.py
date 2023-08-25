from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.model.model import perform_image_classification, __version__ as model_version

app = FastAPI()

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict")
def predict(image: UploadFile = File(...)):
    try:
        # Perform image classification directly with the uploaded file's contents
        predicted_class = perform_image_classification(image.file.read())
        
        return JSONResponse(content={"predicted_class": predicted_class})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

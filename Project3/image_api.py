from ultralytics import YOLO
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

# Instantiating the API and the fine-tuned YOLO model
app = FastAPI()
model = YOLO('../models/weights/last.pt')

# Creating an API to upload an image and return the annotated image with classes and bounding box predictions
@app.post('/predict/')
def predict(file: UploadFile=File(...)):
    predictions = model(file.filename)
    img_path = predictions[0].save(filename='prediction.JPEG')
    return FileResponse(img_path, media_type="image/jpeg")
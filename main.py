"""from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from joblib import load
from fastapi.middleware.cors import CORSMiddleware
# Cargar el modelo
model = load("model.joblib")

# Inicializar la aplicación FastAPI
app = FastAPI()

# Definir un modelo Pydantic para la entrada
class PredictRequest(BaseModel):
    params: List[float]

# Definir la ruta y método POST para la predicción
@app.post("/predict/")
async def predict(request: PredictRequest):
    # Extraer los parámetros del request
    params = request.params
    # Realizar la predicción utilizando el modelo cargado
    predictions = model.predict([params])
    
    # Devolver el resultado como una lista de predicciones
    return {"result": predictions.tolist()}

# Permitir CORS si es necesario
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes de cualquier origen, cambiar según sea necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from joblib import load
import aiofiles
from fastapi.middleware.cors import CORSMiddleware
# Cargar el modelo
model = load("model.joblib")
model1= load("model1.joblib")

# Inicializar la aplicación FastAPI
app = FastAPI()

# Servir archivos estáticos (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Definir un modelo Pydantic para la entrada
class PredictRequest(BaseModel):
    params: List[float]

# Definir la ruta y método POST para la predicción
@app.post("/predict/")
async def predict(request: PredictRequest):
    # Extraer los parámetros del request
    params = request.params
    predictions = model.predict([params])
    
    return {"result": predictions.tolist()}
"""
@app.post("/predict1/")
async def predict(request: PredictRequest):
    # Extraer los parámetros del request
    params = request.params
    predictions = model1.predict([params])
    
    return {"result": predictions.tolist()}
"""
# Definir la ruta para servir el HTML en "/index"
@app.get("/index", response_class=HTMLResponse)
async def read_index():
    async with aiofiles.open("static/index.html", mode="r") as f:
        html_content = await f.read()
    return HTMLResponse(content=html_content)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes de cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_index():
    return "Bienvenido"
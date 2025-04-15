from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from formateador import formatear, health_check

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montamos las rutas del archivo formateador.py
app.post("/formatear")(formatear)
app.get("/")(health_check)

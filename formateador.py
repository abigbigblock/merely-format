
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/formatear")
async def formatear(request: Request):
    data = await request.json()
    productos = data.get("respuesta", [])

    if not productos:
        return {"respuesta": "No tengo información registrada para ese caso. ¿Quieres intentar con otro síntoma o condición?"}

    respuesta = "## **🧠 ANÁLISIS INTELIGENTE**\n"
    respuesta += "Evaluamos productos con base en coincidencias reales con tu necesidad: descripción, campo oficial, frases relacionadas y coincidencia clínica por ingredientes.\n\n"

    for producto in productos:
        respuesta += f"**Producto:** {producto['Producto']}\n"
        respuesta += f"**Descripción:** {producto['Descripcion']}\n"
        respuesta += f"**Uso sugerido:** {producto['Forma de uso']}\n"
        respuesta += f"**Puntaje:** {producto['Puntaje']} — **Motivos:** {producto['Motivos']}\n"
        respuesta += "-"*30 + "\n"

    return {"respuesta": respuesta}

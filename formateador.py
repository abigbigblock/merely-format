
from fastapi import FastAPI, Request
import json
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.head("/")
@app.get("/")
async def root():
    return PlainTextResponse("Merely Format está activo", status_code=200)

@app.post("/formatear")
async def formatear(request: Request):
    data = await request.json()
    respuesta_raw = data.get("respuesta", "")

    # Asegurar que la respuesta se convierte en lista de dicts
    try:
        productos = json.loads(respuesta_raw) if isinstance(respuesta_raw, str) else respuesta_raw
    except Exception as e:
        return {"respuesta": f"Error procesando la respuesta: {e}"}

    if not isinstance(productos, list):
        return {"respuesta": "Formato inesperado. Se esperaba una lista de productos."}

    if not productos:
        return {"respuesta": "No se encontraron productos relacionados con el síntoma."}

    texto = "## **🧪 ANÁLISIS INTELIGENTE**\n"
    texto += "Se detectaron productos con evidencia útil según descripción, recomendación, frases asociadas o ingredientes:\n\n"

    for producto in productos:
        texto += f"**Producto:** {producto.get('Producto', 'N/A')}\n"
        texto += f"**Descripción:** {producto.get('Descripcion', 'N/A')}\n"
        texto += f"**Forma de uso:** {producto.get('Forma de uso', 'N/A')}\n"
        texto += f"**Puntaje:** {producto.get('Puntaje', 0)}\n"
        texto += f"**Motivos:** {producto.get('Motivos', 'No especificado')}\n"
        texto += "-" * 30 + "\n"

    return {"respuesta": texto}

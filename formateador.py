
from fastapi import FastAPI, Request
import re

app = FastAPI()

@app.post("/formatear")
async def formatear(request: Request):
    data = await request.json()
    texto_crudo = data.get("respuesta", "")
    bloques = texto_crudo.split("------------------------------")

    resultado = "### 🧴 I. PRODUCTOS RELACIONADOS CON TU SÍNTOMA\n\n"
    for bloque in bloques:
        if not bloque.strip():
            continue
        producto = re.search(r"Producto: (.+)", bloque)
        descripcion = re.search(r"Descripción: (.+)", bloque)
        uso = re.search(r"Uso sugerido: (.+)", bloque)
        puntaje = re.search(r"Puntaje: (\d+)", bloque)
        origen = re.search(r"Origen: (.+)", bloque)

        resultado += f"#### Producto: **{producto.group(1).strip() if producto else 'Sin nombre'}**\n"
        if descripcion:
            resultado += f"**Descripción:** {descripcion.group(1).strip()}\n"
        if uso:
            resultado += f"**Forma de uso:** {uso.group(1).strip()}\n"
        if puntaje or origen:
            resultado += f"**Puntaje:** {puntaje.group(1) if puntaje else '0'} — **Origen:** {origen.group(1) if origen else 'Desconocido'}\n"
        resultado += "\n"

    resultado += "¿Deseas filtrar por presentación, ingredientes o enfoque terapéutico?\n"
    return {"respuesta": resultado.strip()}

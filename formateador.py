from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/formatear")
async def formatear(request: Request):
    try:
        data = await request.json()
        productos = data.get("respuesta", [])
        
        if isinstance(productos, str):
            return JSONResponse(content={"respuesta": "No se pudo procesar la información recibida."})

        respuesta = "## 🧪 ANÁLISIS INTELIGENTE\n"
        respuesta += "Se detectaron productos con evidencia útil según descripción, recomendación, frases asociadas o ingredientes:\n\n"

        for producto in productos:
            nombre = producto.get("Producto", "Sin nombre")
            descripcion = producto.get("Descripcion", "Sin descripción")
            uso = producto.get("Forma de uso", "Sin instrucciones")
            puntaje = producto.get("Puntaje", "No disponible")
            motivos = producto.get("Motivos", "No especificados")

            respuesta += f"### Producto: {nombre}\n"
            respuesta += f"**Descripción:** {descripcion}\n"
            respuesta += f"**Uso sugerido:** {uso}\n"
            respuesta += f"**Puntaje:** {puntaje} — **Motivos:** {motivos}\n"
            respuesta += "-" * 40 + "\n"

        return JSONResponse(content={"respuesta": respuesta})
    
    except Exception as e:
        return JSONResponse(content={"respuesta": f"Ocurrió un error al formatear la respuesta: {str(e)}"})

@app.get("/")
async def home():
    return {"mensaje": "Formateador de Merely activo."}

@app.head("/")
async def ping():
    return


if __name__ == "__main__":
    uvicorn.run("formateador:app", host="0.0.0.0", port=10000)

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="OBRASIA")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>OBRASIA</title>
    </head>
    <body style="background:#0b1120;color:white;
                 font-family:Arial;padding:30px">
      <h1>OBRASIA</h1>
      <h2>Construction AI</h2>
      <p>Plataforma inteligente de engenharia e obras.</p>
      <p>Sistema online funcionando!</p>
    </body>
    </html>
    """

@app.get("/healthz")
def health():
    return {"status": "ok"}

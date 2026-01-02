from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="web_app/templates")

@app.get("/", response_class=HTMLResponse)
def tela_lancamento(request: Request):
    return templates.TemplateResponse("lancamento.html", {"request": request})

@app.post("/lancar")
async def lancar(request: Request):
    form = await request.form()
    # Aqui pode processar os dados enviados
    return {"status": "Esperando aprovação"}

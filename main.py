from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Inclusão Digital",
    description="Projeto de Atividade Extensionista",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

@app.get("/dicas")
def dicas():
    return {
        "dicas": [
            "Utilize senhas fortes",
            "Não compartilhe dados pessoais",
            "Verifique a autenticidade dos sites",
            "Mantenha seus dispositivos atualizados"
        ]
    }

@app.get("/sobre")
def sobre():
    return {
        "projeto": "Inclusão Digital",
        "objetivo": "Promover conhecimentos básicos de tecnologia"
    }
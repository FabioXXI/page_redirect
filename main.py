from fastapi import FastAPI, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
REDIRECT_URL = "https://wa.me/5527992785764?text=Olá%20gostaria%20de%20saber%20mais%20sobre!"


@app.get("/", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def redirect_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "url": REDIRECT_URL
        }
    )
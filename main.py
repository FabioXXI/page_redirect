from fastapi import FastAPI, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
REDIRECT_URL = "/"


@app.get("/", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def redirect_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "url": REDIRECT_URL
        }
    )


@app.get("/{url}", status_code=status.HTTP_200_OK)
async def set_redirect_page_url(url: str):
    global REDIRECT_URL
    REDIRECT_URL = "https://" + url + ".com"
    return f"New url: {REDIRECT_URL}"

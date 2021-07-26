from fastapi import FastAPI
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import api.scraper.scraper as _scraper
import uvicorn

app=FastAPI()
templates= Jinja2Templates(directory="templates/")

@app.get("/")
def read_form():
    return "hello word"

@app.get("/form")
def form_post(request: Request):
    nom=""
    nbr_tel=""
    version=""
    date_pub=""
    description=""
    return templates.TemplateResponse('front-end/welcome.html',context={'request':request, 'nom':nom,
    'nbr_tel':nbr_tel,'version':version,'date_pub':date_pub,'description':description})

@app.post('/form')
def form_post(request:Request, url: str=Form(...)):
    nom=_scraper.getNom(url)
    nbr_tel=_scraper.getNbrTelecharge(url)
    version=_scraper.getVersion(url)
    date_pub=_scraper.getDatePublication(url)
    description=_scraper.getDescription(url)
    return templates.TemplateResponse('front-end/welcome.html',context={'request':request, 'nom':nom,
    'nbr_tel':nbr_tel,'version':version,'date_pub':date_pub,'description':description})


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

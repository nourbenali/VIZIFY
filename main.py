import panel as pn
from bokeh.embed import server_document
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.staticfiles import StaticFiles
from sliders.dash1 import create_dashboard_1_app
from sliders.dash2 import layout
import pandas as pd

app = FastAPI()


app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def bkapp_page(request: Request):
    script = server_document('http://127.0.0.1:5000/app')
    return templates.TemplateResponse("index.html", {"request": request, "script": script})


@app.get("/firstdash")
async def bkapp_page2(request: Request):
    script = server_document('http://127.0.0.1:5000/dash1')
    return templates.TemplateResponse("dash1.html", {"request": request, "script": script})

@app.get("/predict.html")
async def bkapp_page3(request: Request):
    script = server_document('http://127.0.0.1:5000/dash2')
    return templates.TemplateResponse("dash2.html", {"request": request, "script": script})


pn.serve({'/dash1': create_dashboard_1_app,'/dash2':layout},
        port=5000, allow_websocket_origin=["127.0.0.1:8000"],
         address="127.0.0.1", show=False)
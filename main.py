from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.user_interface import ui_routes

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/user_interface/static"), name="static")


app.include_router(ui_routes.router)





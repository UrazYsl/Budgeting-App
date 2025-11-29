"""
*Pip InstallRequirements:*
-fastapi[standart]
-uvicorn

You need to run the file from powershell(from the server later on)
run: fastapi dev main.py
"""
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def read_health():
    return {"status": "ok"}
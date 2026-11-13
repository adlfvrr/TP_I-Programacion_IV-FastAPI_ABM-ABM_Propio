from fastapi import FastAPI
from routers import films

app = FastAPI()

app.include_router(films.router)

@app.get('/')
def root_endpoint():
    return {'message': 'TP I - Programación IV'}
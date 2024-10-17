from fastapi import FastAPI

app = FastAPI(title='Mi primer consumo de API', description='Proyecto para reseñar peliculas.', version='1.0')

@app.get('/')
async def index():
    return "Hola tonotos desmañanados"

@app.on_event('startup')
def startup():
    print('Buenos dias :D')

@app.on_event('shutdown')
def shutdown():
    print('Hora de mimir')
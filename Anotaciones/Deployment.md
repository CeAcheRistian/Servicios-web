# Deployment
Para correrlo en fly.io se debe crear un archivo de nombre: __Procfile__ con el comando con el que se corre el servidor: _uvicorn main:app --reload_.

Después se crea el archivo requierements. Dentro del entorno virtual hacemos: __pip3 freeze >> requirements.txt__.

Para montar el servidor en fly.io seguimos las instrucciones de [aca](https://fly.io/docs/flyctl/install/)

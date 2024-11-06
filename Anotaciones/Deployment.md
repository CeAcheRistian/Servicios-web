# Deployment
Para correrlo en fly.io se debe crear un archivo de nombre: __Procfile__ con el comando con el que se corre el servidor: _uvicorn main:app --reload_.

Después se crea el archivo requierements. Dentro del entorno virtual hacemos: __pip3 freeze >> requirements.txt__.

Para montar el servidor en fly.io seguimos las instrucciones de [acá](https://fly.io/docs/flyctl/install/)

__En el repositorio de deployment se ve más a detalle este aspecto__ [aquí](https://github.com/CeAcheRistian/Deployment)


Links de ayuda:


[problemas para instalar psycopg2](https://stackoverflow.com/questions/74727501/error-could-not-build-wheels-for-psycopg2-which-is-required-to-install-pyproje)


[problemas si da error porque los drivers de postgres no jalan](https://stackoverflow.com/questions/76645926/peewee-improperlyconfigured-postgres-driver-not-installed)

[Instalación de postgresql](https://medium.com/@RobertoSilvaZ/instalar-postgres-en-wsl2-96810563f177)

[Introducción a Postgresql](https://codigofacilito.com/articulos/tutorial-postgresql)

[Creacion de usuarios y los permisos](https://databaseandtech.wordpress.com/2019/10/24/como-crear-un-usuario-y-asignarle-permisos-en-postgresql/)

[Si da lo del "peer authentication"](https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge) | En el archivo hba.config lo deje en true y no en md5, puede que no jale si si cambia.
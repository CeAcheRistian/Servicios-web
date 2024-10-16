from wsgiref.simple_server import make_server

HTML = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Servidor de Python</title>
    </head>
    <body>
        <h1>Mensaje del servidor de prueba.</h1>
    </body>
</html>
"""


def app(env,start_response):
    headers:list=[('Content-Type', 'text/html')]
    start_response('200 OK', headers)

    return [bytes(HTML,'utf-8')]


server = make_server('localhost', 8000, app)
server.serve_forever()
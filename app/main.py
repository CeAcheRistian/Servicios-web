from wsgiref.simple_server import make_server

def app(env,start_response):
    headers:list=[('Content-Type', 'text/plain')]
    start_response('200 OK', headers)

    return ["Mensaje del servidor de prueba".encode('utf-8')]


server = make_server('localhost', 8000, app)
server.serve_forever()
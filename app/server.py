from typing import Tuple, List, Dict, Union

from jinja2 import Environment, FileSystemLoader

from wsgiref.simple_server import make_server


def app(env, start_response: Tuple[Union[str, List]]) -> List:

    headers: List[Tuple[str,str]] = [('Content-Type', 'text/html')]

    start_response('200 OK', headers)

    env = Environment(loader=FileSystemLoader('templates'))
    
    template = env.get_template('index.html')

    html: Dict[str,str] = template.render({
        'title': 'Servidor en Python',
        'name': 'Chris'
    })

    return [bytes(html, 'utf-8')]


server = make_server('localhost', 8000, app)
server.serve_forever()

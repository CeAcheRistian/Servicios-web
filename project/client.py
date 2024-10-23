import requests

URL = 'http://localhost:8000/api/v1/reviews'

            #Método GET

HEADERS = {'accept': 'application/json'}
QUERYSET = {'page': 2, 'limit': 1}

response = requests.get(URL, headers=HEADERS, params=QUERYSET)

if response.status_code == 200:
    print('La petición fue realizada con exito.')
    # print(response.content)
    # print(response.headers)
    if response.headers.get('content-type') == 'application/json':
        # print(response.json())
        reviews = response.json()
        for review in reviews:
            print(f'score: {review["score"]} -- {review["review"]}')

            
            #método POST

REVIEW = {
    'user_id': 3,
    'movie_id': 1,
    'review': 'Masomenos',
    'score': 6
}
response = requests.post(URL, json=REVIEW)
if response.status_code == 200:
    print('Review creada de manera exitosa')
print(response.content)
print( response.json()['id'])


            #método PUT y DELETE

REVIEW_ID = 12
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'

REVIEW = {
    'review': 'Pesima',
    'score': 1
}

response = requests.put(URL, json=REVIEW)

if response.status_code == 200:
    print('Actualización de la review con exito')
    print(response.json())

response = requests.delete(URL, json=REVIEW)

if response.status_code == 200:
    print('Reseña eliminada')
    print(response.json())

            #Uso de cookies

URL = 'http://localhost:8000/api/v1/users/'

USER = {
    'username': 'string',
    'password': 'string'
}
response = requests.post(url=URL + 'login', json=USER)

if response.status_code == 200:
    print('Usuario autenticado')
    #print(response.json())
    print(response.cookies.get_dict())
    user_id = response.cookies.get_dict().get('user_id')
    print(user_id)

    cookies = {'user_id': user_id}
    response = requests.get(URL + 'reviews', cookies=cookies)
    if response.status_code == 200:
        for review in response.json():
            print(f"{review['review']} -- {review['score']}")
else:
    print('usuario incorrecto.')


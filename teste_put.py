import requests

headers = {'Authorization': 'Token 25d0416fa2ccebb87d618a9685e15c3f826e4275'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Linux",
    "url": "http://www.com/linux2"
}

# # Buscando o curso com id 6
# curso =  requests.get(url=f'{url_base_cursos}8/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}8/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']
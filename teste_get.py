import requests

headers = {'Authorization': 'Token 25d0416fa2ccebb87d618a9685e15c3f826e4275'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
# print(resultado.json())

# print(resultado.status_code)

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registro
assert resultado.json()['count'] == 3

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Programação Web Com Python E Django Framework: Essencial'
print(resultado.json()['results'][0]['titulo'])
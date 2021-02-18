import requests

headers = {'Authorization': 'Token b49fda9706f293de268f4a9683f4208171defc7b'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
# print(resultado.json())

# print(resultado.status_code)

# Testando se o endpoint está correto
# assert resultado.status_code == 200

# Testando a quantidade de registro
assert resultado.json()['count'] == 6

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Programação Web Com Python E Django Framework: Essencial'
print(resultado.json()['results'][0]['titulo'])
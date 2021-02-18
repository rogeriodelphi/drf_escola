import requests

headers = {'Authorization': 'Token b49fda9706f293de268f4a9683f4208171defc7b'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}5/', headers=headers)

#Tesntado o codigo HTTP
assert resultado.status_code == 204

#Testanto se o tamanho do conteudo retornado é 0
assert len(resultado.text) == 0
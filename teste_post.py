import requests

headers = {'Authorization': 'Token 25d0416fa2ccebb87d618a9685e15c3f826e4275'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gêrncia Ágil de Projetos com Scrum2",
    "url": "http://www.com.br/scrum2"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo que foi informado
assert resultado.json()['titulo'] == novo_curso["titulo"]
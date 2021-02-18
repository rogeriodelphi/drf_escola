import requests

# GET Avaliacoes

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados desta página
# print(avaliacoes.json()['results'])

# Acessando o primeiro elemento da lista de resuts
# print(avaliacoes.json()['results'][0])

# Acessando o último elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da última pessoa que fez a última avaliação
# print(avaliacoes.json()['results'][-1]['nome'])


# GET Avaliação
# avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/3')
# print((avaliacao.json()))

# GET Cursos
# headers = {'Authorization': 'Token 25d0416fa2ccebb87d618a9685e15c3f826e4275'}
# cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)
# print(cursos.status_code)
# print(cursos.json())
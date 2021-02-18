import requests


class TesteCursos:
    headers = {'Authorization': 'Token b49fda9706f293de268f4a9683f4208171defc7b'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)
        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}8/', headers=self.headers)
        # Testando se o endpoint está correto
        assert resposta.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "titulo": "Metodologia Ágile",
            "url": "http://www.com.br/magile"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo_curso)
        # Testando o código de status HTTP 201
        assert resposta.status_code == 201

        # Testando se o título do curso retornado é o mesmo que foi informado
        assert resposta.json()['titulo'] == novo_curso["titulo"]

    def test_put_curso(self):
        curso_atualizado = {
            "titulo": "Windows Server 2012 Avançado4/",
            "url": "http://www.com/ws/avancado4"
        }
        resposta = requests.put(url=f'{url_base_cursos}8/', headers=headers, data=curso_atualizado)

        # Testando o código de status HTTP
        assert resposta.status_code == 200

        # Testando o título
        assert resposta.json()['titulo'] == curso_atualizado['titulo']

    def test_delete_curso(self):
        resultado = requests.delete(url=f'{url_base_cursos}11/', headers=headers)

        # Testando o codigo HTTP e se o tamanho do conteudo retornado é 0
        assert resultado.status_code == 204 and len(resultado.text) == 0

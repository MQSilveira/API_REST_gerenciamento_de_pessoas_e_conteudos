# Desafio Vaga Backend
Este repositório contém a solução do desafio para uma vaga de Backend na qual eu participei. 
O objetivo do desafio é criar uma API REST utilizando o Django Rest Framework e popular um banco de dados com informações de pessoas e conteúdos.
<br><br>

## Tecnologias utilizadas
* Django
* Django Rest Framework
* PostgreSQL
* Docker
* Docker Compose
* Pytest
<br><br>

## Como executar a aplicação
Para executar a aplicação, você precisa ter o Docker e o Docker Compose instalados em sua máquina.
<br>Em seguida, siga os passos abaixo:

Clone este repositório em sua máquina:
```bash
$ git clone https://github.com/MQSilveira/desafio.git
$ cd desafio
$ docker-compose up -d
```
Após os serviços definidos em docker-compose serem iniciados, faça a migração do banco de dados utilizando o comando:
```bash
$ docker-compose exec web python manage.py migrate
```
Para acessar a API, envie solicitações HTTP para o endereço http://localhost:8000
<br><br>

## Endpoints da API
A API possui os seguintes endpoints:

- `/people/`
<p>POST: Cria uma nova pessoa.</p>
<p>GET: Lista todas as pessoas cadastradas, com seus respectivos conteúdos criados conforme o exemplo de json abaixo:</p>

```bash
[
  {
    "id": 11000,
    "name": "Juli Fishby",
    "contents_created": [
      {
        "id": 10000,
        "text": "Customer-focused even-keeled contingency"
      }
    ]
  }
]
```
<br><br>

- `/people/<int:person_id>/`
<p>GET: Retorna os dados de uma pessoa, com seus respectivos conteúdos criados.</p>
<p>PUT: Atualiza apenaso nome de uma pessoa.</p>
<p>DELETE: Remove o registro de uma única pessoa. Caso a pessoa tenha algum conteúdo criado, todos esses conteúdos também deverão ser removidos.</p>
<br><br>

- `/content/`
<p>POST: Cria um novo conteúdo.</p>
<p>GET: Lista todos os conteúdos cadastrados. Este endpoint deve retornar todos as pessoas que leram o conteúdo, conforme o exemplo de json abaixo:

```json
  {
    "id": 1,
    "text": "Customer-focused even-keeled contingency",
    "read_by": [
      {
        "id": 10001,
        "name": "Marja Claye"
      },
      {
        "id": 10002,
        "name": "Jenifer McCreedy"
      }
    ]
  }
  ```
<br><br>

- `/content/<int:content_id>/`

<p>GET: Retorna os dados de um único  conteúdo. Este endpoint também retorna todos as pessoas que leram o mesmo, conforme mostrado no json anteriormente.</p>
<p>PUT: Atualiza o texto e o criador de um único conteúdo.</p>
<p>DELETE: Remove o registro de um conteúdo.</p>
<br><br>

- `/content/<int:content_pk>/<int:person_pk>/mark-as-read/`

<p>POST: Adiciona uma pessoa que leu um conteúdo (apenas marca como lido por uma determinada pessoa).</p>

* Os endpoints que fazem listagem de dados estão paginados, com a quantidade de 50 elementos por página.
<br><br>

## Licença
Este programa é licenciado sob a licença MIT. Veja o arquivo [LICENSE.md](https://github.com/MQSilveira/desafio/blob/main/LICENSE) para detalhes.
___
Para acessar o README contendo a descrição original do desafio, está nesse [link](https://github.com/MQSilveira/desafio/blob/main/desafio.md).
___
<br>

## Próximos Passos (melhorias futuras)
- Implementar programação assíncrona para minimizar o impacto no banco de dados.
- Melhorar os testes automatizados.
- Workflows para CI utilizando o [github actions](https://github.com/features/actions).
- Deploy em alguma cloud.
<br><br>

## Você pode me encontrar em outras plataformas:
- [LinkedIn](https://www.linkedin.com/in/dev-marcos-silveira/)
- [Website](https://mqsilveira.github.io/pagina_links/)
- marcosilveira.lg@gmail.com


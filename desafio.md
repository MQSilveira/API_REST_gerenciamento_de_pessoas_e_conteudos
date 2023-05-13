# Desafio Vaga Backend

Este desafio está organizado em duas partes para a implementação:

- **Construção de API**

- **Popular o banco de dados**

## 1 - Criar uma API REST utilizando o Django Rest Framework

Esta API deve possuir apenas dois models, `Person` e `Content`. Abaixo os campos que cada um deve ter:

- **Person**

  name: string

- **Content**

  text: string

  creator: Chave estrangeira para o model Person

  read_by: Campo muitos-para-muitos entre os models Person e Content

De acordo com os models acima, a API deve implementar os endpoints abaixo juntamente com os métodos HTTP que eles devem receber:

- `/people/`

  **POST** para a criação de novas linhas na tabela Person;

  **GET** para a listagem das linhas na tabela Person. Além dos dados de cada pessoa, este endpoint deve retornar todos os conteúdos que cada pessoa criou, conforme o exemplo de json abaixo:

  ```json
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

- `/people/<int:person_id>/`

  **GET** para retornar os dados de uma única pessoa. Este endpoint também deve retornar todos os conteúdos que cada pessoa criou, conforme mostrado anteriormente.

  **PUT** para atualizar os dados de uma única pessoa. Como o model Person tem apenas um único campo, este endpoint deve atualizar apenas o campo `name`.

  **DELETE** para apagar o registro de uma única pessoa. Caso a pessoa tenha algum conteúdo criado, todos esses conteúdos também deverão ser removidos.

- `/content/`

  **POST** para a criação de novas linhas na tabela Content;

  **GET** para a listagem das linhas na tabela Content. Além dos dados de cada conteúdo, este endpoint deve retornar todos as pessoas que leram o conteúdo, conforme o exemplo de json abaixo:

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

- `/content/<int:content_id>`

  **GET** para retornar os dados de um único conteúdo. Este endpoint também deve retornar todos as pessoas que leram o mesmo, conforme mostrado no json anteriormente.

  **PUT** para atualizar os dados de um único conteúdo. Neste caso, apenas os campos `text` e `creator` poderão ser atualizados.

  **DELETE** para apagar o registro de um único conteúdo.

- `content/<int:content_pk>/<int:person_pk>/mark-as-read/`

  Este endpoint deverá receber apenas o método **POST**. A sua única função será de adicionar no campo `read_by` uma pessoa que leu um conteúdo, ou seja, apenas marca como lido por uma determinada pessoa.

## 2 - Popular a base de dados

Neste repositório você pode realizar o download do arquivo `data.json`. Este arquivo está estruturado da seguinte forma:

```json
{
  "people": [
    {
      "name": "string"
    }
  ],
  "content": [
    "text": "string"
  ]
}
```

A property `people` é um array contendo **EXATAMENTE** 1000 objetos com a property `name`.

A property `content` é um array contendo **EXATAMENTE** 1000 objetos com a property `text`.

Nesta parte você deve criar um comando que lê este arquivo json e realiza as seguintes operações:

- Cria e salva 1000 instâncias do model `Person` na base de dados;

- Cria e salva 1000 instâncias do model `Content` na base de dados. Cada objeto do tipo `Content` deve possuir um `creator` que é uma instância do model `Person`. Como temos 1000 linhas no model `Person`, cada `Content` deve possuir um `creator` sem problemas;

- Após as duas etapas acima serem finalizadas, o comando deve adicionar no campo `read_by` de cada instância de model `Content` criado as 1000 instâncias do model `Person`. Em resumo, todos as instâncias de `Content` devem possuir no campo `read_by` todas as pessoas que foram cadastradas;

---

## Observações

- Os endpoints que fazem listagem de dados devem estar paginados. O valor mínimo para o `page_size` deve ser de 50 elementos por página.

- Não é necessário criar uma interface web (frontend) para realizar as requisições. Você pode utilizar um cliente http como o [postman](https://www.postman.com/).

- O código deve ser compartilhado via Github.

- Você deve criar um arquivo docker-compose para que possamos subir os containers para avaliar seu trabalho. Este arquivo deve apenas possuir os serviços do banco de dados e do django rodando em modo de desenvolvimento.

## Diferenciais (Não obrigatórios mas irão te destacar)

- Deploy em alguma cloud. Muitas delas estão cobrando hoje em dia, mas recomendamos o [railway](https://railway.app/) pelo fato de seu free tier ser bem generoso.

- Testes automatizados utilizando a library [pytest](https://docs.pytest.org/en/7.3.x/).

- Workflows para CI utilizando o [github actions](https://github.com/features/actions).

- Comando para importação dos dados escrito como um service no arquivo docker-compose.


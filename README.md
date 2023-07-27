# People and Content Management
This repository contains a REST API developed with Django and Django Rest Framework, which allows the management of people and content. The application allows the creation, updating, reading, and deletion of people and content records, as well as keeping track of the people who have read each content. The API was built with the aim of providing a flexible and scalable solution for managing data related to people and content.
<br><br>

## Technologies used
* Django
* Django Rest Framework
* PostgreSQL
* Docker
* Docker Compose
* Pytest
<br><br>

## How to Run the Application
To run the application, you need to have Docker and Docker Compose installed on your machine.
<br>Next, follow the steps below:

Clone this repository on your machine:
```bash
$ git clone https://github.com/MQSilveira/People_and_Content_Management_REST_API.git
$ cd People_and_Content_Management_REST_API
$ docker-compose up -d
```

To access the API, send HTTP requests to the address http://localhost:8000
<br>
![API](https://github.com/MQSilveira/People_and_Content_Management_REST_API/blob/main/files/api.png)



## API Endpoints
The API has the following endpoints:

- `/people/`
<p>POST: Create a new person.</p>
<p>GET: Lists all registered persons, along with their respective created contents, as shown in the example JSON below:</p>

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
<br>

![PEOPLE](https://github.com/MQSilveira/People_and_Content_Management_REST_API/blob/main/files/people.png)

- `/people/<int:person_id>/`
<p>GET: Returns the data of a person, with their respective created contents.</p>
<p>PUT: Updates only the name of a person.</p>
<p>DELETE: Removes the record of a single person. If the person has any content created, all such content should also be removed.</p>
<br><br>

- `/content/`
<p>POST: Create new content.</p>
<p>GET: Lists all the registered contents. This endpoint should return all the people who have read the content, as shown in the example JSON below:

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
<br>

![CONTENT](https://github.com/MQSilveira/People_and_Content_Management_REST_API/blob/main/files/content.png)

- `/content/<int:content_id>/`

<p>GET: Returns the data of a single content. This endpoint also returns all the people who have read the content, as shown in the JSON above.</p>
<p>PUT: Updates the text and creator of a single content.</p>
<p>DELETE: Removes the record of a content.</p>
<br><br>

- `/content/<int:content_pk>/<int:person_pk>/mark-as-read/`

<p>POST: Adds a person who has read a piece of content (only marks it as read by a particular person).</p>

* The endpoints that list data are paginated, with the amount of 50 elements per page.
<br><br>

## License
This program is licensed under the MIT License. See the [LICENSE.md](https://github.com/MQSilveira/desafio/blob/main/LICENSE) file for details.
___
To obtain more details about the project proposal and specific requirements, please refer to the specification document located [here](https://github.com/MQSilveira/People_and_Content_Management_REST_API/blob/main/files/desafio.md).
___
<br>

## You can find me on other platforms:
- [LinkedIn](https://www.linkedin.com/in/dev-marcos-silveira/)
- [Website](https://mqsilveira.github.io/Portfolio/)
- marcosilveira.lg@gmail.com


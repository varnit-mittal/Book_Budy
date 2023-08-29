
![Logo](https://sites.google.com/a/jamesruse.nsw.edu.au/bookbuddy/_/rsrc/1312510514973/config/customLogo.gif?revision=7)


# BookBuddy
This project is made as a part of Zense Recruitment Project which is Coding and Development related club at IIITB. It aims to create a community of book readers and enthusiasts across the Internet.
## Features

- AI model that gives user recommendations on genres based on their favourite books
- Chatting system is provided for the users which is free to use so that they can freely express their ideas and likings. This system is also divided based on genres so that there is no refute between the users of different likings and everyone can enjoy in their community. The Channels are also heavily moderated by the admins so that there is no sort of abusive content on the site since this project is created keeping in mind the users of all ages.
- A Razorpay payment system is provided to buy the premium membership of our website in order to use some speacial community features.
- Video conferencing is a premium feature which is achieved using Agora SDK and helps users connect on a more personal and a closer level.


## API Reference

#### Razorpay API

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `api_key_id`      | `string` | **Required**. This is the key id generated at Razorpay portal|

#### Agora API

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `APP_ID` | `string` | **Required**. Your APP ID generated at Agora portal |


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `CHANNEL`      | `string` | **Required**. This is the name of the dynamic or static channel created for the user|

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `TOKEN` | `string` | **Required**. Dynamically generated through python's agora_token_builder module|

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `uid` | `number` | **Required**. Unique id of the user joining the channel|


## URL Structures

| URL| Use   | 
| :-------- | :------- | 
| `/` | landing page |
| `/login/` | login page | 
| `/signup/` | signup page |
| `/logout/` | logout confirmation page |
| `/books/home/` | main home page |
| `/books/room/<str:pk>/` | chatting page for the room |
| `/books/create/` | room creation page only for the admins |
| `/books/delete/<str:rm>/<str:pk>/` | a delete message confirmation page |
| `/profile/` | profile viewing and update page |
| `/payment/` | paying page |
| `/payment/success/` | payment successful page |
| `/video/lobby` | video lobby community page |
| `/video/lobby/room` | video conference page |
| `/video/create` | video room creation page |

## Run Locally

Clone the project

```bash
  git clone https://github.com/varnit-mittal/Book_Budy.git
```

Go to the project directory

```bash
  cd Book_Budy
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Make migrations

```bash
  python manage.py makemigrations
```

Migrate to create a database

```bash
  python manage.py migrate
```

Create a Superuser
```bash
  python manage.py createsuperuser
```

Collect all the static files
```bash
  python manage.py collectstatic
```

Start server
```bash
  python manage.py runserver
```

## Documentation

[Documentation](https://drive.google.com/file/d/1-uGHS-x8DD0UmkCvoXfKmIQY41A4e8zo/view?usp=sharing)

## Authors

 [@varnit-mittal](https://github.com/varnit-mittal)


## License

[MIT](https://choosealicense.com/licenses/mit/)


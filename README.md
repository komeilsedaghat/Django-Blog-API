# Django Blog API

### Features
- Custom User
- Auth Using Token
- CRUD Articles
- Login,Register And Logout View
- Password Change And Reset
- Custom Permission
- Admin Panel(For CRUD Users)
- Custom Throttle And Set in Views
- Add Schema 
- Change Token Authentication To JWT Authentication
- Pagination(Custom Pagination)
- Set Parser Class(JSONParser)
## API Endpoints


- `/api/accounts/register/`
<br>POST - Creates new user (**username**, **phone_number**, **password**,**Password2** as form data)
- `/api/accounts/login/`
<br>POST - Login(**username** & **email** & **password** form data)
- `/api/accounts/logout/`
<br>POST - For Logout User
- `/api/accounts/password_change/`
<br>POST - For Change Password(**Old password**,**New Password**)
- `/api/accounts/password_reset/`
<br>POST - Reset Password (**Email** , form data)
- `/api/accounts/create-token/`
<br>POST - Create Token And Login (**username** ,**password** form data)
- `/api/accounts/revoke_token/`
<br>DELETE - Revoke Token (**Token** )
- `/api/accounts/token/`
<br>POST - get access and refresh token (**username**,**password** )
- `/api/accounts/token/refresh/`
<br>POST - get new access token (**refresh token** )


- `/api/articles/`
<br>GET - Retrive all Articles
- `api/articles/detail/<slug:slug>/`
<br>GET - Detail Article
- `api/articles/delete/<slug:slug>/`
<br>DELETE - Delete Article
- `api/articles/update/<slug:slug>/`
<br>PUT - Update Article
- `api/articles/add-article/`
<br>POST - Add Article
- `api/articles/admin_panel/`
<br>POST - Add User
<br>GET - List User
- `api/articles/admin_panel/<int:pk>/`
<br>DELETE - Delete User
<br>PUT - Update User
- `/swagger/`
<br>GET - Schema


## Setup

Clone the repo:
```bash
git clone
https://github.com/komeilsedaghat/Django-Blog-API.git
```
Now cd into cloned repo, create a virtualenv and pip install the requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
Create and apply the migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Create a superuser for admin privilages
```bash
python3 manage.py createsuperuser
```
Now set the variables `SECRET_KEY` from `BlogApi/.env-sample` either as environment variables or hard code them into the file itself.
<br>Start the server
```bash
python3 manage.py runserver
```
Head over to [localhost:8000](http://localhost:8000/), or **Postman** to use the application

---


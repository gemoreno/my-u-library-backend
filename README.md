# 📚 My U Library – Backend

This is the backend API for **My U Library**, a simple library management system built with **Django** and **PostgreSQL**.

It supports:
- 🔐 Custom user authentication (email-based)
- 📚 Book management (with unique title-author constraints)
- ✅ Librarian/student/admin roles
- 🔄 Checkout and return logic

---

## 🚀 Tech Stack

- Python 3.10+
- Django 4+
- PostgreSQL
- Django REST Framework
- Deployed on Render

---

## 📁 Project Structure

```
my-u-lib-back/
│
├── core/              # Django settings & WSGI
├── library/           # Main app (users, books, checkout logic)
├── manage.py
├── requirements.txt
└── render.yaml        # For Render deployment
```

---

## 🔧 Setup (Local)

1. **Clone the repo**

```bash
git clone https://github.com/your-username/my-u-lib-back.git
cd my-u-lib-back
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create `.env` file**

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://username:password@localhost:5432/mydb
DJANGO_SETTINGS_MODULE=core.settings
```

5. **Run migrations and create superuser**

```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Start development server**

```bash
python manage.py runserver
```

---

## 🌐 API Overview

| Endpoint             | Method | Description                          |
|----------------------|--------|--------------------------------------|
| `/api/token/`        | POST   | Obtain JWT token                     |
| `/api/token/refresh/`| POST   | Refresh JWT                          |
| `/api/auth/me/`      | GET    | Get current user info                |
| `/api/users/`        | POST   | Admin/librarian creates new user     |
| `/api/books/`        | GET/POST | Search or add books               |
| `/api/checkouts/`    | POST   | Checkout a book                      |
| `/api/returns/`      | POST   | Return a book                        |

All endpoints use JSON format and are protected using role-based permissions.

---

## 🐳 Deployment (Render)

This project uses [`render.yaml`](./render.yaml) to define infrastructure:

```yaml
services:
  - type: web
    name: my-u-lib-backend
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn core.wsgi:application
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: core.settings
      - key: SECRET_KEY
        value: your_django_secret_key
      - key: DEBUG
        value: False
      - key: DATABASE_URL
        fromDatabase:
          name: my-database-name
          property: connectionString
```

> ✅ Make sure your PostgreSQL database is also created in Render and linked.

---

## 📦 Requirements

See [`requirements.txt`](./requirements.txt)

Key packages:
- `Django`
- `djangorestframework`
- `psycopg2-binary`
- `gunicorn`
- `python-decouple` (optional for `.env`)

---

## 📃 License

MIT – Feel free to use and modify for educational or non-commercial projects.

---

## 🙋‍♂️ Maintainer

Created by **Gerardo Moreno** – Electrical & Software Engineer

Feel free to reach out if you want help integrating this backend into a frontend or deploying it live.

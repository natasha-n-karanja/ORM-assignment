# 📚 ORM Assignment - Bookstore Manager

This project is a **Bookstore Management System** built using **Python**, **SQLAlchemy ORM**, and **PostgreSQL**. It provides functionality to manage books with the ability to create, read, update, delete (CRUD), and search for books in a PostgreSQL database.

---

## 🚀 Features

- Add new books with title, author, genre, and price
- View a list of all books
- Update existing book details
- Delete books
- Search for books by title or author

---

## 🧑‍💻 How to Run This Project

- 1. 🔁 Clone the repository

git clone https://github.com/your-username/ORM-assignment.git
cd ORM-assignment

---

- 2.🧪 Create & activate a virtual environment 

python3 -m venv venv
source venv/bin/activate

---

- 3. 📥 Install this

pip install -r requirements.txt

---

- 4. 🗃 Set up PostgreSQL

sudo -u postgres psql

-- Inside the PostgreSQL shell:
CREATE DATABASE bookstore;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE bookstore TO myuser;
\q

---

- 5. ⚙️ Configure database connection

DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost/bookstore"

- 6. 🏃 Run the application

python app.py

---


# 📚 SmartLibrary – Library Management System (Django)

## 📌 Project Overview

This project is a backend-focused web application built using Django that simulates a real-world library management system.

It allows users to manage books, issue and return books, and track due dates while ensuring proper handling of book availability.

The main focus of this project is to implement clean CRUD operations, business logic for issuing/returning books, and date-based validation such as late return tracking.

---

## ⚙️ Key Features

📚 Add, view, edit, and delete books
📖 Issue books with user name input
🔄 Return books and update availability
⏱️ Automatic due date assignment
⚠️ Late days calculation based on return date
📊 Track issued books with status (Issued/Returned)
🚫 Prevent issuing already issued books
🧠 Clean structure using Django (models, views, templates, urls)
🎨 Simple and clean UI using HTML & CSS

---

## 🧠 Core Logic (Important)

The system manages book issuing using backend logic:

* Each book has an `is_available` field
* When a book is issued → it becomes Not Available
* When returned → availability is restored

Late return is calculated using:

* `due_date` (assigned during issue)
* `return_date` (captured on return)
* If not returned → current date is used

Late days = difference between due date and return/current date

This ensures proper tracking of overdue books.

---

## 🛠️ Tech Stack

Python 🐍
Django 🌐
PostgreSQL 🗄️
HTML + CSS 🎨

---
## 📂 Project Structure

```text
smartLibrary/
│
├── libraryApp/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── book_list.html
│   │   ├── add_book.html
│   │   ├── issue_book.html
│   │   ├── issued_books.html
│   │   ├── edit_book.html
│
├── smartLibrary/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
```

## 🔗 Application Routes

### 📚 Book Management

GET `/` → View all books
GET `/add-book/` → Add new book
GET `/edit-book/<id>/` → Edit book
GET `/delete-book/<id>/` → Delete book

### 📖 Issue & Return

GET `/issue/<book_id>/` → Issue book
GET `/return/<issue_id>/` → Return book

### 📊 Issued Books

GET `/issued-books/` → View all issued books

---

## ▶️ How to Run the Project

Clone the repository:

```
git clone <your-repo-link>
```

Navigate to project folder:

```
cd smartLibrary
```

Install dependencies:

```
pip install -r requirements.txt
```

Apply migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Run server:

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## 📊 Example Use Case

✅ Issue Book:

* User enters name
* Book becomes unavailable
* Due date is assigned

🔄 Return Book:

* Return date stored
* Availability restored
* Late days calculated

---

## 💡 Key Learnings

Implemented real-world library workflow
Handled CRUD operations in Django
Applied business logic for availability tracking
Worked with date/time operations
Improved debugging and problem-solving skills
Built structured backend system with UI integration

---

## 🚀 Future Improvements

🔐 Add authentication (login/signup)
🔍 Add search functionality
🌐 Convert to Django REST Framework (API version)
🎨 Improve UI with Bootstrap
📈 Add fine calculation system

---

## 🙌 Conclusion

This project helped me understand how backend systems handle real-world operations like issuing, returning, and tracking items.

It strengthened my knowledge of Django, database relationships, and business logic implementation, and improved my ability to build structured backend applications.

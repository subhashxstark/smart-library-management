# 📚 SmartLibrary – Library Management System (Django)

**🌐 Live Application:** 
http://18.61.83.194:8000

## 📌 Project Overview

This project is a backend-focused web application built using Django that simulates a real-world library management system.

It allows users to manage books, issue and return books, and track due dates while ensuring proper handling of book availability.

The main focus of this project is to implement clean CRUD operations, business logic for issuing/returning books, and date-based validation such as late return tracking.

---
``` text
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

```
---
## 📸 Screenshots
📸 📚 Book List / Home Page

Displays all books in the library with details like title, author, and availability status.  
Allows users to issue available books and manage records using edit and delete options.

<img width="1920" height="1020" alt="book_list(homepage)" src="https://github.com/user-attachments/assets/c93ae14c-2b35-4a0d-a00e-02f82f0d4f9f" />

📸 ➕ Add Book Page

Allows users to add new books to the library by entering the book title and author name.
Provides a simple form interface for quick and easy data entry.

<img width="1920" height="1020" alt="add_book" src="https://github.com/user-attachments/assets/6274188d-7420-4372-b1e6-1ef943d3efba" />

📸 ✏️ Edit Book Page

Allows users to update existing book details such as title and author name.
Provides a simple interface to modify records and save changes efficiently.

<img width="1920" height="1020" alt="edit_book" src="https://github.com/user-attachments/assets/b7cca7c7-cf56-4402-b032-4edc8ab99726" />

📸 📖 Issue Book Page

Displays selected book details and allows users to issue the book by entering their name.
Ensures only available books can be issued through a simple and clear interface.

<img width="1920" height="1020" alt="issue_book" src="https://github.com/user-attachments/assets/ccc77415-34c0-40b1-b00c-0d70a8a3bda9" />

📸 📚 Issued Books Page

Displays all issued books with details such as user name, issue date, due date, and return status.
Allows users to track issued records and return books through a simple interface.

<img width="1920" height="1020" alt="5_issued_books" src="https://github.com/user-attachments/assets/531e2817-9f3c-4c6e-b837-55cdb802fa1a" />


## 🧠 Core Logic (Important)

The system manages book issuing using backend logic:

- Each book has an **`is_available`** field  
- When a book is issued → it becomes **`Not Available`**  
- When returned → availability is restored  
- All issued records are stored in **`PostgreSQL`** for tracking history  
- Return updates the **`return_date`** and restores book availability  
- System tracks **`user`**, **`issue_date`**, **`due_date`**, **`return_date`**, and **`status`** (**`Issued`**/**`Returned`**/**`Late`**)  
- Only available books can be issued  
- Issued records cannot be edited or deleted to maintain data integrity  

### 📅 Late Return Calculation

- **`due_date`** (assigned during issue)  
- **`return_date`** (captured on return)  
- If not returned → current date is used  
- Late days = difference between **`due_date`** and return/current date  

This ensures proper tracking of overdue books.

---

## 🛠️ Tech Stack
```
Python 🐍
Django 🌐
PostgreSQL 🗄️
HTML + CSS 🎨
Docker
AWS EC2
```
---
## 📂 Project Structure

```text
smartLibrary/
│
├── libraryApp/                # Main application
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates (UI)
│   ├── __init__.py
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   ├── models.py             # Database models
│   ├── tests.py              # Test cases
│   ├── views.py              # Application logic
│
├── screenshots/              # Project UI screenshots
│   ├── 1_home.png
│   ├── 2_add_book.png
│   ├── 3_edit_book.png
│   ├── 4_issue_book.png
│   ├── 5_issued_books.png
│
├── smartLibrary/             # Project configuration
│   ├── __init__.py
│   ├── asgi.py               # ASGI config
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI config
│
├── .dockerignore             # Docker ignore file
├── .gitignore                # Git ignore file
├── Dockerfile                # Docker configuration
├── manage.py                 # Django management script
├── README.md                 # Project documentation
├── requirements.txt          # Project dependencies
```

## 🔗 Application Routes

### 📚 Book Management

GET `/` → View all books

GET `/add-book/` → Display form to add a new book

POST `/add-book/` → Add a new book

GET `/edit-book/<book_id>/` → Display edit form

POST `/edit-book/<book_id>/` → Update book details

GET `/delete-book/<book_id>/` → Delete a book

### 📖 Issue & Return

GET `/issue/<book_id>/` → Display issue page

POST `/issue/<book_id>/` → Issue book and mark unavailable

GET `/return/<issue_id>/` → Return book and update status

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
``` text
Implemented real-world library workflow
Handled CRUD operations in Django
Applied business logic for availability tracking
Worked with date/time operations
Improved debugging and problem-solving skills
Built structured backend system with UI integration
```
---

## 🐳 Docker Setup

This project is containerized using Docker to ensure consistent environment setup and easy deployment.

### 🔧 Steps Performed

* Created a `Dockerfile` for the Django application
* Installed required dependencies using `requirements.txt`
* Configured application to run using **Gunicorn**
* Exposed application on port **8000**

### ▶️ Run with Docker

```
docker build -t smartlibrary .
docker run -d -p 8000:8000 smartlibrary
```

---

## ☁️ AWS EC2 Deployment

The application is deployed on an AWS EC2 instance and is accessible via public IP.

### 🔧 Deployment Steps

* Launched an Ubuntu EC2 instance
* Installed Docker and PostgreSQL on the server
* Configured Security Groups (ports 22 for SSH and 8000 for application)
* Cloned project from GitHub repository
* Built Docker image on EC2
* Ran Docker container in detached mode
* Connected Django application to PostgreSQL running on EC2
---
## 💡 Deployment Highlights

* Dockerized Django application for portability
* Deployed on AWS EC2 for public access
* PostgreSQL used for persistent data storage
* Application accessible across multiple devices
* Real-time data updates using centralized database

---


## 🚀 Future Improvements
``` text
🔐 Add authentication (login/signup)
🔍 Add search functionality
🌐 Convert to Django REST Framework (API version)
🎨 Improve UI with Bootstrap
📈 Add fine calculation system
```
---

## 🙌 Conclusion

This project helped me understand how backend systems handle real-world operations like issuing, returning, and tracking items.

It strengthened my knowledge of Django, database relationships, and business logic implementation, and improved my ability to build structured backend applications.

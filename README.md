# TodoManager — Full-Stack Task Management Web Application

A secure, multi-user task management web application built with **Python, Django, MySQL, and Bootstrap 5**, featuring route protection, strict per-user data isolation, and a modern glassmorphic UI.

---

## Key Features

- **User Authentication & Registration:** Built-in Django authentication system for secure user signup, login, and logout.
- **Route Protection & Access Control:** Unauthenticated users and direct URL access to protected pages are blocked using `@login_required`.
- **Per-User Data Isolation & Ownership Validation:** Queries filter tasks strictly by `request.user` with ownership checks so users can only view, edit, or delete their own tasks.
- **Full CRUD Operations:** Create, view, update, mark complete, and delete tasks seamlessly backed by MySQL and Django ORM.
- **Contact & Support Module:** Dedicated contact/feedback page integrated with the database.
- **Modern Glassmorphic UI:** Responsive design built with Bootstrap 5, Django Crispy Forms, frosted-glass styling, and scroll/hover animations.

---

## Tech Stack

- **Backend:** Python, Django (MVT Architecture, Django ORM)
- **Database:** MySQL
- **Frontend:** HTML5, CSS3, Bootstrap 5, Django Crispy Forms, AOS Animations
- **Tools:** Git, GitHub, VS Code

---

## Local Setup & Installation

1. **Clone the repository**
   ```bash
   git clone  https://github.com/surajv2025/TodoManager.git
   cd TodoManager





1.Create and activate a virtual environment

Bash
python -m venv todo_env
# On Windows:
todo_env\Scripts\activate


2.Install dependencies

Bash
pip install -r requirements.txt


3.Configure MySQL Database

Create a MySQL database (e.g., todomanager_db).

Update DATABASES and SECRET_KEY in TodoManager/settings.py (or configure via environment variables).


4.Apply migrations & start the server

Bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver



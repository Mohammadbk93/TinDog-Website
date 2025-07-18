# TinDog 🐶

TinDog is a fun, imaginary dating website for dogs, inspired by the idea of combining pet enthusiasm with modern web development. This project was created to practice and demonstrate full-stack skills including frontend design, backend development, and RESTful API integration using **FastAPI**.

It’s a playful concept meant to sharpen my technical skills while building something entertaining and interactive.

## 🌐 Live Website

🔗 [Visit the deployed version here](https://tindog-website-uwnd.onrender.com/)

<img width="1079" height="388" alt="TinDog_1" src="https://github.com/user-attachments/assets/fa960ad6-0662-40cd-b94f-205edf318a9f" />


---

## 🎯 Project Objectives

- Develop a full-stack web application using FastAPI and HTML/CSS.
- Allow users (dog owners) to register via a signup form.
- Handle user data using a SQLite database via SQLAlchemy ORM.
- Serve static assets and render dynamic HTML templates.
- Deploy and run the project locally or via cloud (e.g., Render or Railway).

---

## 🛠 Tech Stack

### Backend:
- **FastAPI** – for API development and server-side rendering.
- **SQLAlchemy** – ORM for database management.
- **PostgreSQL** – production-grade relational database.
- **Jinja2** – for rendering HTML templates.

### Frontend:
- **HTML5/CSS3**
- **Bootstrap 5** – for styling and modal UI.
- **JavaScript** – for client-side form validation and interactivity.

---

## 🗄️ Database: PostgreSQL

For this project, I used **PostgreSQL** to store user registration data.

### 🧾 Users Table Overview

The `users` table stores the following information:

| Column Name | Data Type           | Description                                  |
|-------------|---------------------|----------------------------------------------|
| `id`        | `integer (PK)`      | Unique identifier for each user              |
| `name`      | `varchar`           | Full name of the user                        |
| `email`     | `varchar`           | User's email address (must be unique)        |
| `password`  | `varchar` (hashed)  | User password hashed using **bcrypt**        |
| `created_at`| `timestamp`         | Date and time when the user was registered   |

### 🔐 Password Security

- Passwords are **never stored in plain text**.
- They are hashed using **bcrypt** to ensure user privacy and security.

### 🕒 Timestamps

- Each user record includes a `created_at` field.
- This tracks the **exact time** of registration for logging and auditing purposes.


### Utilities:
- **Uvicorn** – ASGI server for running FastAPI.
- **CORS Middleware** – to allow cross-origin requests.
- **Jinja2Templates** – to render dynamic HTML content.


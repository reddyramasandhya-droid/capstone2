# Capstone 2 – Student CRUD App (Django)

A simple web application built with **Django** that performs **CRUD** (Create, Read, Update, Delete) operations on student records. Data is stored in an SQLite database.

> 🎓 Built as part of the **Full Stack Python Internship** at [CodingBrains](https://codingbrains.in).

🔗 **Live Demo:** [ramasandhyasomula.pythonanywhere.com](https://ramasandhyasomula.pythonanywhere.com/)

📦 **Repository:** [github.com/reddyramasandhya-droid/capstone2](https://github.com/reddyramasandhya-droid/capstone2)

---

## Features

- **Create** – add a new student using the "Insert Student Details" form
- **Read** – view all students in the "Student Details" table on the same page
- **Update** – click **Edit** to open a pre-filled form and update a student's details
- **Delete** – click **Delete** to remove a student record
- Clean, responsive UI styled with Bootstrap

Each student record stores:

| Field  | Type                   |
| ------ | ---------------------- |
| Name   | Text (max 25 chars)    |
| Email  | Text (max 25 chars)    |
| Age    | Text (max 25 chars)    |
| Gender | Text (max 25 chars)    |

## Screenshots

### Home Page – Insert Form and Student List
<img width="1917" height="545" alt="Image" src="https://github.com/user-attachments/assets/b72a70ed-e23c-4706-ae0b-57f4d203c52f" />

### Update Student Details
<img width="1046" height="551" alt="Image" src="https://github.com/user-attachments/assets/f039b2ae-a539-4d9a-a9e7-72e83aa3c8c6" />
## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML templates (Django template engine), Bootstrap
- **Deployment:** PythonAnywhere

## Project Structure

```
capstone2/
├── app/                 # Main app: models, views, templates
│   └── templates/app/   # index.html, edit.html, ...
├── crud/                # Project settings and URL configuration
├── screenshots/         # Images used in this README
├── db.sqlite3           # SQLite database
├── manage.py            # Django command-line utility
└── requirements.txt     # Python dependencies
```

## Getting Started (Run Locally)

**Requirements:** Python 3.12 or newer (needed for Django 6.x)

1. **Clone the repository**
   ```bash
   git clone https://github.com/reddyramasandhya-droid/capstone2.git
   cd capstone2
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env

   # Windows
   env\Scripts\activate

   # macOS / Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. Open **http://127.0.0.1:8002/** in your browser.

### Optional: create an admin user

```bash
python manage.py createsuperuser
```

Then visit **http://127.0.0.1:8002/admin/**.

## Deployment Notes (PythonAnywhere)

- Add your PythonAnywhere domain to `ALLOWED_HOSTS` in `crud/settings.py`.
- The free plan runs an older Python version, so you may need a compatible Django version (for example `Django==5.2.17`) in `requirements.txt` on the server.
- After pulling new changes, reload the web app from the **Web** tab.

## Author

**Somula Rama Sandhya**
BTech (AIML), Presidency University, Bangalore
Full Stack Python Intern, CodingBrains
GitHub: [@reddyramasandhya-droid](https://github.com/reddyramasandhya-droid)

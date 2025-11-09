# Offline Quiz Manager

A simple offline-capable web application built with **Django** and **Tailwind CSS** that allows users to create, manage, and take quizzes. This project was developed as part of a technical task to demonstrate Django, Python, and Tailwind CSS skills.

---

## Features

### Admin Interface
- Create, edit, and delete quizzes.
- Each quiz can contain multiple questions.
- Each question includes:
  - Question text
  - Four answer options (`option1`–`option4`)
  - One correct answer
- Basic dashboard displaying:
  - Total quizzes and questions
  - Quiz attempt history
  - Average scores

### User Interface
- List all available quizzes.
- Take a quiz (all questions on one page).
- Submit answers and view result summary.
- Option to retake quizzes.
- View personal quiz attempt history.

---

## Tech Stack

| Component | Tool |
|------------|------|
| Backend | Django 4.2 |
| Frontend | Tailwind CSS |
| Web Server | Gunicorn |
| Static Files | WhiteNoise |
| Database | SQLite (local) |
| Deployment | Render (Free Tier) |
| Database | SQLite (default Django database) |
| Authentication | Django built-in authentication for user quiz attempts |

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/winhtet1997/quizz-manager.git
cd quizz-manager
```

2. **Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Create a superuser**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Access the app**
- Admin panel: `http://localhost:8000/admin/`
- User interface: `http://localhost:8000/`

---

## Usage

1. Log in to the **admin panel** to create quizzes and questions.
2. Add four options for each question and select the correct answer.
3. On the user side, navigate to the quiz list, take a quiz, and submit answers.
4. View results and history of past quiz attempts.

---

## Screenshots
**Admin Portal**
<img width="1920" height="1150" alt="image" src="https://github.com/user-attachments/assets/7650d9a2-66ac-4cfc-9313-ff70128c8d7c" />

**Quiz List**
<img width="1920" height="1150" alt="image" src="https://github.com/user-attachments/assets/9fcac7a5-e9ea-4d73-a14c-ef539c28897b" />

**History**
<img width="1920" height="1150" alt="image" src="https://github.com/user-attachments/assets/40f5212c-8b12-45a0-ac06-35cc28522eb1" />

**Quiz Taking**
<img width="1920" height="1150" alt="image" src="https://github.com/user-attachments/assets/f5a6af97-b7aa-4f54-bd57-1b886b4485fb" />

**Result**
<img width="1920" height="1150" alt="image" src="https://github.com/user-attachments/assets/00b793cf-c829-43f4-b52d-27ace9890f9b" />

---

## License

This project is for demonstration purposes. No license applied.

---

## Author

**Win Win Htet**  
Technical Task: Offline Quiz Manager for Django/Tailwind assessment

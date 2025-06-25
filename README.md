# 🎓 Student Management System (Gradio + SQLite)

A simple, interactive Student Management System built with **Python**, **SQLite**, and **Gradio**. Perfect for learning and practicing SQL concepts such as CRUD operations, JOINs, aggregate functions, and more — all from a modern, visual UI.

---

## ✅ Features

- 🧑 Add, list, search, and delete students
- 📘 Add courses and assign students
- 📚 View enrolled courses per student
- ✏️ Update student GPA
- 📊 View reports (Average GPA, student count, etc.)
- 🖥️ Interactive Gradio interface (no frontend coding needed!)

---

## 🏗️ Project Structure

```
frosty-8-student-management/
├── main.py              # Gradio app entry point
├── database.py          # DB schema and connection
├── models/
│   ├── student.py       # Student-related logic
│   └── course.py        # Course and enrollment logic
├── student_mgmt.db      # SQLite database (auto-generated)
├── pyproject.toml       # Project dependencies
├── uv.lock              # uv virtual environment lockfile
└── README.md
```

---

## 🚀 Getting Started

### 🔧 Prerequisites
- Python 3.12+
- [`uv` package manager](https://github.com/astral-sh/uv) (recommended) or `pip`

### 📦 Install Dependencies

Using **uv**:
```bash
uv venv
uv pip install -r requirements.txt
uv run main.py
```

Or using **pip**:
```bash
pip install gradio
python main.py
```

---

## 🌐 Run the App

```bash
python main.py
```

Then open [http://127.0.0.1:7860](http://127.0.0.1:7860) in your browser.

---

## 💻 SQL Concepts Covered

| SQL Concept        | Example Usage                       |
|--------------------|-------------------------------------|
| `CREATE TABLE`     | Define schema for students, courses |
| `INSERT`           | Add student/course records          |
| `SELECT` + `JOIN`  | View courses for a student          |
| `DELETE`           | Remove student records              |
| `UPDATE`           | Modify student GPA                  |
| `LIKE`             | Search students by name             |
| `GROUP BY`, `AVG`  | GPA reporting by age                |
| `COUNT`            | Number of students per age          |
| `FOREIGN KEY`      | Enrollment table                    |
| `PRIMARY KEY`      | ID fields in tables                 |

---

## 📊 Built-In Reports

- 📈 Average GPA by Age
- 👥 Student Count by Age
- 🔢 Total Number of Students

---

## 🌍 Deployment Notes

SQLite is used for simplicity and learning. For **production**, consider using a managed PostgreSQL instance on:
- [Render](https://render.com)
- [Railway](https://railway.app)
- [Supabase](https://supabase.io)

Gradio can be deployed easily on **Render**, **Railway**, or even **Hugging Face Spaces**.

---

## 📌 To-Do / Extensions

- [ ] Add student photo upload
- [ ] Export reports to CSV
- [ ] Authentication with user roles
- [ ] Switch to PostgreSQL for persistence
- [ ] Add charts with Plotly or matplotlib

---

## 🧑‍💻 Author

Built with ❤️ by **Sarthak Dongare**

---

## 📄 License

MIT License – free to use and modify

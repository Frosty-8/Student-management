import sqlite3

def get_connection():
    return sqlite3.connect("student_mgmt.db")

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        # STUDENTS TABLE
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                gpa REAL
            )
        ''')

        # COURSES TABLE
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                credits INTEGER
            )
        ''')

        # ENROLLMENTS TABLE (Many-to-Many)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS enrollments (
                student_id INTEGER,
                course_id INTEGER,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id)
            )
        ''')

        conn.commit()

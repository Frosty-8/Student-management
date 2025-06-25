from database import get_connection

def add_student(name,age,gpa):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO students (name,age,gpa) VALUES (?,?,?)", (name,age,gpa)
        )
        conn.commit()

def list_students():
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM students ORDER BY name"
        )
        return cursor.fetchall()
    
def search_student(name):
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM students WHERE name LIKE ? ", ('%' + name + '%',)
        )
        return cursor.fetchall()
    
def delete_student(student_id):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM students WHERE id = ?", (student_id,)
        )
        conn.commit()

def update_gpa(student_id,new_gpa):
    with get_connection() as conn:
        conn.execute(
            " UPDATE students SET gpa = ? WHERE id = ?",(new_gpa,student_id)
        )
        conn.commit()

def avg_gpa_by_age():
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT AVG(gpa) FROM students GROUP BY age ORDER BY age"
        )
        return cursor.fetchall()
    
def student_count_by_age():
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT age , COUNT(*) FROM students GROUP BY age ORDER BY age"
        )
        return cursor.fetchall()
    
def total_student_count():
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT COUNT(*) FROM students"
        )
        return cursor.fetchone()[0]
    
def avg_gpa_by_age():
    with get_connection() as conn:
        cursor = conn.execute("SELECT age, AVG(gpa) FROM students WHERE gpa IS NOT NULL GROUP BY age ORDER BY age")
        return [row for row in cursor.fetchall() if row[0] is not None and row[1] is not None]

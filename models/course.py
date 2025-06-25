from database import get_connection

def add_course(name,credits):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO courses (name,credits) VALUES (?,?)",(name,credits)
        )
        conn.commit()

def list_courses():
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM courses ORDER BY name"
        )
        return cursor.fetchall()
    
def enroll_student(course_id,student_id):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO enrollments (course_id,student_id) VALUES (?,?)",(course_id,student_id)
        )
        conn.commit()

def get_student_courses(student_id):
    with get_connection() as conn:
        cursor = conn.execute(
            """SELECT c.name,c.credits 
            FROM enrollments e 
            JOIN courses c ON e.course_id = c.id
            WHERE e.student_id=?""",(student_id,)
        )
        return cursor.fetchall()
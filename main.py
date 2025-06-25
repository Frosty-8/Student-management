import gradio as gr
from database import init_db
from models import student, course

# Initialize DB once
init_db()

# Gradio Functions
def add_student(name, age, gpa):
    student.add_student(name, int(age), float(gpa))
    return f"✅ Student '{name}' added successfully!"

def list_students():
    data = student.list_students()
    return "\n".join([f"ID: {s[0]} | Name: {s[1]} | Age: {s[2]} | GPA: {s[3]}" for s in data])

def search_student(keyword):
    data = student.search_student(keyword)
    return "\n".join([f"ID: {s[0]} | Name: {s[1]} | Age: {s[2]} | GPA: {s[3]}" for s in data]) or "No results found."

def delete_student(sid):
    student.delete_student(int(sid))
    return f"🗑️ Student ID {sid} deleted."

def add_course(name, credits):
    course.add_course(name, int(credits))
    return f"📘 Course '{name}' added successfully!"

def enroll_student(sid, cid):
    course.enroll_student(int(sid), int(cid))
    return f"📚 Student {sid} enrolled in Course {cid}."

def view_courses(sid):
    data = course.get_student_courses(int(sid))
    return "\n".join([f"{c[0]} ({c[1]} credits)" for c in data]) or "No courses found."

def format_report(data, label1, label2):
    if not data:
        return "⚠️ No data available."

    lines = [f"{label1:<10} | {label2}"]
    lines.append("-" * 25)

    for row in data:
        if not row or len(row) < 2:
            continue  # skip malformed rows
        val1 = str(row[0])
        val2 = f"{row[1]:.2f}" if isinstance(row[1], float) else str(row[1])
        lines.append(f"{val1:<10} | {val2}")

    return "\n".join(lines) if len(lines) > 2 else "⚠️ No valid records found."


# Tabs for Gradio App
with gr.Blocks(title="Student Management System") as demo:
    gr.Markdown("## 🎓 Student Management System")

    with gr.Tab("Add Student"):
        with gr.Row():
            name = gr.Textbox(label="Name")
            age = gr.Number(label="Age", precision=0)
            gpa = gr.Number(label="GPA", precision=2)
        add_btn = gr.Button("Add Student")
        output1 = gr.Textbox(label="Status")
        add_btn.click(fn=add_student, inputs=[name, age, gpa], outputs=output1)

    with gr.Tab("List Students"):
        list_btn = gr.Button("Refresh List")
        student_output = gr.Textbox(label="All Students", lines=10)
        list_btn.click(fn=list_students, outputs=student_output)

    with gr.Tab("Search Student"):
        keyword = gr.Textbox(label="Search by Name")
        search_btn = gr.Button("Search")
        search_output = gr.Textbox(label="Results", lines=5)
        search_btn.click(fn=search_student, inputs=keyword, outputs=search_output)

    with gr.Tab("Delete Student"):
        sid_input = gr.Number(label="Student ID", precision=0)
        del_btn = gr.Button("Delete")
        del_output = gr.Textbox(label="Status")
        del_btn.click(fn=delete_student, inputs=sid_input, outputs=del_output)

    with gr.Tab("Add Course"):
        cname = gr.Textbox(label="Course Name")
        credits = gr.Number(label="Credits", precision=0)
        course_btn = gr.Button("Add Course")
        course_output = gr.Textbox(label="Status")
        course_btn.click(fn=add_course, inputs=[cname, credits], outputs=course_output)

    with gr.Tab("Enroll Student"):
        enroll_sid = gr.Number(label="Student ID", precision=0)
        enroll_cid = gr.Number(label="Course ID", precision=0)
        enroll_btn = gr.Button("Enroll")
        enroll_output = gr.Textbox(label="Status")
        enroll_btn.click(fn=enroll_student, inputs=[enroll_sid, enroll_cid], outputs=enroll_output)

    with gr.Tab("View Student Courses"):
        view_sid = gr.Number(label="Student ID", precision=0)
        view_btn = gr.Button("View Courses")
        view_output = gr.Textbox(label="Courses", lines=5)
        view_btn.click(fn=view_courses, inputs=view_sid, outputs=view_output)


    with gr.Tab("✏️ Update GPA"):
        update_id = gr.Number(label="Student ID", precision=0)
        update_gpa_val = gr.Number(label="New GPA", precision=2)
        update_btn = gr.Button("Update GPA")
        update_output = gr.Textbox(label="Status")

        def handle_gpa_update(sid, gpa):
            try:
                student.update_gpa(int(sid), float(gpa))
                return f"✅ Updated Student ID {sid} with new GPA {gpa:.2f}"
            except Exception as e:
                return f"❌ Error: {str(e)}"

        update_btn.click(fn=handle_gpa_update, inputs=[update_id, update_gpa_val], outputs=update_output)


    with gr.Tab("📊 Reports"):
        report_output = gr.Textbox(label="Report Output", lines=10)

        avg_gpa_btn = gr.Button("📈 Avg GPA by Age")
        student_count_btn = gr.Button("👥 Student Count by Age")
        total_count_btn = gr.Button("🔢 Total Number of Students")

        def format_report(data, label1, label2):
            if not data:
                return "No data available."
            lines = [f"{label1:<10} | {label2}"]
            lines.append("-" * 25)
            for row in data:
                lines.append(f"{row[0]:<10} | {row[1]:.2f}" if isinstance(row[1], float) else f"{row[0]:<10} | {row[1]}")
            return "\n".join(lines)

        avg_gpa_btn.click(fn=lambda: format_report(student.avg_gpa_by_age(), "Age", "Avg GPA"), outputs=report_output)
        student_count_btn.click(fn=lambda: format_report(student.student_count_by_age(), "Age", "Count"), outputs=report_output)
        total_count_btn.click(fn=lambda: f"Total Students: {student.total_student_count()}", outputs=report_output)


if __name__ == "__main__":
    demo.launch()
#student databade.py

import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

# Set up the database and create the students table
bg_color = "#badc57"
def setup_database():
    conn = sqlite3.connect('student_records.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            marks INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Add a new student record
def add_student(name, age, marks):
    conn = sqlite3.connect('student_records.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, age, marks) VALUES (?, ?, ?)', (name, age, marks))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", f"Student '{name}' added successfully!")

# Display all student records
def display_students():
    conn = sqlite3.connect('student_records.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()

    if not students:
        messagebox.showinfo("Info", "No records found.")
    else:
        records = "\n".join([f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Marks: {student[3]}" for student in students])
        messagebox.showinfo("Student Records", records)

# Update an existing student record
def update_student(student_id, name, age, marks):
    conn = sqlite3.connect('student_records.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE students SET name=?, age=?, marks=? WHERE id=?', (name, age, marks, student_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", f"Student ID {student_id} updated successfully!")

# Delete a student record
def delete_student(student_id):
    conn = sqlite3.connect('student_records.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", f"Student ID {student_id} deleted successfully!")

# GUI Setup
def create_gui():
    root = tk.Tk()
    root.title("Student Records Management System")

    def on_add():
        name = simpledialog.askstring("Input", "Enter name:")
        age = simpledialog.askinteger("Input", "Enter age:")
        marks = simpledialog.askinteger("Input", "Enter marks:")
        if name and age is not None and marks is not None:
            add_student(name, age, marks)

    def on_display():
        display_students()

    def on_update():
        student_id = simpledialog.askinteger("Input", "Enter Student ID to update:")
        if student_id:
            name = simpledialog.askstring("Input", "Enter new name:")
            age = simpledialog.askinteger("Input", "Enter new age:")
            marks = simpledialog.askinteger("Input", "Enter new marks:")
            if name and age is not None and marks is not None:
                update_student(student_id, name, age, marks)

    def on_delete():
        student_id = simpledialog.askinteger("Input", "Enter Student ID to delete:")
        if student_id:
            delete_student(student_id)

    tk.Button(root, text="Add Student", command=on_add).pack(pady=10)
    tk.Button(root, text="Display Students", command=on_display).pack(pady=10)
    tk.Button(root, text="Update Student", command=on_update).pack(pady=10)
    tk.Button(root, text="Delete Student", command=on_delete).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    setup_database()
    root.mainloop()

if __name__ == "__main__":
    create_gui()
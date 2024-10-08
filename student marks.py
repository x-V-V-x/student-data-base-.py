#                                                 This code is only for single subject managment 
import sqlite3

# Set up the database and create the students table
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
    print(f"\nStudent '{name}' added successfully!")

# Display all student records
def display_students():
    conn = sqlite3.connect('student_records.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()

    print("\nStudent Records:")
    print("-" * 40)
    if not students:
        print("No records found.")
    else:
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Marks: {student[3]}")
    print("-" * 40)

# Update an existing student record
def update_student(student_id, name, age, marks):
    conn = sqlite3.connect('student_records.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE students SET name=?, age=?, marks=? WHERE id=?', (name, age, marks, student_id))
    conn.commit()
    conn.close()
    print(f"\nStudent ID {student_id} updated successfully!")

# Delete a student record
def delete_student(student_id):
    conn = sqlite3.connect('student_records.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
    conn.commit()
    conn.close()
    print(f"\nStudent ID {student_id} deleted successfully!")

# Main program loop
def main():
    setup_database()
    
    while True:
        print("\nStudent Records Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            marks = int(input("Enter marks: "))
            add_student(name, age, marks)
        
        elif choice == '2':
            display_students()
        
        elif choice == '3':
            student_id = int(input("Enter Student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            marks = int(input("Enter new marks: "))
            update_student(student_id, name, age, marks)
        
        elif choice == '4':
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)
        
        elif choice == '5':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

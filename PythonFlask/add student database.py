import sqlite3

def add_student():
    firstName = input("Enter the first name of the student: ")
    lastName = input("Enter the last name of the student: ")
    dob = input("Enter the date of birth of the student (YYYY-MM-DD): ")

    conn = sqlite3.connect('your_database_name.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO Student (firstName, lastName, dob) VALUES (?, ?, ?)", (firstName, lastName, dob))
        conn.commit()
        print("Student added successfully!")
    except sqlite3.Error as e:
        print("Error adding student:", e)
    finally:
        conn.close()

while True:
    choice = input("Enter 1 to add a new student to the database or 2 to exit: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        break
    else:
        print("Error: Invalid input. Please enter either '1' or '2'.")


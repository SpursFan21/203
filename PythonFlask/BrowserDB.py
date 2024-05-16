from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dbBrowser.jinja')

@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        dob = request.form['dob']

        try:
            conn = sqlite3.connect('Database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Student (firstName, lastName, dob) VALUES (?, ?, ?)", (firstName, lastName, dob))
            conn.commit()
            return "Student added successfully!"
        except sqlite3.Error as e:
            return f"Error adding student: {e}"
        finally:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(os.getcwd(), 'Database.db')
app.config["SECRET_KEY"] = "random string"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student1' 
    idNumber = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    
    def __init__(self, firstName, lastName, address, city):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city

@app.route("/")
def show_all():
    students = Student.query.all()
    return render_template("show_all.html", students=students)

@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        if not request.form["firstName"] or not request.form["lastName"] or \
           not request.form["address"] or not request.form["city"]:
            flash("Please enter all the fields", "error")
        else:
            studentmain = Student(request.form["firstName"],
                                  request.form["lastName"],
                                  request.form["address"],
                                  request.form["city"])
            db.session.add(studentmain)
            db.session.commit()
            
            flash("Record Inserted!")
            return redirect(url_for("show_all"))
        
    return render_template("new.html")

if __name__ == "__main__":
    app.run(debug=True)

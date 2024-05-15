from flask import Flask, redirect, url_for


app = Flask(__name__)

#127.0.0.1:5000/admin
@app.route("/admin")
def hello_admin():
    return "Hello Admin"

#127.0.0.1:5000/guest/rolf
@app.route("/guest/<guest>")
def hello_guest(guest):
    return f"Hello {guest} as a Guest"

#if 127.0.0.1:5000/user/admin was passed => redirect to #127.0.0.1:5000/admin
@app.route("/user/<name>")
def hello_user(name):
    if name =="admin":
        return redirect(url_for("hello_admin"))
    else:
        # if 127.0.0.1:5000/user/rouwa => redirect to 127.0.0.1:5000/guest/rouwa
        return redirect (url_for("hello_guest", guest = name))
    
if  __name__ == "__main__":
    app.run(debug = True) 
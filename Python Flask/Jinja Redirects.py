from flask import Flask, redirect, url_for, request, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("form.jinja")

@app.route("/")
def welcome(name):
    return f"welcome {name}"

@app.route("/")
def login():
    if request.method=="post":
        user=request.form["nm"]
        return redirect(url_for("welcome", name=user))
    else:
        user=request.args.get("nm")
        return redirect(url_for("welcome", name=user))
if __name__ == "__main__":
    app.run(debug=True)
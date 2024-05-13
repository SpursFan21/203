from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("setCookie.jinja")

@app.route("/setCookie", methods=["POST", "GET"])
def setCookie():
    if request.method=="POST":
        username = request.form["nm"]
        resp=make_response(render_template("readCookie.html"))
        resp.set_cookie("username", username)
        
        age = request.form["age"]
        resp.set_cookie("age", age)
        
        return resp
    
@app.route("/getCookie")
def getCookie():
    name = request.cookies.get("username")
    age = request.cookies.get("age")
    return f"Hello{name}, your age is {age}"

if __name__ == "__main__":
    app.run(debug=True)
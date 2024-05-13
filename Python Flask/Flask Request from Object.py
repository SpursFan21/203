from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def student():
    return render_template("student.jinja")

@app.route("/result", methods=["Post", "Get"])
def result():
    if request.method=="Post":
        result = request.form
        return render_template("result.html", result = result)
    
if __name__=="__main__":
    app.run(debug=True)
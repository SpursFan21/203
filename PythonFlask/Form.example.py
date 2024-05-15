from flask import Flask, render_template, request, flash, redirect, url_for
from Forms import ContactForm

app = Flask(__name__)
app.secret_key = "1234"

@app.route("/")
def index():
    return redirect(url_for("contact"))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if not form.validate():
            flash("All fields are required.")
            return render_template("Contact.jinja", form=form)
        else:
            return render_template("success.jinja", form=form)
    return render_template("Contact.jinja", form=form)

if __name__ == "__main__":
    app.run(debug=True)

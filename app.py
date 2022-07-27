from flask import Flask, render_template, request, flash

# creates a class for our app
app = Flask(__name__)

app.secret_key = "someKeyHere"

# specify last part of url
@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you")
    return render_template("index.html")
    


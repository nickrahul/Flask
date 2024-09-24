from flask import Flask,render_template,request,redirect,session
from db import Database
import api
import os


app = Flask(__name__)
dbo = Database()


secret_key = os.urandom(24)  # Generates a random 24-byte string
app.secret_key = secret_key


@app.route("/")
def index():
    return render_template("login.html")
    

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/perform_registration",methods=['post'])
def perform_registration():
    username = request.form.get("username")
    useremail = request.form.get("useremail")
    password = request.form.get("user_password")
    response = dbo.insert(username,useremail,password)
    if response:
        return render_template("login.html",message="Registration Succesful. Kindly login to proceed")
    else:
        return render_template("register.html",message="Email already exists.")
    

@app.route("/perform_login",methods=["post"])
def perform_login():
    email = request.form.get("email")
    passs = request.form.get("pass")
    response = dbo.search(email,passs)
    if response:
        session["logged_in"] = True
        return redirect("/profile")
    else:
        return render_template("login.html",message="Incorrect email/password")
    

@app.route("/profile")
def profile():
    if session.get("logged_in"):
        return render_template("profile.html")
    else:
        return redirect("/")

@app.route("/ner")
def ner():
    if session.get("logged_in"):
        return render_template("ner.html")
    else:
        return redirect("/")
    

@app.route("/perform_ner",methods=["post"])
def perform_ner():
    if session.get("logged_in"):
        text = request.form.get("ner_text")
        response = api.ner(text)
        return render_template("ner.html",response=response)
    else:
        return redirect("/")



app.run(debug=True)



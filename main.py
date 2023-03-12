from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)



@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")

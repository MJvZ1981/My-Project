from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        log = True
        users = [x for x in get_users()]
        user = request.form['username']
        if user not in users:
            log = False
        else:
            password = request.form['password']
            if hash_password(password) != get_users()[user]:
                log = False
        if log:
            session['username'] = user
            return render_template('dashboard.html')
        else:
            return redirect(url_for('index'))
    else:
        return render_template('login.html')


@app.route("/dashboard")
def dashboard():
    if 'username' in session:
        user = request.form['username']
        return render_template('dashboard.html' )
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout(): 
    session.pop('username', None)
    return redirect(url_for('index'))

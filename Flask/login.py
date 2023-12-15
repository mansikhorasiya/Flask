from flask import Flask, render_template, request

app = Flask(__name__)

Username = "Mansi"
Password = "Mansi123"


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    # if request.method == "post":
    un = request.form.get('username')
    pw = request.form.get('password')

    if un ==Username and pw== Password:
        return "Welcome {}".format(un)

    else:
        return "Invalid "


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

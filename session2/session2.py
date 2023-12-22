from flask import Flask,render_template,request,redirect,url_for,flash

app = Flask(__name__)
app.secret_key = 'helloooo'

users={}

@app.route('/')
def index():
    return render_template("register.html")

@app.route('/register',methods=["POST"])
def register():
        Firstname = request.form.get('firstname')
        Lastname = request.form.get('lastname')
        Username = request.form.get('username')
        Password = request.form.get('password')

        return render_template('login.html')


@app.route('/login',methods=["POST"])
def login():
    if request.method == 'POST':

        Username = request.form['username']
        Password = request.form['password']

        if(Username == 'username' and Password == 'password'):
            flash('logged in successfully')
            return  redirect(url_for('index'))
        else:
            flash('invalid')
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)



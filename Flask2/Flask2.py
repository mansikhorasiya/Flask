from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("app.html")


@app.route('/register', methods=['POST'])
def Register():
    if request.method == 'POST':
              Firstname = request.form.get('firstname')
              Lastname = request.form.get('lastname')
              Username = request.form.get('username')
              Password = request.form.get('password')
              Address =request.form.get('address')
              City=request.form.get('city')
              Gender =request.form.get('gender')
              hob=request.form.getlist('hobbies')
              hobbies=",".join(hob)
              return (f"First Name :{Firstname},<br>" 
                    f"Last Name :{Lastname}," f"<br>User Name:{Username},<br>Password :{Password},<br>Address :{Address},"
                     f"<br>City :{City},<br>Gender :{Gender},<br>Hobbies:{hobbies}")

if __name__ == '__main__':
    app.run()

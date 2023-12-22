from flask import Flask, render_template, request,redirect

app = Flask(__name__)

# fn=""
# ln=""

@app.route('/')
def index():
    return render_template("Session.html")

@app.route('/session', methods=['POST'])
def session():

    fn = request.form.get('fn')

    ln = request.form.get('ln')

    un =request.form.get('un')

    password =request.form.get('password')

    return (f'fn :{fn}<br><br>'
            f'ln : {ln}<br><br>'
            f'un :{un}<br><br>'
            f'password :{password}<br><br>'
            f'<a href="http://127.0.0.1:5000/session2?{fn}&{ln}">click me </a>')

@app.route('/Session')
def Session2():
    return  render_template('')
    # fn=request.args.get("fn")
    # ln=request.args.get("ln")
    #
    # return (f"fn:{fn},"
    #         f"ln:{ln}")

if __name__=="__main__":
    app.run(debug=True)




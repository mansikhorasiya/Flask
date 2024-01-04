from flask import Flask, request, render_template, redirect
import pymysql

app = Flask(__name__)


def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='rootroot',
        db='flask_demo',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


@app.route('/')
def index():
    return render_template('Register.html')


@app.route('/register', methods=['POST'])
def register():
    Firstname = request.form.get('firstname')
    Lastname = request.form.get('lastname')
    Username = request.form.get('username')
    Password = request.form.get('password')
    City = request.form.get('city')
    Gender = request.form.get('gender')
    hob = request.form.getlist('hobbies')
    hobbies = ",".join(hob)
    connection = get_db_connection()
    cursor1 = connection.cursor()

    cursor1.execute("insert into register_1(Firstname,Lastname,Username,"
                    "Password,City,Gender, "
                    "hobbies) values('{}','{}','{}','{}','{}','{}'," \
                    "'{}')".format(Firstname, Lastname, Username,
                                   Password, City, Gender, hobbies))

    connection.commit()
    cursor1.close()

    return redirect("/view")


@app.route('/view')
def view():
    connection = get_db_connection()
    cursor1 = connection.cursor()
    cursor1.execute("select * from register_1")
    data = cursor1.fetchall()
    print("Data>>>>", data)
    connection.commit()

    return render_template("View.html", item=data)

@app.route('/delete')
def delete():
    id = request.args.get("id")
    connection = get_db_connection()
    cursor1 = connection.cursor()
    cursor1.execute("DELETE FROM register_1 WHERE RegId='{}'".format(id))
    connection.commit()
    cursor1.close()
    return redirect("/view")


@app.route('/edit')
def edit():
    print("In")
    id = request.args.get("id")

    connection = get_db_connection()
    cursor1 = connection.cursor()
    cursor1.execute("Select * from register_1 WHERE RegId = {}".format(id))
    data=cursor1.fetchall()
    connection.commit()
    cursor1.close()

    return render_template("Edit.html",items=data)


@app.route('/update',methods=["post"])
def update():
    id = request.form.get("id")
    Firstname = request.form.get('firstname')
    Lastname = request.form.get('lastname')
    Username = request.form.get('username')
    Password = request.form.get('password')
    City = request.form.get('city')
    Gender = request.form.get('gender')
    hob= request.form.getlist('hobbies')
    hobbies = ",".join(hob)

    connection = get_db_connection()
    cursor1 = connection.cursor()

    cursor1.execute(f"update register_1 set Firstname='{Firstname}',Lastname='{Lastname}',Username='{Username}',Password='{Password}',City='{City}',Gender='{Gender}',hobbies='{hobbies}' where RegId='{id}'")
    connection.commit()
    cursor1.close()
    connection.close()
    # return redirect("View.html")
    return redirect("/view")


if __name__ == '__main__':
    app.run(debug=True)

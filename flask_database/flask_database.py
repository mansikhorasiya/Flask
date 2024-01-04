# pip install pymysql

import pymysql


def insertLogin():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='rootroot',
        db='flask_demo',
        port=3306

    )
    #
    # un = "aa"
    # pwd = "bb"
    # role = "cc"
    # status = "dd"

    cursor1 = connection.cursor()

    cursor1.execute(
        "insert into register(first_name,lats_name,user_name,pass_word) "
        "values('Mansi','khorasinsya','MK','maansi1234')"

        )
    connection.commit()



insertLogin()
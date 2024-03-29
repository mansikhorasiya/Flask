from base import app
from flask import render_template,request,redirect
from base.com.vo.category_vo import CategoryVo
from  base.com.dao.category_dao import CategoryDAO

# from base.com.vo import category_vo

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/add_category')
def add_category():
    return render_template('addCategory.html')

@app.route('/insert_category',methods=['POST'])
def insert_category():
    category_name=request.form.get('name')
    category_description=request.form.get('description')

    category_vo=CategoryVo()
    category_dao=CategoryDAO()

    category_vo.category_name=category_name
    category_vo.category_description =category_description

    category_dao.insert_category(category_vo)

    return redirect("/searchCategory")

@app.route("/searchCategory")
def searchCategory():
    category_dao=CategoryDAO()
    data=category_dao.search_category()
    print(data)
    return render_template('viewCategory.html',data=data)

@app.route("/delete_category")
def delete_category():
    category_id=request.args.get('category_id')
    category_vo=CategoryVo()
    category_vo.category_id=category_id
    category_dao = CategoryDAO()
    category_dao.delete_category(category_vo)
    return redirect('/searchCategory')

@app.route("/edit_category")
def edit_category():
    category_id = request.args.get('category_id')
    category_vo = CategoryVo()

    category_vo.category_id = category_id
    category_dao = CategoryDAO()

    data= category_dao.edit_category(category_vo)


    return render_template('edit.html',data=data)

@app.route("/update_category",methods=['Post'])
def update_category():
    category_name = request.form.get('name')
    category_description = request.form.get('description')
    category_id=request.form.get('id')

    category_vo=CategoryVo()
    category_vo.category_id=category_id
    category_vo.category_name=category_name
    category_vo.category_description=category_description


    category_dao=CategoryDAO()
    category_dao.update_category(category_vo)

    return redirect('/searchCategory')
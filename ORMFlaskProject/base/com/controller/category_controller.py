from base import app
from flask import render_template,request,redirect
from base.com.vo.category_vo import CategoryVo
from  base.com.dao.category_dao import CategoryDAO
    

# category_blueprint = Blueprint('category', __name__, url_prefix='/category')

@app.route('/')
def home():
    # Logic related to the category page
    return render_template("home.html")

@app.route("/add_category")
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

    return render_template('addCategory.html')

@app.route("/searchCategory")
def searchCategory():
    category_dao=CategoryDAO()
    data=category_dao.search_category()
    print(data)
    return render_template('viewCategory.html',data=data)
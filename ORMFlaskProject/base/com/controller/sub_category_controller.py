from base import app
from flask import render_template,request,redirect
from base.com.vo.subcategory_vo import SubCategoryVo
from base.com.dao.subcategory_dao import SubCategoryDao
from base.com.dao.category_dao import CategoryDAO

@app.route('/load_subcategory')
def load_subcategory():
    category_dao=CategoryDAO
    data=category_dao.search_category()
    return render_template('addSubCategory',data=data)

@app.route('/addSubCategory',methods=['Post'])
def add_subcategory():
    subcategory_name=request.form.get('subcategory_name')
    subcategory_description=request.form.get('subcategory_description')
    subcategory_category_id=request.form.get('category_id')

    subcategory_vo = SubCategoryVo()
    subcategory_vo.subcategory_category_id = subcategory_category_id
    subcategory_vo.sub_category_name = subcategory_name
    subcategory_vo.sub_category_description = subcategory_description
    print(subcategory_name)
    subcategory_dao = SubCategoryDao()
    subcategory_dao.insert_subcategory(subcategory_vo)

    return redirect('load_subcategory')
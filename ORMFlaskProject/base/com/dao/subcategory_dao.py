from base import db
from base.com.vo.subcategory_vo import SubCategoryVo

class SubCategoryDao():
    def insert_subcategory(self,subcategory_vo):
        db.session.add(subcategory_vo)
        db.session.commit()
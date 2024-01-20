from base import db
from base.com.vo.category_vo import CategoryVo

class CategoryDAO:
    def insert_category(self,category_vo):
        db.session.add(category_vo)
        db.session.commit()
        
    def search_category(self):
        query=db.session.query(CategoryVo).all()
        db.session.commit()
        return  query
    
    def delete_category(self,category_vo):
        data=CategoryVo.query.get(category_vo.category_id)
        db.session.delete(data)
        db.session.commit()
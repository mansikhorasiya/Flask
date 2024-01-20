from  base import  db,app

class CategoryVo(db.Model):
    def __init__(self):
        with app.app_context():
            db.create_all()

    __tablename__ ='category_table'
    category_id=db.Column('category_id',db.Integer,primary_key=True,
                          autoincrement=True)
    category_name =db.Column('category_name',db.String(255),nullable=False)

    category_description=db.Column('category_description',db.Text,nullable=False)

    def as_dict(self):
        return {
            'category_id':self.category_id,
            'category_name':self.category_name,
            'category_description':self.category_description,
        }


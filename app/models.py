from app import db, app
from sqlalchemy import Column, Integer, String, Float


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

# class Product(db.Model):
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False, unique=True)
#     price = Column(Float, default=0)
#     image = Column(String(100))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

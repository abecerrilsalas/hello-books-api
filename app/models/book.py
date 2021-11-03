from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

#below is example from class
# class Dog(db.Model):
#     __tablename__='dogs'
#     breed=db.Column(db.Integer, primary_key=True, autoincrement=True)
#     age=db.Column(db.Integer)
#     name=db.Column(db.String(64))

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data.db')
connection = engine.connect()
 
db =SQLAlchemy()
 
class StudentModel(db.Model):
    __tablename__ = "students"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    branch = db.Column(db.String())
    batch = db.Column(db.String())
    email = db.Column(db.String())
    dob = db.Column(db.String())
    
    def __init__(self, name,branch,batch,email,dob):
        self.name = name
        self.branch = branch
        self.batch = batch
        self.email = email
        self.dob = dob
        
 
    def __repr__(self):
        return f"{self.name}:{self.branch}"
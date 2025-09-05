print('models_file')
from swish_app import db

class UsersTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique= True, nullable=False)
    salary = db.Column(db.Float, nullable=False )

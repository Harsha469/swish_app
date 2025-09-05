from swish_app import app,db
from swish_app import views
from swish_app.models import  UsersTable
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
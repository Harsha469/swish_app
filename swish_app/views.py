print('views_file')
from swish_app import app,db
from flask import render_template, jsonify,request
from swish_app.models import UsersTable

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/profile/<int:id>', methods = ['GET'])
def profile(id):
    return jsonify(msg = f'the id is {id}')

@app.route('/query_params')
def query_params():
    data= request.args.to_dict()
    cols = {col.name: getattr(UsersTable,col.name) for col in UsersTable.__table__.columns if not col.primary_key}
    query = UsersTable.query
    for key,value in data.items():
        if key in cols:
            query = query.filter(cols[key] == value)
    users = query.all()
    if not users:
        return jsonify(msg = 'no data')
    results = []
    for u in users:
        results.append({'id':u.id, 'name':u.name, 'price':u.price})
    return jsonify(msg = results)

@app.route('/new')
def new_one():
    return 'hello'
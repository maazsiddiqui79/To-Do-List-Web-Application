from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static',
    instance_path='/tmp'          # writable on Vercel
)

# ✅ PostgreSQL SQLAlchemy connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://go_todo_database_user:xcb0mg7xwZO3O5G6t8hwYy8O1XghwNGB@dpg-d1pan9mr433s73d6r1jg-a.oregon-postgres.render.com/go_todo_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    year = str(datetime.utcnow()).split('-')[0]
    date = db.Column(db.DateTime, default=year)

class DeletedTodo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    year = str(datetime.utcnow()).split('-')[0]
    date = db.Column(db.DateTime, default=year)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        if title and desc:
            to_do = Todo(title=title, content=desc)
            db.session.add(to_do)
            db.session.commit()
            return redirect(url_for('home'))
    all_todo = Todo.query.all()
    del_all_todo = DeletedTodo.query.all()
    return render_template('index.html', all_todo=all_todo, deltodo=del_all_todo)

@app.route('/done/<int:id>', methods=['POST', 'GET'])
def done(id):
    user_to_delete = db.session.query(Todo).filter_by(sno=id).first()
    if user_to_delete:
        deleted_entry = DeletedTodo(
            sno=user_to_delete.sno,
            title=user_to_delete.title,
            content=user_to_delete.content
        )
        db.session.add(deleted_entry)
        db.session.delete(user_to_delete)
        db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        user_to_update = Todo.query.filter_by(sno=id).first()
        user_to_update.title = title
        user_to_update.content = desc
        db.session.commit()
        return redirect('/')
    user_to_update = Todo.query.filter_by(sno=id).first()
    return render_template('update.html', todo=user_to_update)

@app.route('/deldone/<int:id>', methods=['POST', 'GET'])
def deldone(id):
    user_to_delete = db.session.query(DeletedTodo).filter_by(sno=id).first()
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
    return redirect('/')

@app.route('/clear', methods=['POST', 'GET'])
def clear():
    db.drop_all()
    db.create_all()
    return redirect(url_for('home'))

@app.route('/Profile')
def maaz():
    return render_template('connect.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

# Create database tables if they don't exist (runs once)
with app.app_context():
    db.create_all()               # runs once per cold‑start

# Local development only
if __name__ == '__main__':
    app.run(debug=True)

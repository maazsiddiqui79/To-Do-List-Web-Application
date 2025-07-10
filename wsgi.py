from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
if __name__ == '__main__':
    app.run(debug=True, port=4570)
    with app.app_context():
        db.create_all()
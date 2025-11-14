from flask import Flask, render_template     # flask library import garako. Flask app banaucha and HTML pages render garna help garcha
from flask_sqlalchemy import SQLAlchemy      # SQLAlchemy import gareko. Database access garna like MySQL/SQLite use garincha
from datetime import datetime                # current date/time handle garna datetime import gareko

# Flask app banako
first = Flask(__name__)                      # index file banako. __name__ tells Flask where to find files, routes, templates etc.

# Database configuration
first.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do.db'  # SQLite database ko file link deko
first.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False          # tracking off gareko (optional, performance ko lagi)

db = SQLAlchemy(first)                        # SQLAlchemy object create gareko, Flask app sanga link gareko

# Table/model banako
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary key, auto-increment garera unique banaune
    title = db.Column(db.String(100), nullable=False)                  # task title. nullable=False bhaye empty value allow hudaina
    content = db.Column(db.String(500), nullable=False)                # task content/description. same as above
    date = db.Column(db.DateTime, default=datetime.utcnow)             # default current date/time automatically set huncha

    def __repr__(self) -> str:                                         # object print garda k output aauxa vanera define gareko
        return f"{self.sno}: {self.title}"                             # example: 1: Buy groceries

# Flask routes
@first.route('/')          # '/' vaneko home page ko URL
def helloworld():           # function banako, page visit garda execute huncha
    from datetime import datetime

    # Warning: yo manually sno=1 haleko xa, future ma UNIQUE constraint fail huncha
    to_do = Todo(
        title="hello",
        content="hello what are you doing",
        # date automatic set huncha default value le
    )
    db.session.add(to_do)   # database ma add garna session ma rakheko
    db.session.commit()     # database ma commit gareko (save gareko)

    allTodo = Todo.query.all()  # fetch all todo records
    return render_template('index.html', allTodo=allTodo)
  # index.html render garne
    return 'Hello, this is my first Flask program!'     # yo second return reachable hudaina, hataunu parcha

@first.route('/about')       # about page ko route
def about():
    return 'aasari aarko page ma jana sakinxa '   # simple string return garera test gareko

@first.route('/hello1')      # hello1 page ko route
def hello1():
    return render_template('hello1.html')  # HTML page render garna
@first.route('/show')
def show():
    allTodo=Todo.query.all()
    print(allTodo )
    return "this is about page"

# App run garne
if __name__ == "__main__":        # directly execute garda code run hos ko lagi
    first.run(debug=True)          # debug=True bhaye error haru terminal ma dekhiyos

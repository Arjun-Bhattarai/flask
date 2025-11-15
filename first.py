from flask import Flask, render_template, request, redirect    # flask library import garako. Flask app banaucha and HTML pages render garna help garcha
from flask_sqlalchemy import SQLAlchemy               # SQLAlchemy import gareko. Database access garna like MySQL/SQLite use garincha
from datetime import datetime                         # current date/time handle garna datetime import gareko

# Flask app banako
first = Flask(__name__)                               # index file banako. __name__ tells Flask where to find files, routes, templates etc.

# Database configuration
first.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do.db'      # SQLite database ko file link deko
first.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False              # tracking off gareko (optional, performance ko lagi)

db = SQLAlchemy(first)                                 # SQLAlchemy object create gareko, Flask app sanga link gareko

# Table/model banako
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary key, auto-increment garera unique banaune
    title = db.Column(db.String(100), nullable=False)                  # task title. nullable=False bhaye empty value allow hudaina
    content = db.Column(db.String(500), nullable=False)                # task content/description. same as above
    date = db.Column(db.DateTime, default=datetime.utcnow)             # default current date/time automatically set huncha

    def __repr__(self) -> str:                                         # object print garda k output aauxa vanera define gareko
        return f"{self.sno}: {self.title}"                             # example: 1: Buy groceries


# ------------------------- HOME PAGE (SHOW + ADD TODOS) -------------------------
@first.route('/', methods=['GET', 'POST'])          # '/' vaneko home page ko URL
def helloworld():                                    # function banako, page visit garda execute huncha
    
    if request.method == 'POST':                     # form submit bhayo bhane POST method execute huncha
        title = request.form.get('title')            # form bata title lincha
        content = request.form.get('content')        # form bata content lincha
        print(title, content)

        to_do = Todo(title=title, content=content)   # naya todo object banako
        db.session.add(to_do)                        # database ma add garna session ma rakheko
        db.session.commit()                          # database ma commit gareko (save gareko)

    allTodo = Todo.query.all()                       # fetch all todo records
    return render_template('index.html', allTodo=allTodo)   # index.html render garne


# ------------------------- ABOUT PAGE -------------------------
@first.route('/about')                               # about page ko route
def about():
    return 'aasari aarko page ma jana sakinxa '      # simple string return garera test gareko


# ------------------------- HELLO1 PAGE -------------------------
@first.route('/hello1')                              # hello1 page ko route
def hello1():
    return render_template('hello1.html')            # HTML page render garna


# ------------------------- SHOW (DEBUG ONLY) -------------------------
@first.route('/show')
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return "this is about page"


# ------------------------- UPDATE PAGE -------------------------
@first.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    to_do = Todo.query.filter_by(sno=sno).first()    # particular task fetch gareko

    if request.method == 'POST':                     # update form submit bhayo bhane
        to_do.title = request.form.get('title')      # updated title
        to_do.content = request.form.get('content')  # updated content
        db.session.commit()                          # save changes
        return redirect('/')                         # home page ma redirect

    # GET request bhaye update.html render garne
    return render_template('update.html', to_do=to_do)


# ------------------------- DELETE TODO -------------------------
@first.route('/delete/<int:sno>')
def delete(sno):
    to_do = Todo.query.filter_by(sno=sno).first()    # particular task find gareko
    db.session.delete(to_do)                         # delete gareko
    db.session.commit()                              # save change
    return redirect('/')                             # home ma redirect


# ------------------------- RUN APP -------------------------
if __name__ == "__main__":
    first.run(debug=True)                            # debug mode on rakheko

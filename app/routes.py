from flask import Blueprint, render_template, request, redirect
from .models import Todo
from . import db

# Blueprint banako routes modular banauna
main = Blueprint('main', __name__)

# Home page route (GET & POST)
@main.route('/', methods=['GET', 'POST'])
def helloworld():
    error = None  # error message for validation

    # form submit bhayo bhane POST method execute huncha
    if request.method == 'POST':
        title = request.form.get('title').strip()       # form bata title lincha, extra spaces remove garna
        content = request.form.get('content').strip()   # form bata content lincha, extra spaces remove garna

        # use forms for validation
        if not title or not content:
            error = 'Title or content cannot be empty'  # validation message
        else:
            print(title, content)
            to_do = Todo(title=title, content=content)   # naya todo object banako
            db.session.add(to_do)                        # database ma add garna session ma rakheko
            db.session.commit()                          # database ma commit gareko
            return redirect('/')                         # successfully add bhaye home ma redirect

    allTodo = Todo.query.all()                            # fetch all todo records
    return render_template('index.html', allTodo=allTodo, error=error)   # index.html render garne

# About page ko route
@main.route('/about')                               
def about():
    return 'aasari aarko page ma jana sakinxa '      # simple string return garera test gareko

# Hello1 page route
@main.route('/hello1')                              
def hello1():
    return render_template('hello1.html')            # HTML page render garna

# Show all todos (test/debug)
@main.route('/show')
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return "this is about page"

# Update route with GET & POST
@main.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    to_do = Todo.query.filter_by(sno=sno).first()    # particular task fetch gareko

    if request.method == 'POST':                     # update form submit bhayo bhane
        to_do.title = request.form.get('title')      # updated title
        to_do.content = request.form.get('content')  # updated content
        db.session.commit()                          # save changes
        return redirect('/')                         # home page ma redirect

    # GET request bhaye update.html render garne
    return render_template('update.html', to_do=to_do)

# Delete route
@main.route('/delete/<int:sno>')
def delete(sno):
    to_do = Todo.query.filter_by(sno=sno).first()    # particular task find gareko
    db.session.delete(to_do)                         # delete gareko
    db.session.commit()                              # save change
    return redirect('/')                             # home ma redirect

from flask import Flask, render_template, request, redirect      # flask library import gareko. HTML render garna and redirect garna help garcha
from flask_sqlalchemy import SQLAlchemy                         # SQLAlchemy import gareko. Database ko lagi.
from datetime import datetime                                   # date and time store garna import

first = Flask(__name__)                                         # Flask app banako

# Database ko path define
first.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do.db'  # Database location define gareko
first.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False          # Extra warning hataune

db = SQLAlchemy(first)                                          # Database instance banako


# Database ko table banako
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Serial number -> primary key
    title = db.Column(db.String(100), nullable=False)                  # Todo title
    content = db.Column(db.String(500), nullable=False)                # Todo description
    date = db.Column(db.DateTime, default=datetime.utcnow)             # Date automatically add huncha

    def __repr__(self) -> str:
        return f"{self.sno}: {self.title}"


# HOME PAGE → SHOW + ADD TODOS
@first.route('/', methods=['GET', 'POST'])
def helloworld():

    # POST request aayo vaney form ko data database ma save garne
    if request.method == 'POST':
        title = request.form.get('title')          # form bata title liyo
        content = request.form.get('content')      # form bata description liyo

        to_do = Todo(title=title, content=content) # database ko object banako
        db.session.add(to_do)                      # database ma add gareko
        db.session.commit()                        # save garne

    allTodo = Todo.query.all()                     # database bata sabai todo fetch gareko
    return render_template('index.html', allTodo=allTodo)   # index.html ma pathaune



# UPDATE PAGE → BOTH GET + POST
@first.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    to_do = Todo.query.filter_by(sno=sno).first()  # jun todo click gareko tesko data liyeko

    # Form submit bhayo vane update garne
    if request.method == 'POST':
        to_do.title = request.form.get('title')    # naya title
        to_do.content = request.form.get('content')# naya description
        db.session.commit()                        # database update
        return redirect('/')                       # redirect back to home

    return render_template('update.html', to_do=to_do)  # update page kholne



# DELETE
@first.route('/delete/<int:sno>')
def delete(sno):
    to_do = Todo.query.filter_by(sno=sno).first()  # delete garne task find gareko
    db.session.delete(to_do)                       # delete gareko
    db.session.commit()                            # database ma save
    return redirect('/')                           # home ma pathaune


if __name__ == "__main__":
    first.run(debug=True)                          # Flask app run garne

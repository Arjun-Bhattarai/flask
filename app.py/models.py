from . import db
from datetime import datetime

# Table/model banako
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary key, auto-increment garera unique banaune
    title = db.Column(db.String(100), nullable=False)                  # task title. nullable=False bhaye empty value allow hudaina
    content = db.Column(db.String(500), nullable=False)                # task content/description. same as above
    date = db.Column(db.DateTime, default=datetime.utcnow)             # default current date/time automatically set huncha

    def __repr__(self) -> str:                                         # object print garda k output aauxa vanera define gareko
        return f"{self.sno}: {self.title}"                             # example: 1: Buy groceries

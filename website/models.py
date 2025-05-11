from .import db
from datetime import datetime

class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(150),nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

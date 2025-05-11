from flask import Blueprint, render_template, redirect, request, url_for
from .models import Task
from . import db

views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        task_content=request.form['content']
        new_task=Task(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
        
    tasks=Task.query.order_by(Task.date_created).all()
    return render_template('index.html',tasks=tasks)

@views.route('/delete/<int:task_id>')
def delete(task_id):
    task_to_delete=Task.query.get_or_404(task_id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Delete unsuccessful'
        
@views.route('/edit/<int:task_id>',methods=['POST','GET'])
def update(task_id):
    task=Task.query.get_or_404(task_id)

    if request.method=='POST':
        task.content=request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Error during update'
        
    return render_template('edit.html',task=task)
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db.init_app(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self):
        return f"{self.sno} - {self.title}"

with app.app_context():
    db.create_all()

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == 'POST':
        # print("POST method detected!")
        title = request.form['title']
        description = request.form['description']
        todo = Todo(title=title, description=description)
        print("The post title is {}".format(title))
        print("The post description is {}".format(description))
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    print(allTodo)  
    return render_template("index.html", allTodo=allTodo)
    # return render_template("index.html")

@app.route('/home')
def home_hello_world():
    return render_template("index.html")

@app.route('/show')
def show_todos():
    allTodo = Todo.query.all()
    print(allTodo)  
    return render_template("index.html", allTodo=allTodo)
    # return "This is the show page"

@app.route('/about')
def about():
    # return 'Hello, World!'
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/update/<int:sno>', methods = ['GET', 'POST'])
def update(sno):
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description'] 
        todo = Todo.query.filter_by(sno=sno).first() 
        todo.title = title
        todo.description = description
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todo=todo)
    # return 'Hello, World!'
    # return render_template("about.html")

@app.route('/delete/<int:sno>')
def delete(sno):
    # return 'Hello, World!'
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route('/pricing')
def pricing():
    return render_template("pricing.html")

if __name__ == "__main__":
    app.run(debug=True)
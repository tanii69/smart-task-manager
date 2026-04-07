from flask_cors import CORS
from ai_service import suggest_priority
from flask import request, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Task

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db.init_app(app)
CORS(app)

@app.route('/')
def home():
    return "Backend Running Successfully with DB!"

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json

    # validation
    if not data.get('title'):
        return {"error": "Title is required"}, 400

    # create task
    priority = suggest_priority(data['title'])
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        priority=priority,
        category=data.get('category', 'General')
    )
    db.session.add(task)
    db.session.commit()

    return {"message": "Task created successfully", "task": task.to_dict()}, 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    result = [task.to_dict() for task in tasks]
    return jsonify(result)

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)

    if not task:
        return {"error": "Task not found"}, 404

    db.session.delete(task)
    db.session.commit()

    return {"message": "Task deleted successfully"}

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    
    if not task:
        return {"error": "Task not found"}, 404
    
    data = request.json
    
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'priority' in data:
        task.priority = data['priority']
    if 'category' in data:
        task.category = data['category']
    if 'completed' in data:
        task.completed = data['completed']
    
    db.session.commit()
    
    return {"message": "Task updated successfully", "task": task.to_dict()}

# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
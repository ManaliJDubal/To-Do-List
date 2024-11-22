from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for to-do items
todo_list = []

@app.route('/')
def index():
    """Display the to-do list."""
    return render_template('index.html', todos=todo_list)

@app.route('/add', methods=['POST'])
def add_todo():
    """Add a new item to the to-do list."""
    task = request.form.get('task')
    if task:  # Only add non-empty tasks
        todo_list.append({'task': task, 'done': False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    """Toggle the completion status of a task."""
    if 0 <= task_id < len(todo_list):  # Ensure valid task ID
        todo_list[task_id]['done'] = not todo_list[task_id]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Delete a task from the to-do list."""
    if 0 <= task_id < len(todo_list):  # Ensure valid task ID
        todo_list.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=8081)

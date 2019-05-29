from flask import Flask,jsonify,abort,make_response,request


app = Flask(__name__)

"""
DATA: tasks 模拟数据

"""
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


"""
ROUTE   for  tasks
"""

# @app.route('/api/tasks/', methods=['GET'])
# def index_page():
#     return jsonify({'tasks': tasks})


@app.route('/api/tasks/', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # filter()   返回可迭代对象 需要转换成list
    task = filter(lambda t: t['id'] == task_id,tasks)
    task = list(task)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


# 更新
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    task = list(task)
    if len(task) == 0:
        abort(404)
    # 请求不带data 返回400
    if not request.json:
        abort(400)
    # unicode
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    # 前面做了 task 的赋值
    # 更新了 task[0] （由于id是唯一的 就是说task中只有一个对象
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    task = list(task)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


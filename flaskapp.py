#!flask/bin/python
from flask import Flask, jsonify, abort


app = Flask(__name__)

heroes = {
    1: {
        'name': 'Lady Deathstrike', 'place': 'Osaka, Japan'
    },
    2: {
        'name': 'Absorbing Man', 'place': 'New York City, New York'
    }
}

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/heroes/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        return jsonify({'task': heroes[task_id]})
    except KeyError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
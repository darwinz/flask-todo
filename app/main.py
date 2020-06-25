from flask import Flask
from flask_restful import Api

from app.controllers.task_controller import TaskController

app = Flask(__name__)
api = Api(app)

api.add_resource(TaskController, '/')

if __name__ == '__main__':
    app.run(debug=True)

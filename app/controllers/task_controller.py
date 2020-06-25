from flask_restful import Resource


class TaskController(Resource):
    def get(self):
        return {'tasks': [{'id': 1, 'name': 'Test', 'description': 'Test'}]}

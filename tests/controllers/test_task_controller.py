from unittest import TestCase

from app.controllers.task_controller import TaskController


class TestTaskController(TestCase):
    def setUp(self):
        self.controller = TaskController()

    def test_get(self):
        subject = self.controller.get()
        self.assertEqual({'tasks': [{'id': 1, 'name': 'Test', 'description': 'Test'}]}, subject)

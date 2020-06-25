class Task:
    def __init__(self, name, description, user_id):
        self.id = None
        self.name = name
        self.description = description
        self.user_id = user_id
        self.complete = False

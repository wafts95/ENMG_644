from datetime import date

class Task:

    def __init__(self, name, effort, developer, start, status, end):
        self.name = name
        self.effort = effort
        self.developer = developer
        self.start = start
        self.end = end
        self.status = status

    def update_status(self, newStatus):
        self.status = newStatus
        if(newStatus == 'Completed'):
            self.end = date.today()

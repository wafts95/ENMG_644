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
    
    def print_details(self):
        print('\n'
              'Task name:\t\t%s\n'
              'Task effort:\t\t%s\n'
              'Assigned developer:\t%s\n'
              'Completion status:\t%s\n'
              'Task start:\t\t%s\n'
              'Task end:\t\t%s\n'
              % (self.name,
              self.effort,
              self.developer.name,
              self.status,
              (self.start if self.start else 'N/A'),
              (self.end if self.end else 'N/A')))

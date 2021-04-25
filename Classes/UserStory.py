class UserStory:
    def __init__(self, name, size):
        self.name = name
        self.tasks = []
        self.effort = 0
        self.status = 'Open'
        self.size = size

    def print_itr(self):
        print("Name : " + self.name)

    def update_effort(self):
        res = 0
        for task in self.tasks:
            res += task.effort
        self.effort = res

    def update_status(self):
        task_status = [task.status for task in self.tasks]
        if('In Progress' in task_status):
            self.status = 'In Progress'
        elif(all(elem == 'Completed' for elem in task_status)):
            self.status = 'Completed'
        else:
            self.status = 'Open'

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, taskName):
        newList= []
        for item in self.tasks:
            if item.name != taskName:
                newList.append(item)
        self.tasks = newList

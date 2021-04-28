class UserStory:
    def __init__(self, name, size):
        self.name = name
        self.tasks = []
        self.effort = 0
        self.status = 'Open'
        self.size = size

    def print_itr(self):
        print("Name : " + self.name)

    def print_details(self):
        self.update_effort()
        self.update_status()
        print('\n'
              'User Story name:\t%s\n'
              'Number of Tasks:\t%s\n'
              'User Story effort:\t%s\n'
              'Completion status:\t%s\n'
              'User Story size:\t%s\n'
              % (self.name,
              len(self.tasks),
              self.effort,
              self.status,
              self.size))

    def print_tasks(self):
        print('\nRegistered Tasks are:\n')
        for index, task in enumerate(self.tasks):
            print('\t' + str(index+1) + '- ' + task.name)

    def update_effort(self):
        res = 0
        for task in self.tasks:
            res += task.effort
        self.effort = res

    def update_status(self):
        task_status = [task.status for task in self.tasks]
        if('In Progress' in task_status or 'Completed' in task_status):
            self.status = 'In Progress'
        else:
            self.status = 'Open'

        if(all(elem == 'Completed' for elem in task_status)):
            self.status = 'Completed'

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, taskName):
        newList= []
        for item in self.tasks:
            if item.name != taskName:
                newList.append(item)
        self.tasks = newList

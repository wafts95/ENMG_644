from matplotlib import pyplot as plt
from datetime import timedelta, date

class Iteration:

    def __init__(self, name, duration, start, developers):
        self.name = name
        self.duration = duration
        self.start = start
        self.developers = developers
        self.userStories = []

    def delete_userStory(self, storyName):
        newList= []
        for item in self.userStories:
            if item.name != storyName:
                newList.append(item)
        self.userStories = newList

    def add_story(self, story):
        self.userStories.append(story)


    def print_report(self):
        # US classification
        backlog = []
        progress = []
        completed = []
        # Task classification
        openTask = []
        progressTask = []
        completedTask = []

        for story in self.userStories:
            story.update_status()
            story.update_effort()
            if story.status == 'Completed':
                completed.append(story)
            elif(story.status == 'Open'):
                backlog.append(story)
            else:
                progress.append(story)

        velocity = 0
        for story in completed:
            velocity += int(story.size)

        print('\n')
        print('Iteration:\t'+self.name)
        print('Duration:\t'+str(self.duration) +' days')
        print('Start Date:\t'+self.start.strftime('%d/%m/%Y'))
        print('Velocity:\t'+str(velocity))
        print('\n')
        print('User Story Backlog:')
        for item in backlog:
            print(item.name)
            for task in item.tasks:
                print('\t'+task.name+'\t\t-\t'+task.developer.name)
        print('\n')


        print('User Story In progress:')
        for item in progress:
            print(item.name)
            # Classify Tasks
            for task in item.tasks:
                if task.status == 'Completed':
                    completedTask.append(task)
                elif(task.status == 'In Progress'):
                    progressTask.append(task)
                else:
                    openTask.append(task)

            # Print Tasks
            print('\n\tTasks Open')
            for task in openTask:
                print('\t'+task.name+'\t\t-\t'+task.developer.name)
            print('\n\tTasks in progress')
            for task in progressTask:
                print('\t'+task.name+'\t\t-\t'+task.developer.name)
            print('\n\tTasks completed')
            for task in completedTask:
                print('\t'+task.name+'\t\t-\t'+task.developer.name)
        print('\n')
        print('User Story Completed:')
        for item in completed:
            print(item.name)
            for task in item.tasks:
                print('\t'+task.name+'\t\t-\t'+task.developer.name)
        print('\n')
        max_effort = 0
        for story in self.userStories:
            max_effort += story.effort

        plt.style.use("fivethirtyeight")
        # Plot the control line
        control_x = []
        control_y = []
        axis=[]
        for i in range(0,int(self.duration) + 1):
            axis.append(i)
            control_x.append(i)
            control_y.append((-max_effort/int(self.duration))*i+max_effort)
        ideal, = plt.plot(control_x,control_y, label="Ideal")

        # plot the progress
        max_x = int((date.today() - self.start).days)
        if(max_x > int(self.duration)):
            max_x = int(self.duration)

        curve_x = []
        curve_y = []
        start_effort = max_effort

        for i in range(0, max_x + 1):
            curve_x.append(i)
            curr_date = self.start + timedelta(days = i)
            curr_effort = 0
            for story in self.userStories:
                for task in story.tasks:
                    if(task.end == curr_date):
                        curr_effort += task.effort
            start_effort = start_effort - curr_effort
            curve_y.append(start_effort)
        actual, = plt.plot(curve_x, curve_y, label="Actual")
        plt.legend(handles=[ideal, actual])
        plt.xticks(axis)
        plt.xlabel("Duration")
        plt.ylabel("Effort")
        plt.title("Burn-down Chart")
        plt.show()

from Classes.Iteration import Iteration
from Classes.UserStory import UserStory
from Classes.Task import Task
from Classes.Developer import Developer
from utils import get_obj_by_name
import datetime
import pandas as pd

def init():
  print('\nInitializing application...\n')
  # Load Developers
  users = []
  df = pd.read_excel('./Database/user.xlsx', dtype=str)
  df = df.fillna('')
  for i in range(0, len(df)):
    row = df.iloc[i]
    users.append(Developer(row['name']))

  # Load Itr without the users stories
  itrs = []
  df = pd.read_excel('./Database/Iteration.xlsx', dtype=str)
  df = df.fillna('')
  for i in range(0, len(df)):
    row = df.iloc[i]
    temp = row['developers'].split('-')
    devs = []
    for item in temp:
      devs.append(get_obj_by_name(item, users))
    itrs.append(Iteration(row['name'], row['duration'], datetime.datetime.strptime(row['start date'], "%d/%m/%Y").date(), devs))

  # Load User Stories without Tasks
  stories = []
  df = pd.read_excel('./Database/userStory.xlsx', dtype=str)
  df =df.fillna('')
  for i in range(0, len(df)):
    row = df.iloc[i]
    temp_itr = get_obj_by_name(row['iteration'], itrs)
    stories.append(UserStory(row['name'], row['size']))
    temp_itr.add_story(stories[-1])

# load all tasks and assign them to stories
  tasks = []
  df = pd.read_excel('./Database/task.xlsx')
  df = df.fillna('')
  for i in range(0, len(df)):
    row = df.iloc[i]
    temp_story = get_obj_by_name(row['user story'], stories)
    temp_developer = get_obj_by_name(row['developer'], users)
    end = ''
    if row['end']:
      end = datetime.datetime.strptime(row['end'], "%d/%m/%Y").date()
    tasks.append(Task(row['name'], row['effort'], temp_developer,   datetime.datetime.strptime(row['start'], "%d/%m/%Y").date(), row['status'], end))
    temp_story.add_task(tasks[-1])
  print('\nApplication Loaded Successfully!\n')
  return {'users' : users, 'iterations' : itrs}

def save(users, iterations):
  print('\nSaving Data...\n')
  listUsers = []
  listTasks = []
  listItrations = []
  listUserStories = []
  for user in users:
    listUsers.append({'name': user.name})

  for iteration in iterations:
    temp = ''
    for dev in iteration.developers:
      temp += dev.name +'-'
    temp = temp[:-1]
    listItrations.append({'name' : iteration.name, 'duration' : iteration.duration, 'start date' : iteration.start.strftime('%d/%m/%Y'), 'developers' : temp})
    for story in iteration.userStories:
      listUserStories.append({'name' : story.name, 'size' : story.size, 'iteration' : iteration.name})
      for task in story.tasks:
        end = ''
        if(task.end):
          end = task.end.strftime('%d/%m/%Y')
        listTasks.append({'name' : task.name, 'effort' : task.effort, 'start' : task.start.strftime('%d/%m/%Y'), 'end' : end, 'developer' : task.developer.name, 'user story' : story.name, 'status' : task.status})
  # Over Write DB files
  pd.DataFrame(listUsers, columns = ['name']).to_excel('./Database/user.xlsx', index=None)
  pd.DataFrame(listTasks, columns = ['name', 'effort', 'start', 'end', 'developer', 'user story', 'status']).to_excel('./Database/task.xlsx', index=None)
  pd.DataFrame(listUserStories, columns = ['name', 'size', 'iteration']).to_excel('./Database/userStory.xlsx', index=None)
  pd.DataFrame(listItrations, columns = ['name', 'duration', 'start date', 'developers']).to_excel('./Database/Iteration.xlsx', index=None)
  print('\nData has been saved successfully!\n')

from Classes.Iteration import Iteration
from Classes.UserStory import UserStory
from Classes.Task import Task
from Classes.Developer import Developer
from initializer import init, save
from utils import get_obj_by_name
import datetime

users = []
iterations = []
role = None
res = init()
users = res['users']
iterations = res['iterations']
session_user = None
curr_opp=''

while not role:
  print('\nPlease Select a Role:\n1- Scrum Master\n2- Developer\n')
  role_key = int(input('Selection: '))
  if role_key in [1,2]:
    if role_key == 1:
      role = 'Scrum Master'
      session_user = 'Scrum Master'
    else:
      role = 'Developer'
  else:
    print('Error: Invalid Selection...')
    role_key = int(input('Selection: '))


if role == 'Developer':
    while not session_user:
      name = input('Please enter your name: ')
      if name in [user.name for user in users]:
        session_user = get_obj_by_name(name, users)
      else:
        print('\nError: User is not in database!\n')
print('\nUser Sign In Successfull!\n')
while 1:
  print('Available Options:\n')
  print('0- Save & Exit')
  if(role == 'Scrum Master'):
    print('1- Create Iteration')
    print('2- Create User Story')
    print('3- Create Task')
    print('4- Delete User Story')
    print('5- Delete Task')
  else:
    print('6- Update Task Status')
  print('7- Generate Iteration Report')
  print('\n')
  curr_opp=input("Enter option: ")

  # Exit handling
  if(curr_opp not in ['0','1', '2','3','4', '5', '6', '7', '8', '9', '10']):
    print("\nError: Invalid Opperation, Please Try Again!\n")

  elif(curr_opp == '0'):
    print('\nData has been written to database...\n')
    break

  elif(curr_opp == '1' and role == 'Scrum Master'):
    # Create a new Iteration
    name=input("Enter Iteration Name: ")
    duration=int(input("Enter Iteration Duration (in days): "))
    start=input("Enter instructor Start (DD/MM/YYYY): ")
    developers = []
    while(developers == []):
      temp_developers = (input("Enter Developer Names ( - seperated): ")).split('-')
      temp_list = []
      for developer in temp_developers:
        if developer not in [user.name for user in users]:
          # Create The user that did not exist before
          users.append(Developer(developer))
          temp_list.append(get_obj_by_name(developer, users))
        else:
          temp_list.append(get_obj_by_name(developer, users))
      developers = temp_list
    iterations.append(Iteration(name, duration, datetime.datetime.strptime(start, "%d/%m/%Y").date(), developers))
    print("\nIteration Created Successfully\n")

    # create a new user story and assign it to Iteration
  elif(curr_opp == "2" and role == 'Scrum Master'):
    if(iterations == []):
      print('\nAn Iteration needs to be created before creating additional user stories\n')
    else:
      print('\nPlease selectan iteration to add the story to:\n')
      for itr in iterations:
        print(itr.name)
      print('\n')
      selected_itr = input("Selection: ")
      while selected_itr not in [itr.name for itr in iterations]:
        print('\nError: Invalid Selection...\n')
        selected_itr = input("Selection: ")
      selected_iteration = get_obj_by_name(selected_itr, iterations)
      name=input("Enter User Story Name: ")
      while name in [item.name for item in selected_iteration.userStories]:
        print('\nError: Story Already exists in iteration, please try again...\n')
        name=input("Enter User Story Name: ")
      size=int(input("Enter User Story Size: "))
      selected_iteration.add_story(UserStory(name, size))
      print("\nUser Story Created Successfully\n")

  # create new task and assign in to a user story
  elif(curr_opp == "3" and role == 'Scrum Master'):
    if(iterations == []):
      print('\nAn Iteration needs to be created before creating additional tasks\n')
    else:
      temp = {}
      print('\nPlease select an iteration to add the task to:\n')
      for itr in iterations:
        print(itr.name+':')
        temp[itr.name] = {}
        for story in itr.userStories:
          print('\t'+story.name)
          temp[itr.name][story.name]=story
        print('\n')
      selected_itr = input("Selection: ")
      while selected_itr not in [itr.name for itr in iterations]:
        print('\nError: Invalid Selection...\n')
        selected_itr = input("Selection: ")
      if(not get_obj_by_name(selected_itr, iterations).userStories):
        print('\nNew tasks cant be added to iterations with no user stories...\n')
      else:
        print('\nPlease select a user story to add the task to:\n')
        for item in temp[selected_itr].keys():
          print(item)
        print('\n')
        selected_story = input("Selection: ")
        while selected_story not in temp[selected_itr].keys():
          print('\nError: Invalid Selection...\n')
          selected_story = input("Selection: ")
        selected_itr = get_obj_by_name(selected_itr, iterations)
        selected_story = get_obj_by_name(selected_story, selected_itr.userStories)

        name = input("Enter Task Name: ")
        while name in [item.name for item in selected_story.tasks]:
          print('\nError: Task Already Exists...\n')
          name = input("Selection: ")
        effort = int(input("Enter Task Effort: "))
        print('\nPlease select a developer: \n')
        for dev in selected_itr.developers:
          print(dev.name)
        print('\n')
        selected_dev = input('Selection: ')
        while selected_dev not in [item.name for item in selected_itr.developers]:
          print('\nError: Invalid Developer Name...\n')
          selected_dev = input('Selection: ')
        start = input('Start Date (DD/MM/YYYY): ')
        selected_story.add_task(Task(name, effort, get_obj_by_name(selected_dev, users), datetime.datetime.strptime(start, "%d/%m/%Y").date(), 'Open', None))
        print('\nTask has been created successfully!\n')

  elif(curr_opp == '4' and role == 'Scrum Master'):
    print('Please Select An Iteration\n')
    temp = []
    for itr in iterations:
      print(itr.name)
      temp.append(itr.name)
    print('\n')
    selected_itr = input('Selection: ')
    while selected_itr not in temp:
      print('\nError: Invalid Selection...\n')
      selected_itr = input('Selection: ')
    selected_iteration = get_obj_by_name(selected_itr, iterations)
    print('\nPlease Select The User Story That You Would Like To Delete:\n')
    temp = []
    if not selected_iteration.userStories:
      print('\nThere are no user stories to be selected!\n')
    else:
      for us in selected_iteration.userStories:
        print(us.name)
        temp.append(us.name)
      selected_story = input('Selection: ')
      while(selected_story not in temp):
        print('\nError: Invalid Selection...\n')
        selected_story = input('Selection: ')

      selected_iteration.delete_userStory(selected_story)
      selected_story = get_obj_by_name(selected_story, selected_iteration.userStories)
      print('\nUser Story Has Been Delete Successfully!\n')

  elif(curr_opp == '5' and role == 'Scrum Master'):
    print('\nPlease Select An Iteration\n')
    temp = []
    for itr in iterations:
      print(itr.name)
      temp.append(itr.name)
    print('\n')
    selected_itr = input('Selection: ')
    while selected_itr not in temp:
      print('Error: Invalid Selection...')
      selected_itr = input('Selection: ')
    selected_iteration = get_obj_by_name(selected_itr, iterations)
    print('\nPlease Select The User Story That Contains The Task That You Would Like to Delete:\n')
    temp = []
    if not selected_iteration.userStories:
      print('\nThere are no user stories to be selected!\n')
    else:
      for us in selected_iteration.userStories:
        print(us.name)
        temp.append(us.name)
      selected_story = input('Selection: ')
      while(selected_story not in temp):
        print('Error: Invalid Selection...')
        selected_story = input('Selection: ')
      selected_story = get_obj_by_name(selected_story, selected_iteration.userStories)
      print('\nPlease Select the Task that You Would Like to Delete:\n')
      temp = []
      if not selected_story.tasks:
        print('\nThere are no tasks to be deleted!\n')
      else:
        for item in selected_story.tasks:
          print(item.name)
          temp.append(item.name )
        print('\n')
        selected_task = input('Selection: ')
        while selected_task not in temp:
          print('\nError: Invalid Selection...\n')
          selected_task = input('Selection: ')

        selected_story.delete_task(selected_task)
        print('\nTask Has Been Delete Successfully!\n')

  elif(curr_opp == '6'):
    temp = []
    for itr in iterations:
      if session_user in itr.developers:
        temp.append(itr)
    if not temp:
      print('\You are not a part of any iteration so you cant edit a task...\n')
    else:
      print('\nPlease Select the Iteration that contains the task:\n')
      for item in temp:
        print(item.name)
      print('\n')
      selected_itr = input('Selection: ')
      while selected_itr not in [itr.name for itr in temp]:
        print('\nError: Invalid Selection...\n')
        selected_itr = input('Selection: ')
      selected_itr = get_obj_by_name(selected_itr, temp)
      temp = []

      print('\nPlease Select the User Story that contains the task:\n')
      for item in  selected_itr.userStories:
        temp.append(item.name)
        print(item.name)
      print('\n')
      selected_story = input('Selection: ')
      while selected_story not in temp:
        print('\nError: Invalid Selection...\n')
        selected_story = input('Selection: ')
      selected_story = get_obj_by_name(selected_story, selected_itr.userStories)
      if(not selected_story.tasks):
        print('\nThere are no tasks in this story yet...\n')
      else:
        valid = False
        temp = []
        for task in selected_story.tasks:
          if session_user == task.developer:
            temp.append(task.name+' - '+task.status)
            valid = True
        if not valid:
          print('\nYou are not assigned to any tasks in this story...\n')
        else:
          print('\nPlease Select the task that you would like to update:\n')
          for item in temp:
            print(item)
          print('\n')
          selected_task = input('Selection: ')
          while selected_task not in [task.name for task in selected_story.tasks]:
            print('\nError: Invalid Selection...\n')
            selected_task = input('Selection: ')
          print('Please select the new status that you would like to assign:')
          print('1- In Progress')
          print('2- Completed\n')
          selection = input('Selection: ')
          while selection not in ['1', '2']:
            print('\nError: Invalid Selection...\n')
            selection = input('Selection: ')
          task = get_obj_by_name(selected_task, selected_story.tasks)
          if(selection == '1'):
            task.update_status('In Progress')
          else:
            task.update_status('Completed')
          print('\nTask Update Successfully!\n')

  elif(curr_opp == '7'):
    print('\nPlease Select an Iteration:\n')
    for itr in iterations:
      if itr.userStories != [] and all(elem.tasks != [] for elem in itr.userStories):
          print(itr.name)
    print('\n')
    selected_iteration = input('Selection: ')
    while selected_iteration not in [item.name for item in iterations]:
      print('Error: Invalid Selection... ')
      selected_iteration = input('Selection: ')
    selected_iteration = get_obj_by_name(selected_iteration, iterations)
    selected_iteration.print_report()
save(users, iterations)

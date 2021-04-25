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
  role_key = input('Selection: ')
  if role_key in ['1','2']:
    if role_key == '1':
      role = 'Scrum Master'
      session_user = 'Scrum Master'
    else:
      role = 'Developer'
  else:
    print('Error: Invalid Selection...')
    #role_key = input('Selection: ')


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
    print('6- Delete Iteration')
  else:
    print('7- Update Task Status')
  print('8- Generate Iteration Report')
  print('\n')
  curr_opp=input("Enter option: ")

  if(not (curr_opp in ['0','8'] or (role == 'Scrum Master' and curr_opp in ['1', '2','3','4', '5', '6']) or (role == 'Developer' and curr_opp in ['7']))):
    print("\nError: Invalid Operation, Please Try Again!\n")
    
  # Exit handling
  #if(curr_opp not in ['0','1', '2','3','4', '5', '6', '7', '8', '9', '10']):
   # print("\nError: Invalid Operation, Please Try Again!\n")

  elif(curr_opp == '0'):
    print('\nData has been written to database...\n')
    break

  elif(curr_opp == '1'):
    # Create a new Iteration
    name=input("Enter Iteration Name: ")
    while True:
      try:
        duration=int(input("Enter Iteration Duration (in days): "))
        break
      except:
        print("Invalid Duration")
    while True:
      try:
        start= datetime.datetime.strptime(input("Enter iteration Start (DD/MM/YYYY): "), "%d/%m/%Y").date()
        break
      except:
        print("Invalid Date")
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
    iterations.append(Iteration(name, duration, start, developers))
    print("\nIteration Created Successfully\n")
      
    # create a new user story and assign it to Iteration
  elif(curr_opp == "2"):
    if(iterations == []):
      print('\nAn Iteration needs to be created before creating additional user stories\n')
    else:
      print('\nPlease select the number for an iteration to add the story to or Back to go to main menu.\n')
      i=1
      for itr in iterations:
        print(str(i)+": "+itr.name)
        i+=1
      print('\n')
      
      
      selected_itr = input("Selection: ")

#add back option
      #if selected_itr.lower() == "back":
       # continue
      
      while selected_itr.lower() != "back":
        try:
          if int(selected_itr)>0:
            selected_itr = iterations[int(selected_itr)-1].name
            break
          else:
            selected_itr = input("Invalid Selection.. Try again: ")
        except:
          selected_itr = input("Invalid Selection.. Try again: ")
      if selected_itr.lower() == "back":
        continue
      print('\nYou selected:', selected_itr,'\n')



      #while selected_itr not in [itr.name for itr in iterations]:
      #  print('\nError: Invalid Selection...\n')
      #  selected_itr = input("Selection: ")
      selected_iteration = get_obj_by_name(selected_itr, iterations)
      name=input("Enter User Story Name: ")
      while name in [item.name for item in selected_iteration.userStories]:
        print('\nError: Story Already exists in iteration, please try again...\n')
        name=input("Enter User Story Name: ")
      while True:
        try:
          size=int(input("Enter User Story Size: "))
          break
        except:
          print("Invalid Size. Please choose an integer value.")
      selected_iteration.add_story(UserStory(name, size))
      print("\nUser Story Created Successfully\n")

  # create new task and assign in to a user story
  elif(curr_opp == "3"):
    if(iterations == []):
      print('\nAn Iteration needs to be created before creating additional tasks\n')
    else:
      temp = {}
      print('\nPlease select an iteration to add the task to:\n')
      i=1
      n=[]
      for itr in iterations:
        print(str(i)+"- "+itr.name+':')
        i+=1
        temp[itr.name] = {}
        n.append(itr.name)
        for story in itr.userStories:
          print('\t'+story.name)
          temp[itr.name][story.name]=story
        print('\n')
      selected_itr = input("Selection: ")

      while selected_itr.lower() != "back":
        try:
          if int(selected_itr)>0:
            selected_itr = n[int(selected_itr)-1]
            break
          else:
            selected_itr = input("Invalid Selection.. Try again: ")
        except:
          selected_itr = input("Invalid Selection.. Try again: ")

      if selected_itr.lower() == "back":
        continue

      if(not get_obj_by_name(selected_itr, iterations).userStories):
        print('\nNew tasks cant be added to iterations with no user stories...\n')
      else:
        print('\nPlease select a user story to add the task to:\n')
        i=1
        k=[]
        for item in temp[selected_itr].keys():
          print(str(i)+": "+item)
          k.append(item)
          i+=1
        print('\n')
        selected_story = input("Selection: ")

        while selected_story.lower() != "back":
          try:
            if int(selected_story)>0:
              selected_story = k[int(selected_story)-1]
              break
            else:
              selected_story = input("Invalid Selection.. Try again: ")
          except:
            selected_story = input("Invalid Selection.. Try again: ")
        if selected_story.lower() == "back":
          continue

       # while selected_story not in temp[selected_itr].keys():
       #   print('\nError: Invalid Selection...\n')
       #   selected_story = input("Selection: ")
       
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
        while True:
          try:
            start= datetime.datetime.strptime(input('Start Date (DD/MM/YYYY): '), "%d/%m/%Y").date()
            break
          except:
            print("Invalid Date")
        selected_story.add_task(Task(name, effort, get_obj_by_name(selected_dev, users), start, 'Open', None))
        print('\nTask has been created successfully!\n')

  #delete user story
  elif(curr_opp == '4'):
    print('Please Select An Iteration\n')
    #temp = []
    i=1
    for itr in iterations:
      print(str(i)+": "+itr.name)
      i+=1
      #temp.append(itr.name)
    print('\n')
    selected_itr = input('Selection: ')

    #if selected_itr.lower()=="back":
    #  continue

    while selected_itr.lower() != "back":
      try:
        if int(selected_itr)>0:
          selected_itr = iterations[int(selected_itr)-1].name
          break
        else:
          selected_itr = input("Invalid Selection.. Try again: ")
      except:
        selected_itr = input("Invalid Selection.. Try again: ")

    if selected_itr.lower() == "back":
        continue
      
   
    #while selected_itr not in temp:
    #  print('\nError: Invalid Selection...\n')
    #  selected_itr = input('Selection: ')

    selected_iteration = get_obj_by_name(selected_itr, iterations)
    
    print('\nPlease Select The User Story That You Would Like To Delete:\n')
    temp = []
    if not selected_iteration.userStories:
      print('\nThere are no user stories to be selected!\n')
    else:
      i=1
      for us in selected_iteration.userStories:
        print(str(i)+": "+us.name)
        i+=1
        temp.append(us.name)
      selected_story = input('Selection: ')

      #if selected_story.lower() == "back":
      #  continue
      
      while selected_story.lower() != "back":
        try:
          if int(selected_story)>0:
            selected_story = temp[int(selected_story)-1]
            break
          else:
            selected_story = input("Invalid Selection.. Try again: ")
        except:
          selected_story = input("Invalid Selection.. Try again: ")
      if selected_story.lower() == "back":
        continue


      #while(selected_story not in temp):
        #print('\nError: Invalid Selection...\n')
        #selected_story = input('Selection: ')

      selected_iteration.delete_userStory(selected_story)
      selected_story = get_obj_by_name(selected_story, selected_iteration.userStories)  #delete this line
      print('\nUser Story Has Been Deleted Successfully!\n')

  elif(curr_opp == '5'):
    print('\nPlease Select An Iteration\n')
    #temp = []
    i=1
    for itr in iterations:
      print(str(i)+": "+itr.name)
      i+=1
      #temp.append(itr.name)
    print('\n')
    selected_itr = input('Selection: ')
    
    while selected_itr.lower() != "back":
      try:
        if int(selected_itr)>0:
          selected_itr = iterations[int(selected_itr)-1].name
          break
        else:
          selected_itr = input("Invalid Selection.. Try again: ")
      except:
        selected_itr = input("Invalid Selection.. Try again: ")

    if selected_itr.lower() == "back":
        continue

    selected_iteration = get_obj_by_name(selected_itr, iterations)
    
    print('\nPlease Select The User Story That Contains The Task That You Would Like to Delete:\n')
    temp = []
    if not selected_iteration.userStories:
      print('\nThere are no user stories to be selected!\n')
    else:
      i=1
      for us in selected_iteration.userStories:
        print(str(i)+": "+us.name)
        i+=1
        temp.append(us.name)
      print('\n')
      selected_story = input('Selection: ')
      
      while selected_story.lower() != "back":
        try:
          if int(selected_story)>0:
            selected_story = temp[int(selected_story)-1]
            break
          else:
            selected_story = input("Invalid Selection.. Try again: ")
        except:
          selected_story = input("Invalid Selection.. Try again: ")
      if selected_story.lower() == "back":
        continue
      
      selected_story = get_obj_by_name(selected_story, selected_iteration.userStories)
      print('\nPlease Select the Task that You Would Like to Delete:\n')
      temp = []
      if not selected_story.tasks:
        print('\nThere are no tasks to be deleted!\n')
      else:
        
        i=1
        for item in selected_story.tasks:
          print(str(i)+": "+item.name)
          i+=1
          temp.append(item.name)
        print('\n')
        selected_task=input('Selection: ')

        while selected_task.lower()!="back":
          try:
            if int(selected_task)>0:
              selected_task = temp[int(selected_task)-1]
              break
            else:
              selected_task = input("Invalid Selection.. Try again: ")
          except:
            selected_task = input("Invalid Selection.. Try again: ")
        if selected_task.lower() == "back":
          continue

        
        selected_story.delete_task(selected_task)
        print('\nTask Has Been Delete Successfully!\n')

##############
  elif(curr_opp == '6'):
    print('\nPlease select an iteration to delete:\n')
    if iterations == []:
      print('\nCaution: No iterations are available.\n')
      continue
    i=1
    for itr in iterations:
      print(str(i)+": "+itr.name)
      i+=1
    print('\n')

    selected_itr = input("Selection: ")
    while selected_itr.lower()!="back":
      try:
        if int(selected_itr)>0:
          selected_itr = iterations[int(selected_itr)-1]
          break
        else:
          selected_itr = input("Invalid Selection.. Try again: ")
      except:
        selected_itr = input("Invalid Selection.. Try again: ")
    if selected_itr.lower() == "back":
      continue 
    iterations.remove(selected_itr)
    print('\nIteration has been deleted.\n')
##############

  elif(curr_opp == '7'):
    temp = []
    for itr in iterations:
      if session_user in itr.developers:
        temp.append(itr)
    if not temp:
      print('\You are not a part of any iteration so you cant edit a task...\n')
    else:
      print('\nPlease Select the Iteration that contains the task:\n')
      i=1
      for item in temp:
        print(str(i)+": "+item.name)
        i+=1
      print('\n')
      selected_itr = input('Selection: ')

      while selected_itr.lower() != "back":
        try:
          if int(selected_itr)>0:
            selected_itr = temp[int(selected_itr)-1].name
            break
          else:
            selected_itr = input("Invalid Selection.. Try again: ")
        except:
         selected_itr = input("Invalid Selection.. Try again: ")

      if selected_itr.lower() == "back":
        continue


      selected_itr = get_obj_by_name(selected_itr, temp)
      temp = []

      print('\nPlease Select the User Story that contains the task:\n')
      i=1
      for item in  selected_itr.userStories:
        temp.append(item.name)
        print(str(i)+": "+item.name)
        i+=1
      print('\n')
      selected_story = input('Selection: ')

      while selected_story.lower() != "back":
        try:
          if int(selected_story)>0:
            selected_story = temp[int(selected_story)-1]
            break
          else:
            selected_story = input("Invalid Selection.. Try again: ")
        except:
          selected_story = input("Invalid Selection.. Try again: ")
      if selected_story.lower() == "back":
        continue

       
      selected_story = get_obj_by_name(selected_story, selected_itr.userStories)
      if(not selected_story.tasks):
        print('\nThere are no tasks in this story yet...\n')
      else:
        valid = False
        temp = []
        n = []
        for task in selected_story.tasks:
          if session_user == task.developer:
            temp.append(task.name+' - '+task.status)
            n.append(task.name)
            valid = True
        if not valid:
          print('\nYou are not assigned to any tasks in this story...\n')
        else:
          print('\nPlease Select the task that you would like to update:\n')
          i=1
          for item in temp:
            print(str(i)+': '+item)
            i+=1
          print('\n')
          selected_task = input('Selection: ')

          while selected_task.lower()!="back":
            try:
              if int(selected_task)>0:
                selected_task = n[int(selected_task)-1]
                break
              else:
                selected_task = input("Invalid Selection.. Try again: ")
            except:
              selected_task = input("Invalid Selection.. Try again: ")
            
          if selected_task.lower() == "back":
            continue

            
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

  elif(curr_opp == '8'):
    print('\nPlease Select an Iteration:\n')
    i=1
    temp=[]
    for itr in iterations:
      if itr.userStories != [] and all(elem.tasks != [] for elem in itr.userStories):
        print(str(i)+": "+itr.name)
        i+=1
        temp.append(itr.name)
    print('\n')
    selected_itr = input('Selection: ')

    while selected_itr.lower() != "back":
      try:
        if int(selected_itr)>0:
          selected_itr = temp[int(selected_itr)-1]
          break
        else:
          selected_itr = input("Invalid Selection.. Try again: ")
      except:
        selected_itr = input("Invalid Selection.. Try again: ")

    if selected_itr.lower() == "back":
        continue

    selected_itr = get_obj_by_name(selected_itr, iterations)
    selected_itr.print_report()
    
save(users, iterations)

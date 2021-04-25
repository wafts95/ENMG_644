
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





































   



























#add back option
      if selected_itr.lower() == "back":
        continue
      
      while True:
        try:
          if int(selected_itr)>0:
            selected_itr = iterations[int(selected_itr)-1].name
            break
          else:
            selected_itr = input("Invalid Selection.. Try again: ")
        except:
          selected_itr = input("Invalid Selection.. Try again: ")
      print('\nYou selected:', selected_itr,'\n')

      
i=1
for itr in iterations:
        print(str(i)+": "+itr.name)
        i+=1
      print('\n')

      selected_itr = input("Selection: ")

#add back option
      if selected_itr.lower() == "back":
        continue
      
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

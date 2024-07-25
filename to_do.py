
# Online Python - IDE, Editor, Compiler, Interpreter
def task():
  tasks = []  #empty_list
  print("welcome to the to-do app")

  total_task = int(input("enter how many task u want to add =-----"))
  for i in range(1,total_task+1):
    task_name = input(f"enter task {i} = ")
    tasks.append(task_name)
  print(f"today's tasks are\n {tasks}")
  while True:
    operation = int(input("enter  1- add\n 2-update\n3-delete\n4-view\n5-exit/stop"))
    if operation == 1:
      add = input("enter task you want to add =")
      tasks.append(add)
      print(f"Task{add} has been successfully added..... ")
    elif operation == 2:
      update_val = input("enter the task name you want to update")
      if update_val in tasks:
        up = input("enter new tasks = ")
        ind = tasks.index(update_val)
        tasks[ind] = up
        print(f"updated tasks{up} ")
    elif operation == 3:
        del_val = input("which task you want to delete? = ")
        if del_val in tasks:
            ind = tasks.index(del_val)
            del tasks[ind]
            print(f"task {del_val} has been deleted")
    elif operation == 4:
        print(f"total task = {tasks}")
    elif operation == 5:
        print("closing the program ......")
        break
    else:
        print("invalid input")
task()

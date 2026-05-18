#v1-basic-todo
#Features : add,view,remove,basic menu

tasks=[]

def add_task(tasks,task):
  tasks.append(task)
  print("Task added successfully")
  print()

def view_tasks(tasks):
  if (len(tasks)==0):
    print("No tasks available")
  else:
    print("Your Tasks")
    for i in range(1,len(tasks)+1):
      print(f"[{i}] {tasks[i-1]}")
  print()

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print("Task Removed : ", removed)
    else:
        print("Invalid task number")
    print()

while True:

  print("TO-DO LIST")
  print("01. Add task")
  print("02. View tasks")
  print("03. Remove Task")
  print("04. Exit")
  print()

  choice=input("Choose an option (01-04) : ")
  print()

  if (choice=="1"):
    task=input("Enter task : ")
    add_task(tasks,task)

  elif (choice=="2"):
    view_tasks(tasks)

  elif (choice=="3"):
      index=int(input("Enter the task number : "))
      remove_task(tasks,index)

  elif(choice=="4"):
    break

  else:
    print("Invalid Choice")
    print()
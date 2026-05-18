#v2-advanced-features-todo
#Features added : datetime module,undo,edit,search tasks,task status,counters,clear all tasks

from datetime import datetime

tasks=[]
last_deleted = None

#ADD TASKS
def add_task(tasks,task):
  created_time=datetime.now().strftime("%d-%m-%y")
  tasks.append([task,"Pending", created_time])
  print("Task added successfully")
  print()


#VIEW TASKS
def view_tasks(tasks):
  if (len(tasks)==0):
    print("No tasks available")
    print()

  else:
    print("Your tasks")
    for i in range(1,len(tasks)+1):
      print(f"[{i}] {tasks[i-1][0]} [{tasks[i-1][1]}] [{tasks[i-1][2]}]")
    print()

#REMOVE TASKS
def remove_task(tasks, index):
    global last_deleted
    if 1 <= index <= len(tasks):
        last_deleted = tasks.pop(index - 1)
        print(f"Task Removed :  {last_deleted[0]}")
        print()

    else:
        print("Invalid task number")
        print()

#UNDO TASKS
def undo_task(tasks):
    global last_deleted
    if last_deleted is not None:
      tasks.append(last_deleted)
      print(f"Task Undo :  {last_deleted[0]}")
      last_deleted = None

    else:
        print("No tasks to undo")
    print()

#EDIT TASKS
def edit_task(tasks, index,edit):
    if index >= 1 and index <= len(tasks):
        tasks[index-1][0]=edit
        print("Task Edited")
        print()
    else:
        print("Invalid task number")
        print()

#CLEAR TASKS
def clr_task(tasks):
  if len(tasks) == 0:
        print("No tasks available")
        print()
  else:
    confirm = input("Are you sure? (y/n): ")
    print()

    if confirm.lower() == "y":
        tasks.clear()
        print("List Cleared")
    else:
        print("Operation Cancelled")
    print()


#SEARCH TASKS
def task_finder(tasks,search):
    found = False
    for i in range(len(tasks)):
      if search.lower() in tasks[i][0].lower():
            print(f"Task Found : {tasks[i][0]} [{tasks[i][1]}]")
            found = True

    if found == False:
        print("Task Not Found")
    print()


#TASKS STATUS
def status(tasks,index):
  if 1 <= index <= len(tasks):
    if (tasks[index-1][1]=="Completed"):
      print("Task is already completed")
    else:
        tasks[index-1][1]="Completed"
        print("Marked as completed")
  else:
      print("Invalid task number")
  print()

#PENDING TASK COUNTER
def counter_pendingtasks(tasks):
    count = 0
    if len(tasks) == 0:
        print("No task available")
    else:
        for i in range(len(tasks)):
            if tasks[i][1] == "Pending":
                count += 1
        print(f"No. of Pending tasks : {count}")
    print()

#COMPLETED TASK COUNTER
def counter_completedtasks(tasks):
    count = 0
    if len(tasks) == 0:
        print("No task available")
    else:
        for i in range(len(tasks)):
            if tasks[i][1] == "Completed":
                count += 1
        print(f"No. of Completed tasks :  {count}")
    print()


def main():

  while True:

    print("TO-DO LIST")
    print("01. Add task")
    print("02. View tasks")
    print("03. Remove Task")
    print("04. Undo task")
    print("05. Edit task")
    print("06. Search tasks")
    print("07. Mark task as completed")
    print("08. Count completed tasks")
    print("09. Count pending tasks")
    print("10. Clear all tasks")
    print("11. Exit")
    print()

    choice=input("Choose an option (1-11) : ")
    print()

    if (choice=="1"):
      task=input("Enter task : ")
      print()
      add_task(tasks,task)

    elif (choice=="2"):
      view_tasks(tasks)

    elif (choice=="3"):
      index=int(input("Enter the task number : "))
      print()
      remove_task(tasks,index)

    elif (choice=="4"):
      undo_task(tasks)

    elif(choice=="5"):
      index=int(input("Enter the task number to edit : "))
      edit=input("Enter the new task : ")
      print()
      edit_task(tasks,index,edit)

    elif (choice=="6"):
      search=input("Enter the task to find : ")
      print()
      task_finder(tasks,search)

    elif (choice=="7"):
      index=int(input("Enter the task number : "))
      print()
      status(tasks,index)

    elif (choice=="8"):
      counter_completedtasks(tasks)

    elif (choice=="9"):
      counter_pendingtasks(tasks)

    elif (choice=="10"):
      clr_task(tasks)

    elif (choice=="11"):
      break

    else:
      print("Invalid choice")
      print()

main()
tasks=[]

def addTask():
    task = input("New To-Do:")
    tasks.append(task)
    print(f"To-Do '{task}' added to the list.")

def listTask():
    if not tasks:
        print("There are no To-Dos currently.")
    else:
        print("Current To-Dos:")
        for index,task in enumerate(tasks):
            print(f"To-Do #{index}. {task}")
def deleteTask():
  listTask()
  try:
    taskToDelete = int(input("Enter the # to delete: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"To-Do {taskToDelete} has been removed.")
    else:
      print(f"To-Do #{taskToDelete} was not found.")
  except:
    print("Invalid input.")


if __name__=="__main__":
    print("Welcome to the TO-DO LIST App :)")
    while True:
        print("\n")
        print("Please select one of the following option")
        print("-----------------------------------------")
        print("1.Add a New TO-Do ")
        print("2.Delete a To-Do")
        print("3.List TO-DO")
        print("4.Quit")

        choice=input("Enter your choice:")

        if(choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTask()
        elif (choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")

    print("Thank you for using the App")
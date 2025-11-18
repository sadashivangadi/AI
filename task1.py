tasks=[]
def menu():
    print("---To-Do-List----\n")
    print("1.View Tasks\n")
    print("2.Add Task\n")
    print("3.Upadate Task\n")
    print("4.Delete Task\n")
    print("5.Exit")

while True:
    menu()

    choice=input("Enter your choice\n")
    #View the tasks step 1
    if (choice=="1"):
        if not tasks:
            print("Do-To-List is EEmpty")
        else:
            print("\n Your tasks")
            for index,task in enumerate(tasks,start=1):
                print(f"{index}.{task}")
 #Add the tasks step 2
    elif(choice=="2"):
        new_task=input("Enter the new taks")
        tasks.append(new_task)
        print("Task added successfully")
 #Update the tasks step 3
    elif(choice=='3'):
        if not tasks:
            print("no taks is updated")
        else:
            for index,task in enumerate(tasks,start=1):
                print(f"{index}.{task}")
            try:
                task_num=int(input("Enter the task number is update"))
                if 1<=task_num<=len(tasks):
                    new_text=input("Enter updated tasks")
                    tasks[task_num-1]=new_text
                    print("Task updated succssufully ")
                else:
                    print("invalid tasks number")
            except ValueError:
                    print("please enter valid input")
       #Deleted the tasks step 4 
    elif(choice=='4'):
        if not tasks:
            print("NO tasks to delete")
        else:
            for index,task in enumerate(tasks,start=1):
                   print(f"{index}.{task}")
            try:
                task_num=int(input("enter task number to delete"))
                if 1<=task_num<=len(tasks):
                    removed=tasks.pop(task_num-1)
                else:
                    print("invalid task number")
            except ValueError:
                    print("please eneter the valid number")
     #Exit the tasks step 5 
    elif (choice=='5'):
        print("Exiting the Do-To-List App BYEEEE !!!")
        break
    else:
            print("invalid choice!,please enter the number between 1 and 5 ")

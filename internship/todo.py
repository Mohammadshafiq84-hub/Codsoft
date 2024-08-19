#creating empty list
task=[]

#defining function to ask the user to enter the tasks to be added 
def addtask():
    #ask the user to enter the number of tasks want to be added
    number=int(input("Enter the number of tasks to be added:"))
    for i in range(number):
        
        #ask the user to enter the tasks.
        add=input(f"Enter the task {i+1}:")
        if add not in task:
             task.append(add)
             print(f" Task  #{add}  added successfully....")
        else:     
            print(f"Task #{add} already exists!!!!")

#defining function to update the tasks
def  updatetask():
    #ask the user to enter the name of the task to be updated
    upd=input("Enter the task name  you want to update:")  
    #checking if the task is present or not
    if upd in task:
        new=input("Enter the new task you want to add:")
        index=task.index(upd)
        task[index]=new
        print(f"task #{new} updated successfully....")

    else:
        print("Invalid task!!!!")    

#defining function to delete task
def deletetask():
    dele=input("Enter the task you want to delete:")
    #checking whether the entered task is present or not
    if dele in task:
        index=task.index(dele)
        del task[index]
        print(f"succesfully deleted the #{dele} task ")
    else:
        print("There is no task to delete!!")

#defining fuunction to view the tasks
def viewtask():
    print("works to do today are:\n",task)

#giving the users choice to choose what they want to do
print("Welcome to my todo list app!!!!")
print("Choose the activity you wish to do:")
print("1.Add task")  
print("2.Update task")  
print("3.Delete task")
print("4.View task")
print("5.Exit")

#running this loop until user chooses to exit 
while True:
    try:  
        choose=int(input("Enter your choice:"))
        if choose==1:
            addtask()

        elif choose==2:
            updatetask()

        elif choose==3:
            deletetask()

        elif choose==4:
            viewtask()

        elif choose==5 :    
            print("Thank youu visit again......")    
            break
        else:
            print("Invalid input!!!!!!")

    except ValueError:
        print("Invalid input. Please enter a number!!!!")        
        



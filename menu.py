# To-Do List
# 1. Add a task 
# 2. View tasks
# 3. Delete a task
# 4. Exit 
# Choose an option (1-4): 1 (etc. 2, 3, 4)

# Enter a new task: Buy groceries
# Task added successfully!


def display_menu():
    print("To-Do List")
    print("1. Add a task")
    print("2. View tasks")  
    print("3. Delete a task")
    print("4. Exit")

def main():
    tasks = []
    while True: 
       display_menu()
       choice = input("Choose an option (1-4):")

       if choice == "1":
           new_task = input("Enter a new task: ")
           tasks.append(new_task)
           print(f"Task '{new_task}' added!")
       elif choice == "2":
           if not tasks: 
               print("No tasks yet - add one from the main menu!")
           else: 
               print("Tasks:")
               for i, task in enumerate(tasks, start=1): 
                   print(f"{i}. {task}")

       elif choice == "3":
           if not tasks:
               print("No tasks to delete.")
               continue
           
           print("Tasks:")
           for i, task in enumerate(tasks, start=1):
               print(f"{i}. {task}")
           try: 
               task_num = int(input("Enter the task number to delete: "))
               index = task_num - 1
               tasks.pop(index)
           except ValueError:
               print("Please enter a valid number.")
           except IndexError:
               print("That task number does not exist.")    
           else:
               print("Task deleted successfully.")         
           finally:
               print("Delete operation complete.")       
       elif choice == "4":
           print("Exiting the program.")
           break                        
       else: 
           print("Invalid choice. Please try again.")
main()
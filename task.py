from datetime import datetime
import uuid
class Task:
    all_tasks=[]
    incomplete_tasks=[]
    completed_tasks=[]

    def __init__(self,name):
        self.task_name=name
        dt=datetime.now()
        dt=dt.strftime("%d/%m/%y %H:%M:%S")
        self.created_time=dt
        self.updated_time="NA"
        self.completed_time="NA"
        self.task_done=False
        self.Id=uuid.uuid4()

    @classmethod
    def update_task(cls,task_obj,new_task_name):
        task_obj.task_name=new_task_name
        update_dt=datetime.now()
        update_dt=update_dt.strftime("%d/%m/%y %H:%M:%S")
        task_obj.updated_time=update_dt

    @classmethod
    def complete_task(cls,task_obj):
        com_dt=datetime.now()
        com_dt=com_dt.strftime("%d/%m/%y %H:%M:%S")
        task_obj.completed_time=com_dt
        #I have to mark the task as completed
        task_obj.task_done=True
        Task.completed_tasks.append(task_obj)
        Task.incomplete_tasks.remove(task_obj)

while True:
    print("1. Add New Task")
    print("2. Show All Task")
    print("3. Show Incomplete Tasks")
    print("4. Show Completed Tasks")
    print("5. Update Task")
    print("6. Mark A Task Completed")
    print("Enter Option: ",end="")
    option=int(input())
    if(option==1):
        print("Enter New Task: ",end="")
        task_name=input()
        task=Task(task_name)
        Task.all_tasks.append(task)
        Task.incomplete_tasks.append(task)
        print()
        print()
        print("Task Created Successfully")
        print()
        print()

    if option==2:
        print()
        print()
        if len(Task.all_tasks)==0:
            print("No Task To Show!")
            print()
            print()
        else:
            for task in Task.all_tasks:
                print(f"ID - {task.Id}")
                print(f"Task - {task.task_name}")
                print(f"Created Time - {task.created_time}")
                print(f"Updated Time - {task.updated_time}")
                print(f"Completed - {task.task_done}")
                print(f"Completed Time - {task.completed_time}")
                print()
                print()

    if option==3:
        print()
        print()
        if len(Task.incomplete_tasks)==0:
            print("No incomplete task")
            print()
            print()
        else:
            for task in Task.incomplete_tasks:
                print(f"ID - {task.Id}")
                print(f"Task - {task.task_name}")
                print(f"Created Time - {task.created_time}")
                print(f"Updated Time - {task.updated_time}")
                print(f"Completed - {task.task_done}")
                print(f"Completed Time - {task.completed_time}")
                print()
                print()

    if option==4:
        print()
        print()
        if len(Task.completed_tasks)==0:
            print("No Completed Task")
            print()
            print()
        else:
            for task in Task.completed_tasks:
                print(f"ID - {task.Id}")
                print(f"Task - {task.task_name}")
                print(f"Created Time - {task.created_time}")
                print(f"Updated Time - {task.updated_time}")
                print(f"Completed - {task.task_done}")
                print(f"Completed Time - {task.completed_time}")
                print()
                print()

    if option==5:
        print()
        print()
        if len(Task.incomplete_tasks)==0:
            print("No Task To Update")
            print()
            print()
        else:
            print("Select Which Task To Update:")
            print()
            print()
            for task_no,task in enumerate(Task.incomplete_tasks):
                print(f"Task No - {task_no+1}")
                print(f"ID - {task.Id}")
                print(f"Task - {task.task_name}")
                print(f"Created Time - {task.created_time}")
                print(f"Updated Time - {task.updated_time}")
                print(f"Completed - {task.task_done}")
                print(f"Completed Time - {task.completed_time}")
                print()
                print()
            task_no=int(input("Enter Task No: "))-1
            new_name=input("Enter New Task: ")
            print()
            print()
            Task.update_task(Task.incomplete_tasks[task_no],new_name)
            print("Task Updated Successfully")
            print()
            print()
    if option==6:
        print()
        print()
        if len(Task.incomplete_tasks)==0:
            print("No Task To Complete")
            print()
            print()
        else:
            print("Select Which Task To Complete:")
            print()
            print()
            for task_no,task in enumerate(Task.incomplete_tasks):
                print(f"Task No - {task_no+1}")
                print(f"ID - {task.Id}")
                print(f"Task - {task.task_name}")
                print(f"Created Time - {task.created_time}")
                print(f"Updated Time - {task.updated_time}")
                print(f"Completed - {task.task_done}")
                print(f"Completed Time - {task.completed_time}")
                print()
                print()
            task_no=int(input("Enter Task No: "))-1
            print()
            print()
            Task.complete_task(Task.incomplete_tasks[task_no])
            print("Task Completed Successfully")
            print()
            print()


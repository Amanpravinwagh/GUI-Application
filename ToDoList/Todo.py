import os
def add_task():
    task = input('Enter task').title()
    with open('todo.txt','a') as f:
        f.write(f'{task},Not done\n')
    print('Task is added')
def view_task():
    if not os.path.isfile('todo.txt'):
        print('todo file not found')
        return
    if not os.path.getsize('todo.txt'):
        print('All tasks are deleted')
        return

    with open('todo.txt') as f:
        task_list = f.readlines()
        for i,line in enumerate(task_list,start=1):
            task,status = line.split(',')
            print(f'{i:<3}{task:25}{status}',end='')

def mark_done():
    if not os.path.isfile('todo.txt'):
        print('todo filke not found')
        return
    if not os.path.getsize('todo.txt'):
        print('All task are deleted')
        return

    task_no = int(input('Enter task_no.'))
    with open('todo.txt') as f:
        with open('temp.txt','w') as t:
            task_list = f.readline()
            for i,line in enumerate(task_list,start=1):
                task,status = line.split(',')
                if task_no ==1:
                    t.write(f'{task},Done\n')
                else:
                    t.write(line)

        os.remove('todo.txt')
        os.remove('temp.txt','todo.txt')
        print(f'Task{task_no} is marked as done')

def delete_task():
    if not os.path.isfile('todo.txt'):
        print('todo file not found')
        return
    if not os.path.getsize('todo.txt'):
        print('All task are deleted')
        return

    task_no = int(input('Enter task_no.'))
    with open('todo.txt') as f:
        with open('temp.txt','w') as t:
            task_list = f.readline()
            for i,line in enumerate(task_list,start=1):
                if task_no !=i:
                    t.write(line)

    os.remove('todo.txt')
    os.remove('temp.txt','todo.txt')
    print(f'Task{task_no} is deleted')

while True:
    print('-'*30)
    print(f'1.Add Task \
           \n2.View Task \
           \n3.Mark Done \
           \n4.Delete Task \
           \n0.Exit')
    choice = input('Enter choice')
    if not choice.isdigit():
        print('Invalid Input')
        continue

    choice = int(choice)
    if choice == 0:
        print('Good Bye')
        break

    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_done()
    elif choice == 4:
        delete_task()
    else:
        print('Invalid choice')

#end

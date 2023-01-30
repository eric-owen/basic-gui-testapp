import func
import time

while True:
    action = input("add, complete, show, edit, or quit: ").strip()

    if action.startswith('add'):
        todo = action.split(' ', 1)[1] + "\n"
        todos = func.get_todos()
        todos.append(todo)

        func.write_todos(todos)

    elif action.startswith('show'):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for i, todo in enumerate(todos):
            rank = i + 1
            todo = todo.strip('\n')
            print(f'{rank}. {todo}')
    elif action.startswith('edit'):
        try:
            num = action.split(' ', 1)[1]
            i = int(num) - 1

            todos = func.get_todos()

            new_todo = input("enter new todo: ")
            todos[i] = new_todo + "\n"

            func.write_todos(todos)

        except ValueError:
            print('command not valid, try again')
            continue
    elif action.startswith('complete'):
        try:
            num = int(action.split(' ', 1)[1])
            todos = func.get_todos()
            todos.pop(num - 1)
            func.write_todos(todos)

        except IndexError:
            print('todo does not exist, try again')
            continue
    elif action.startswith('quit'):
        break
    else:
        print('enter valid input')
print("bye")

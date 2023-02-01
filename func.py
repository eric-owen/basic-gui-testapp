FILEPATH = 'todos.txt'

def get_todos(path=FILEPATH):
    with open(path, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, path=FILEPATH):
    with open(path, 'w') as file:
        file.writelines(todos_arg)

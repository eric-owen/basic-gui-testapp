import func
import PySimpleGUI as sg

label = sg.Text("type in a todo")
input_box = sg.InputText(tooltip='enter todo', key='todo')
add_button = sg.Button('add')

window = sg.Window('my todo app',
                   layout=[[label], [input_box, add_button]])

while True:
    event, values = window.read()
    match event:
        case 'add':
            todos = func.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            func.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
import fuctiones
import FreeSimpleGUI as Sg
import time
import os

# Create the file if it doesn't exist
if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

Sg.theme('DarkBlue12')

layout = [[Sg.Text('', key='clock')],
          [Sg.Text("Enter new to-do")],
          [Sg.InputText(tooltip="Enter todo", key='todo'), Sg.Button("Add")],
          [Sg.Listbox(values=fuctiones.get_todos(), key='todos', enable_events=True, size=(45, 6)),
           Sg.Button('Edit'), Sg.Button("Complete")],
          [Sg.Button("Exit")]]

window = Sg.Window("TO-DO APP", layout, font=('Helvetica', 14))

while True:
    event, values = window.read(timeout=1000)  # Update clock every second
    if event == Sg.WINDOW_CLOSED or event == "Exit":
        break

    window['clock'].update(value=time.strftime("%Y-%m-%d %H:%M:%S"))

    match event:
        case "Add":
            todos = fuctiones.get_todos()  # Fetch the to-do list
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fuctiones.write_todos(todos)  # Save the to-do list back
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = fuctiones.get_todos()
                index = todos.index(to_edit)
                todos[index] = new_todo
                fuctiones.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                Sg.popup("Please select an item first", font=('Helvetica', 14))

        case "Complete":
            try:
                todo_remove = values['todos'][0]
                todos = fuctiones.get_todos()
                todos.remove(todo_remove)
                fuctiones.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                Sg.popup("Please select an item first", font=('Helvetica', 14))

        case 'todos':
            if values['todos']:  # Ensure the list is not empty
                window['todo'].update(value=values['todos'][0])

window.close()

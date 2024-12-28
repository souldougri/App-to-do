import fuctiones
import FreeSimpleGUI as Sg

layout = [[Sg.Text("Enter new to-do")],
          [Sg.InputText(tooltip="Enter todo", key='todo'), Sg.Button("Add")]]

window = Sg.Window("TO-DO APP", layout, font=('Helvetica', 15))

while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = fuctiones.get_todos()  # Fetch the to-do list
            print(type(todos))
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fuctiones.write_todos(todos)  # Save the to-do list back
        case Sg.WINDOW_CLOSED:
            break
window.close()

import fuctiones
import FreeSimpleGUI as Sg

layout = [[Sg.Text("Enter new to-do")],
          [Sg.InputText(tooltip="Enter todo", key='todo'), Sg.Button("Add"),],
          [Sg.Listbox(values=fuctiones.get_todos(),key='todos',enable_events= True,size=[45,6]),Sg.Button('Edit')]]

window = Sg.Window("TO-DO APP", layout, font=('Helvetica', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = fuctiones.get_todos()  # Fetch the to-do list
            print(type(todos))
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fuctiones.write_todos(todos)  # Save the to-do list back
            window['todos'].update(values=todos)
            print()
        case 'Edit':
           to_edit = values['todos'][0]
           new_todo = values['todo']

           todos = fuctiones.get_todos()
           index = todos.index(to_edit)
           todos[index] = new_todo
           fuctiones.write_todos(todos)
           window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case Sg.WINDOW_CLOSED:
            break
window.close()

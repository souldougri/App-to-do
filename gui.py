import fuctiones
import FreeSimpleGUI as sg


layout = [[sg.Text("Enter new to-do ")],[sg.Input(),sg.Button("Add")]]

windows = sg.Window("TO-DO APP",layout)
windows.read()
windows.close()





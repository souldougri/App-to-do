import streamlit as St
import fuctiones

todos = fuctiones.get_todos()
def new_todo():
    newToDo= St.session_state["new_todo"] + '\n'
    todos.append(newToDo)
    fuctiones.write_todos(todos)

St.title('مدير المهام')
St.write("نظم مهامك تزيد إنتاجيتك ",)


for index,todo in enumerate(todos):
    St.checkbox(todo,key=f"todo_{index}")

St.text_input(label="",
    placeholder="New to do...",
    on_change= new_todo,key="new_todo")
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Reads the file and returns the to-do list.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """
    Writes the to-do list to the file.
    """
    with open(filepath, "w") as file_write_local:
        file_write_local.writelines(todos_arg)

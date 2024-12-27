def get_todos (filepath="todos.txt"):
    """
    get_todos rede file and return to do list
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todods_arg, filepath="todos.txt" ):
    with open(filepath, "w") as file_write_lo:
        file_write_lo.writelines(todods_arg)


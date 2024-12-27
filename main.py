import fuctiones
while True:
   user_input = input(" Write Add , edit, Show , complete or Exit: ")
   user_input = user_input.strip()

   if user_input.startswith("add"): 
       todo = user_input[4:] + "\n"

       todos = fuctiones.get_todos()

       todos.append(todo)
       fuctiones.write_todos(todos)


   elif user_input.startswith("show"):

       todos = fuctiones.get_todos()

       for index, item in enumerate(todos) :
           item = item.strip("\n")
           row = f"{index + 1}-{item}"
           print(row)

   elif user_input.startswith("edit"):
       try:
           number = int(user_input[5:])
           number = number - 1
           todos =fuctiones.get_todos()
           new_to_do = input("Enter new to do: ") + '\n'
           todos[number] = new_to_do
           fuctiones.write_todos( todos)
       except ValueError :
           print("Your commend is not valid!")
           continue

   elif user_input.startswith("complete"):
       try:
           number = int(user_input[9:])
           todos =fuctiones.get_todos()
           index = number - 1
           to_do_remove = todos[index].strip('\n')
           todos.pop(index)
           fuctiones.write_todos(todos)
           massage = f"To do ({to_do_remove}) was removd. "
           print(massage)
       except IndexError :
           print("Thier is no to do with this number!")
           continue

   elif user_input.startswith("exit"):
       break
   else:
       print("Invalid input try agin. ")


print("Bay !")

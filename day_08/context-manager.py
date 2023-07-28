while True:
    user_input = input("Enter add, show, edit or complete : \n")
    user_input = user_input.strip()
    user_input = user_input.lower()

    match user_input:
        case 'add':
            add_todo = input('Add a to do : \n') + "\n"
            add_todo = add_todo.capitalize()

            # changes here using the "with context manager"
            with open('../todos.txt', 'r') as file:
                todos = file.readlines()
                todos.append(add_todo)
            with open('../todos.txt', 'w') as file:
                file.writelines(todos)
            # file = open('todos.txt', 'w')
            # file.writelines(todos)
        case 'show':
            with open('../todos.txt', 'r') as file:
                todos = file.readlines()
                todos = [todo.strip("\n") for todo in todos]
            # file = open('../todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            if len(todos) < 1:
                number_of_todos = len(todos)
                print(f'no todos available - {number_of_todos}')
            else:
                for i, todo in enumerate(todos):
                    o_todo = f"{i + 1}.{todo}"
                    print(o_todo)
        case 'complete':
            number = input("Enter input number of todo to complete: \n ")
            number = int(number) - 1
            with open('../todos.txt', 'r') as file:
                todos = file.readlines()
                removed_todo = todos.pop(number)
                removed_todo = removed_todo.strip("\n")
                message = f"{removed_todo} was removed from your todos"
            with open('../todos.txt', 'w') as file:
                file.writelines(todos)
                print(message)
        case 'edit':
            number = int(input("enter number of the todo edit: \n"))
            number = number - 1
            with open('../todos.txt', 'r') as file:
                todos = file.readlines()
            new_todo = input("enter a new todo: \n")
            todos[number] = new_todo + "\n"
            with open('../todos.txt', 'w') as file:
                file.writelines(todos)
        case 'end' | 'exit':
            break

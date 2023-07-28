while True:
    user_input = input("Enter add, show, edit or complete : \n")
    user_input = user_input.strip()
    user_input = user_input.lower()

    match user_input:
        case 'add':
            add_todo = input('Add a to do : \n') + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()
            add_todo = add_todo.capitalize()
            todos.append(add_todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
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
            todos.pop(number)
        case 'edit':
            print(todos)
        case 'end' | 'exit':
            break

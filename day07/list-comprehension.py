while True:
    user_input = input("Enter add, show, edit or complete : \n")
    user_input = user_input.strip()
    user_input = user_input.lower()

    match user_input:
        case 'add':
            add_todo = input('Add a to do : \n') + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            add_todo = add_todo.capitalize()
            todos.append(add_todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = []

            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)
            # print(todos)show
            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
            if len(todos) < 1:
                number_of_todos = len(todos)
                print(f'no todos available - {number_of_todos}')
            else:
                for i, todo in enumerate(todos):
                    o_todo = f"{i + 1}.{todo}"
        case 'complete':
            number = input("Enter input number of todo to complete: \n ")
            number = int(number) - 1
            todos.pop(number)
        case 'edit':
            print(todos)
        case 'end' | 'exit':
            break

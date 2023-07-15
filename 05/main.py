# print(user_input)

todos = []
while True:
    user_input = input("Enter add, show or edit : \n")

    match user_input:
        case 'add':
            add_todo = input('Add a to do : \n')
            add_todo = add_todo.capitalize()
            todos.append(add_todo)
        case 'show':
            if len(todos) < 1:
                print('no todos available')
            else:
                for todo in todos:
                    print(todo)
        case 'edit':
            print(todos)
        case 'end' | 'exit':
            break

# print(user_input)

todos = []
while True:
    user_input = input("Enter add, show, edit or complete : \n")

    match user_input:
        case 'add':
            add_todo = input('Add a to do : \n')
            add_todo = add_todo.capitalize()
            todos.append(add_todo)
        case 'show':
            if len(todos) < 1:
                number_of_todos = len(todos)
                print(f'no todos available - {number_of_todos}')
            else:
                for i, todo in enumerate(todos):
                    o_todo = f"{i +1}.{todo}"
                    print(o_todo)
        case 'complete':
            number = input("Enter input number of todo to complete: \n ")
            number = int(number) - 1
            todos.pop(number)
        case 'edit':
            print(todos)
        case 'end' | 'exit':
            break

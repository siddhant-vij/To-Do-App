from typing import List


def userTodo() -> str:
    todo: str = input("Enter a Todo: ")
    return todo


def printTodos(todos: List[str]) -> None:
    if len(todos) == 0:
        print("Nothing to show")
        return
    print("Todo List: ")
    idx = 0
    for todo in todos:
        print(idx + 1, "-", todo)
        idx += 1


def addTodoToAListOfTodos(todos: List[str]) -> List[str]:
    todo = userTodo()
    while todo != "":
        todos.append(todo)
        todo = userTodo()
    return todos


def menuItems() -> None:
    print("Todo App")
    print("1. Add")
    print("2. Show")
    print("0. Exit")


def driverCode() -> None:
    todoList: List[str] = []

    while True:
        menuItems()
        userAction: str = input("Enter your choice: ")

        if userAction == "0":
            print("Exiting...")
            break
        elif userAction == "1":
            todoList = addTodoToAListOfTodos(todoList)
        elif userAction == "2":
            printTodos(todoList)

        print("")


if __name__ == "__main__":
    driverCode()

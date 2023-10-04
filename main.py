import os
from typing import List, Tuple

todoFile = "todo.txt"
finishedFile = "finished.txt"


def userTodo() -> str:
    todo: str = input("Enter a Todo: ")
    return todo.strip()


def printTodos(todos: List[str]) -> None:
    if len(todos) == 0:
        print("Nothing to show")
        return
    print("Current Todo List: ")
    for idx, todo in enumerate(todos):
        print(f"{idx + 1}. {todo}")


def printFinishedTodos(finishedTodoList: List[str]) -> None:
    print("Finished Todo List: ")
    for idx, todo in enumerate(finishedTodoList):
        print(f"{idx + 1}. {todo}")


def getToDosFromFile(file: str) -> List[str]:
    if not os.path.exists(file):
        return []
    with open(file, "r") as file:
        return [todo.strip() for todo in file.readlines()]


def addTodoToAListOfTodos(todos: List[str]) -> List[str]:
    todos = getToDosFromFile(todoFile)
    print("Enter Todos below (Press enter to exit)...")
    todo = userTodo()
    while todo != "":
        todos.append(todo)
        with open(todoFile, "a") as file:
            file.writelines(todo + "\n")
        todo = userTodo()
    return todos


def validateTodoIndex(idx: str, todos: List[str]) -> None:
    try:
        idx = int(idx)
    except ValueError:
        print("Invalid index - not an integer")
        return -1
    if idx < 1 or idx > len(todos):
        print("Invalid index - out of range")
        return -1
    else:
        return int(idx) - 1


def editTodoInAListOfTodos(todos: List[str]) -> List[str]:
    if len(todos) == 0:
        print("Nothing to edit")
        return todos
    printTodos(todos)
    idx: str = input("Enter the index of the todo to edit: ")
    idx = validateTodoIndex(idx, todos)
    if idx == -1:
        return todos
    todo: str = input("Enter the new todo: ")
    todos[idx] = todo

    with open(todoFile, "w") as file:
        for todo in todos:
            file.writelines(todo + "\n")
    return todos


def deleteTodoFromAListOfTodos(todos: List[str]) -> List[str]:
    if len(todos) == 0:
        print("Nothing to delete")
        return todos
    printTodos(todos)
    idx: str = input("Enter the index of the todo to delete: ")
    idx = validateTodoIndex(idx, todos)
    if idx == -1:
        return todos
    todos.remove(todos[idx])

    with open(todoFile, "w") as file:
        for todo in todos:
            file.writelines(todo + "\n")
    return todos


def finishTodoFromAListOfTodos(todos: List[str], finishedTodoList: List[str]) -> Tuple[List[str], List[str]]:
    if len(todos) == 0:
        print("Nothing to finish")
        return todos, finishedTodoList
    printTodos(todos)
    idx: str = input("Enter the index of the todo to finish: ")
    idx = validateTodoIndex(idx, todos)
    if idx == -1:
        return todos, finishedTodoList
    finishedTodoList.append(todos[idx])
    with open(finishedFile, "w") as file:
        for fintodo in finishedTodoList:
            file.writelines(fintodo + "\n")

    todos.remove(todos[idx])
    with open(todoFile, "w") as file:
        for todo in todos:
            file.writelines(todo + "\n")
    return todos, finishedTodoList


def menuItems() -> None:
    print("Todo Application")
    print("1. Add Todos")
    print("2. Show Todos")
    print("3. Edit a Todo")
    print("4. Delete a Todo")
    print("5. Finish a Todo")
    print("0. Exit from App")


def driverCode() -> None:
    todoList: List[str] = getToDosFromFile(todoFile)
    finishedTodoList: List[str] = getToDosFromFile(finishedFile)

    while True:
        menuItems()
        userAction: str = input("Enter your choice: ")
        userAction = userAction.strip()

        if userAction == "0":
            print("Exiting the app...")
            break
        elif userAction == "1":
            todoList = addTodoToAListOfTodos(todoList)
        elif userAction == "2":
            printTodos(todoList)
            if len(finishedTodoList) != 0:
                printFinishedTodos(finishedTodoList)
        elif userAction == "3":
            todoList = editTodoInAListOfTodos(todoList)
        elif userAction == "4":
            todoList = deleteTodoFromAListOfTodos(todoList)
        elif userAction == "5":
            todoList, finishedTodoList = finishTodoFromAListOfTodos(
                todoList, finishedTodoList)
        else:
            print("Invalid choice - Try 1, 2, 3, 4, 5 or 0")

        print("")


if __name__ == "__main__":
    driverCode()

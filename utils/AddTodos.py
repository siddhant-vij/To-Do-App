from typing import List
from .CliHelpers import getToDosFromFile


def userTodo() -> str:
    todo: str = input("Enter a Todo: ")
    return todo.strip()


def addTodoToAListOfTodosCli(todos: List[str], todoFile: str) -> List[str]:
    print("Enter Todos below (Press enter to exit)...")
    todo = userTodo()
    while todo != "":
        todos.append(todo)
        print(f"Todo: {todo} - added\n")
        with open(todoFile, "a") as file:
            file.writelines(todo + "\n")
        todo = userTodo()
    return todos


def addTodoToAListOfTodosGui(todos: List[str], todoFile: str, todo: str) -> List[str]:
    todos.append(todo)
    with open(todoFile, "a") as file:
        file.writelines(todo + "\n")
    return todos

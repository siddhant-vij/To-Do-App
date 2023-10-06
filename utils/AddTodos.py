from typing import List
from .Helpers import getToDosFromFile


def userTodo() -> str:
    todo: str = input("Enter a Todo: ")
    return todo.strip()


def addTodoToAListOfTodos(todos: List[str], todoFile: str) -> List[str]:
    todos = getToDosFromFile(todoFile)
    print("Enter Todos below (Press enter to exit)...")
    todo = userTodo()
    while todo != "":
        todos.append(todo)
        print(f"Todo: {todo} - added\n")
        with open(todoFile, "a") as file:
            file.writelines(todo + "\n")
        todo = userTodo()
    return todos

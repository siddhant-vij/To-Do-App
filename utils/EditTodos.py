from typing import List
from .ShowTodos import printTodosCli
from .CliHelpers import validateTodoIndex


def editTodoInAListOfTodosCli(todos: List[str], todoFile: str) -> List[str]:
    if len(todos) == 0:
        print("Nothing to edit")
        return todos
    printTodosCli(todos)
    idx: str = input("\nEnter the index of the todo to edit: ")
    idx = validateTodoIndex(idx, todos)
    if idx == -1:
        return todos
    todo: str = input("Enter the new todo: ")
    oldTodo: str = todos[idx]
    todos[idx] = todo
    print(f"Todo: {oldTodo} - edited to Todo: {todo}")

    with open(todoFile, "w") as file:
        for todo in todos:
            file.writelines(todo + "\n")
    return todos


def editTodoInAListOfTodosGui(todos: List[str], todoFile: str, idx: int, new_todo: str) -> List[str]:
    todos[idx] = new_todo
    with open(todoFile, "w") as file:
        for todo in todos:
            file.writelines(todo + "\n")

    return todos

from typing import List
from .ShowTodos import printTodosCli
from .CliHelpers import validateTodoIndex


def deleteTodoFromAListOfTodosCli(todos: List[str], todoFile: str) -> List[str]:
    if len(todos) == 0:
        print("Nothing to delete")
        return todos
    printTodosCli(todos)
    idx: str = input("\nEnter the index of the todo to delete: ")
    idx = validateTodoIndex(idx, todos)
    if idx == -1:
        return todos
    print(f"Todo: {todos[idx]} - deleted")
    todos.remove(todos[idx])

    with open(todoFile, "w") as file:
        for todo in todos:
            file.writelines(todo + "\n")
    return todos


def deleteTodoFromAListOfTodosGui(todos: List[str], todoFile: str, idx: int) -> List[str]:
    todos.pop(idx)

    with open(todoFile, "w") as file:
        for todo in todos:
            file.writelines(todo + "\n")

    return todos

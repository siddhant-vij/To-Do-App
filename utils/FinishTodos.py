from typing import List, Tuple
from .ShowTodos import printTodosCli
from .CliHelpers import validateTodoIndex


def finishTodoFromAListOfTodosCli(todos: List[str], finishedTodoList: List[str], todoFile: str, finishedFile: str) -> Tuple[List[str], List[str]]:
    if len(todos) == 0:
        print("Nothing to finish")
        return todos, finishedTodoList
    printTodosCli(todos)
    idx: str = input("\nEnter the index of the todo to finish: ")
    idx = validateTodoIndex(idx, todos)
    if idx == -1:
        return todos, finishedTodoList
    finishedTodoList.append(todos[idx])
    print(f"Todo: {todos[idx]} - finished")
    with open(finishedFile, "w") as file:
        for fintodo in finishedTodoList:
            file.writelines(fintodo + "\n")

    todos.remove(todos[idx])
    with open(todoFile, "w") as file:
        for todo in todos:
            file.writelines(todo + "\n")
    return todos, finishedTodoList


def finishTodoFromAListOfTodosGui(todos: List[str], finishedTodoList: List[str], todoFile: str, finishedFile: str, idx: int) -> Tuple[List[str], List[str]]:
    finishedTodoList.append(todos[idx])
    with open(finishedFile, "w") as file:
        for fintodo in finishedTodoList:
            file.writelines(fintodo + "\n")

    todos.remove(todos[idx])
    with open(todoFile, "w") as file:
        for todo in todos:
            file.writelines(todo + "\n")

    return todos, finishedTodoList

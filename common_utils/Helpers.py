import os
from typing import List, Tuple


todoFile = "data/CurrentTodos.txt"
finishedFile = "data/FinishedTodos.txt"


def getToDosFromFile(file: str) -> List[str]:
    if not os.path.exists(file):
        return []
    with open(file, "r") as file:
        return [todo.strip() for todo in file.readlines()]


def initializeTodoLists(todoFile: str, finishedFile: str) -> Tuple[List[str], List[str]]:
    todoList = getToDosFromFile(todoFile)
    finishedTodoList = getToDosFromFile(finishedFile)
    return todoList, finishedTodoList

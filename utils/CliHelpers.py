import os
from typing import List


def menuItems() -> None:
    print("\nTodo Application\n")
    print("1. Add Todos")
    print("2. Show Todos")
    print("3. Edit a Todo")
    print("4. Delete a Todo")
    print("5. Finish a Todo")
    print("0. Exit from App")


def validateTodoIndex(idx: str, todos: List[str]) -> None:
    try:
        idx = int(idx)
    except ValueError:
        print("\nInvalid index - not an integer")
        return -1
    if idx < 1 or idx > len(todos):
        print("\nInvalid index - out of range")
        return -1
    else:
        return int(idx) - 1


def getToDosFromFile(file: str) -> List[str]:
    if not os.path.exists(file):
        return []
    with open(file, "r") as file:
        return [todo.strip() for todo in file.readlines()]

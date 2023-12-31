from typing import List


def printTodosCli(todos: List[str]) -> None:
    if len(todos) == 0:
        print("Nothing to show")
        return
    print("Current Todo List: ")
    for idx, todo in enumerate(todos):
        print(f"{idx + 1}. {todo}")


def printFinishedTodosCli(finishedTodoList: List[str]) -> None:
    print("Finished Todo List: ")
    for idx, todo in enumerate(finishedTodoList):
        print(f"{idx + 1}. {todo}")

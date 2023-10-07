from typing import List, Tuple
from cli import ShowTodos
from cli import CliHelpers
import PySimpleGUI as sg


def finishTodoFromAListOfTodosCli(todos: List[str], finishedTodoList: List[str], todoFile: str, finishedFile: str) -> Tuple[List[str], List[str]]:
    if len(todos) == 0:
        print("Nothing to finish")
        return todos, finishedTodoList
    ShowTodos.printTodosCli(todos)
    idx: str = input("\nEnter the index of the todo to finish: ")
    idx = CliHelpers.validateTodoIndex(idx, todos)
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


def handleFinishGui(todoList: List[str], finishedTodoList: List[str], todoFile: str, finishedFile: str, window: sg.Window, values: dict) -> Tuple[List[str], List[str]]:
    selected_todo = values["CurrentList"]
    if selected_todo:
        idx = todoList.index(selected_todo[0])
        todoList, finishedTodoList = finishTodoFromAListOfTodosGui(
            todoList, finishedTodoList, todoFile, finishedFile, idx)
        window["CurrentList"].update(todoList)
        sg.popup(f"Todo: {selected_todo[0]} - finished")
    return todoList, finishedTodoList
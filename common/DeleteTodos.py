from typing import List
from cli import ShowTodos
from cli import CliHelpers
import PySimpleGUI as sg


def deleteTodoFromAListOfTodosCli(todos: List[str], todoFile: str) -> List[str]:
    if len(todos) == 0:
        print("Nothing to delete")
        return todos
    ShowTodos.printTodosCli(todos)
    idx: str = input("\nEnter the index of the todo to delete: ")
    idx = CliHelpers.validateTodoIndex(idx, todos)
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


def handleDeleteGui(todoList: List[str], todoFile: str, window: sg.Window, values: dict) -> List[str]:
    selected_todo = values["CurrentList"]
    if selected_todo:
        idx = todoList.index(selected_todo[0])
        todoList = deleteTodoFromAListOfTodosGui(
            todoList, todoFile, idx)
        window["CurrentList"].update(todoList)
        sg.popup(f"Todo: {selected_todo[0]} - deleted")
    return todoList

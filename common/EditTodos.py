from typing import List
from cli import ShowTodos
from cli import CliHelpers
import PySimpleGUI as sg


def editTodoInAListOfTodosCli(todos: List[str], todoFile: str) -> List[str]:
    if len(todos) == 0:
        print("Nothing to edit")
        return todos
    ShowTodos.printTodosCli(todos)
    idx: str = input("\nEnter the index of the todo to edit: ")
    idx = CliHelpers.validateTodoIndex(idx, todos)
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


def handleEditGui(todoList: List[str], todoFile: str, window: sg.Window, values: dict) -> List[str]:
    selected_todo = values["CurrentList"]
    if selected_todo:
        idx = todoList.index(selected_todo[0])
        new_todo = sg.popup_get_text(
            'Enter the new todo', default_text=selected_todo[0])
        if new_todo and new_todo != selected_todo[0]:
            todoList = editTodoInAListOfTodosGui(
                todoList, todoFile, idx, new_todo)
            window["CurrentList"].update(todoList)
            sg.popup(f"Todo: {selected_todo[0]} - edited to Todo: {new_todo}")
        elif new_todo == selected_todo[0]:
            sg.popup("No edit made.")
    return todoList

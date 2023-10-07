from typing import List
import PySimpleGUI as sg


def userTodo() -> str:
    todo: str = input("Enter a Todo: ")
    return todo.strip()


def addTodoToAListOfTodosCli(todos: List[str], todoFile: str) -> List[str]:
    print("Enter Todos below (Press enter to exit)...")
    todo = userTodo()
    while todo != "":
        todos.append(todo)
        print(f"Todo: {todo} - added\n")
        with open(todoFile, "a") as file:
            file.writelines(todo + "\n")
        todo = userTodo()
    return todos

def addTodoToAListOfTodosGui(todos: List[str], todoFile: str, todo: str) -> List[str]:
    todos.append(todo)
    with open(todoFile, "a") as file:
        file.writelines(todo + "\n")
    return todos


def handleAddGui(todoList: List[str], todoFile: str, window: sg.Window, values: dict) -> List[str]:
    todo = values["InputText"].strip()
    todoList = addTodoToAListOfTodosGui(todoList, todoFile, todo)
    window["CurrentList"].update(todoList)
    window["InputText"].update("")
    sg.popup(f"Todo: {todo} - added")
    return todoList
from typing import List, Tuple
import PySimpleGUI as sg
from utils import AddTodos, DeleteTodos, EditTodos, FinishTodos, CliHelpers


listbox_width = 48


def initialize_todo_lists(todoFile: str, finishedFile: str) -> Tuple[List[str], List[str]]:
    todoList = CliHelpers.getToDosFromFile(todoFile)
    finishedTodoList = CliHelpers.getToDosFromFile(finishedFile)
    return todoList, finishedTodoList


def get_layout_current(todoList: List[str]) -> List[List[sg.Element]]:
    layout_current = [
        [sg.InputText(tooltip="Enter a Todo", key="InputText",
                      size=(listbox_width + 2, 1)), sg.Button("Add", key="AddBtn", size=(11, 1))],
        [sg.Listbox(todoList, size=(listbox_width, 10), key='CurrentList', enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_SINGLE),
            sg.Column([
                [sg.Button("Edit", key="EditBtn", size=(10, 1))],
                [sg.Button("Delete", key="DeleteBtn", size=(10, 1))],
                [sg.Button("Finish", key="FinishBtn", size=(10, 1))]
            ])],
        [sg.Button("Show Finished Todos", key="ShowFinished", size=(
            listbox_width - 5, 1)), sg.Button("Exit", size=(11, 1))]
    ]
    return layout_current


def get_layout_finished(finishedTodoList: List[str]) -> List[List[sg.Element]]:
    layout_finished = [
        [sg.InputText(tooltip="Todo", key="FinishedInputText", disabled=True, size=(
            listbox_width + 2, 1)), sg.Button("Add", key="AddBtn", disabled=True, size=(11, 1))],
        [sg.Listbox(finishedTodoList, size=(listbox_width, 10), key='FinishedList', enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_SINGLE),
            sg.Column([
                [sg.Button("Edit", key="EditBtn",
                           disabled=True, size=(10, 1))],
                [sg.Button("Delete", key="DeleteBtn",
                           disabled=True, size=(10, 1))],
                [sg.Button("Finish", key="FinishBtn",
                           disabled=True, size=(10, 1))]
            ])],
        [sg.Button("Show Current Todos", key="ShowCurrent", size=(
            listbox_width - 5, 1)), sg.Button("Exit", size=(11, 1))]
    ]
    return layout_finished


def handle_add(todoList: List[str], todoFile: str, window: sg.Window, values: dict) -> List[str]:
    todo = values["InputText"].strip()
    todoList = AddTodos.addTodoToAListOfTodosGui(todoList, todoFile, todo)
    window["CurrentList"].update(todoList)
    window["InputText"].update("")
    sg.popup(f"Todo: {todo} - added")
    return todoList


def handle_edit(todoList: List[str], todoFile: str, window: sg.Window, values: dict) -> List[str]:
    selected_todo = values["CurrentList"]
    if selected_todo:
        idx = todoList.index(selected_todo[0])
        new_todo = sg.popup_get_text(
            'Enter the new todo', default_text=selected_todo[0])
        if new_todo and new_todo != selected_todo[0]:
            todoList = EditTodos.editTodoInAListOfTodosGui(
                todoList, todoFile, idx, new_todo)
            window["CurrentList"].update(todoList)
            sg.popup(f"Todo: {selected_todo[0]} - edited to Todo: {new_todo}")
        elif new_todo == selected_todo[0]:
            sg.popup("No edit made.")
    return todoList


def handle_delete(todoList: List[str], todoFile: str, window: sg.Window, values: dict) -> List[str]:
    selected_todo = values["CurrentList"]
    if selected_todo:
        idx = todoList.index(selected_todo[0])
        todoList = DeleteTodos.deleteTodoFromAListOfTodosGui(
            todoList, todoFile, idx)
        window["CurrentList"].update(todoList)
        sg.popup(f"Todo: {selected_todo[0]} - deleted")
    return todoList


def handle_finish(todoList: List[str], finishedTodoList: List[str], todoFile: str, finishedFile: str, window: sg.Window, values: dict) -> Tuple[List[str], List[str]]:
    selected_todo = values["CurrentList"]
    if selected_todo:
        idx = todoList.index(selected_todo[0])
        todoList, finishedTodoList = FinishTodos.finishTodoFromAListOfTodosGui(
            todoList, finishedTodoList, todoFile, finishedFile, idx)
        window["CurrentList"].update(todoList)
        sg.popup(f"Todo: {selected_todo[0]} - finished")
    return todoList, finishedTodoList

from typing import List
import PySimpleGUI as sg


listbox_width = 48


def getLayoutCurrent(todoList: List[str]) -> List[List[sg.Element]]:
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


def getLayoutFinished(finishedTodoList: List[str]) -> List[List[sg.Element]]:
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

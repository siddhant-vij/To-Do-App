import PySimpleGUI as sg
from utils import GuiHelpers


def driverCode():
    todoFile = "data/CurrentTodos.txt"
    finishedFile = "data/FinishedTodos.txt"

    sg.theme("SystemDefault")

    todoList, finishedTodoList = GuiHelpers.initialize_todo_lists(todoFile, finishedFile)

    window = sg.Window("To-Do App", GuiHelpers.get_layout_current(todoList), finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "AddBtn":
            todoList = GuiHelpers.handle_add(todoList, todoFile, window, values)
        elif event == "EditBtn":
            todoList = GuiHelpers.handle_edit(todoList, todoFile, window, values)
        elif event == "DeleteBtn":
            todoList = GuiHelpers.handle_delete(todoList, todoFile, window, values)
        elif event == "FinishBtn":
            todoList, finishedTodoList = GuiHelpers.handle_finish(todoList, finishedTodoList, todoFile, finishedFile, window, values)
        elif event == "ShowFinished":
            window.close()
            window = sg.Window("To-Do App", GuiHelpers.get_layout_finished(finishedTodoList), finalize=True)
        elif event == "ShowCurrent":
            window.close()
            window = sg.Window("To-Do App", GuiHelpers.get_layout_current(todoList), finalize=True)

    window.close()


if __name__ == "__main__":
    driverCode()

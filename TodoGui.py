import PySimpleGUI as sg
from common_utils import AddTodos, EditTodos, DeleteTodos, FinishTodos, Helpers
from gui_utils import GuiHelpers


def runTodoGui() -> None:
    sg.theme("SystemDefault")

    todoList, finishedTodoList = Helpers.initializeTodoLists(
        Helpers.todoFile, Helpers.finishedFile)

    window = sg.Window(
        "To-Do App", GuiHelpers.getLayoutCurrent(todoList), finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "AddBtn":
            todoList = AddTodos.handleAddGui(
                todoList, Helpers.todoFile, window, values)
        elif event == "EditBtn":
            todoList = EditTodos.handleEditGui(
                todoList, Helpers.todoFile, window, values)
        elif event == "DeleteBtn":
            todoList = DeleteTodos.handleDeleteGui(
                todoList, Helpers.todoFile, window, values)
        elif event == "FinishBtn":
            todoList, finishedTodoList = FinishTodos.handleFinishGui(
                todoList, finishedTodoList, Helpers.todoFile, Helpers.finishedFile, window, values)
        elif event == "ShowFinished":
            window.close()
            window = sg.Window(
                "To-Do App", GuiHelpers.getLayoutFinished(finishedTodoList), finalize=True)
        elif event == "ShowCurrent":
            window.close()
            window = sg.Window(
                "To-Do App", GuiHelpers.getLayoutCurrent(todoList), finalize=True)

    window.close()


if __name__ == "__main__":
    runTodoGui()

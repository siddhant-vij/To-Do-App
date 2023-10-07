from typing import List
from common import AddTodos, EditTodos, DeleteTodos, FinishTodos, Helpers
from cli import CliHelpers, ShowTodos


def runTodoCli() -> None:
    todoList, finishedTodoList = Helpers.initializeTodoLists(
        Helpers.todoFile, Helpers.finishedFile)

    while True:
        CliHelpers.menuItems()
        userAction: str = input("\nEnter your choice: ")
        print("")
        userAction = userAction.strip()

        if userAction == "0":
            print("Exiting the app...")
            break
        elif userAction == "1":
            todoList = AddTodos.addTodoToAListOfTodosCli(
                todoList, Helpers.todoFile)
        elif userAction == "2":
            ShowTodos.printTodosCli(todoList)
            if len(finishedTodoList) != 0:
                print("")
                ShowTodos.printFinishedTodosCli(finishedTodoList)
        elif userAction == "3":
            todoList = EditTodos.editTodoInAListOfTodosCli(
                todoList, Helpers.todoFile)
        elif userAction == "4":
            todoList = DeleteTodos.deleteTodoFromAListOfTodosCli(
                todoList, Helpers.todoFile)
        elif userAction == "5":
            todoList, finishedTodoList = FinishTodos.finishTodoFromAListOfTodosCli(
                todoList, finishedTodoList, Helpers.todoFile, Helpers.finishedFile)
        else:
            print("Invalid choice - Try 1, 2, 3, 4, 5 or 0")

        print("")


if __name__ == "__main__":
    runTodoCli()

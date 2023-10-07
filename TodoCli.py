from typing import List
from utils import AddTodos, CliHelpers, DeleteTodos, EditTodos, FinishTodos, ShowTodos


todoFile = "data/CurrentTodos.txt"
finishedFile = "data/FinishedTodos.txt"


def runTodoApp() -> None:
    todoList: List[str] = CliHelpers.getToDosFromFile(todoFile)
    finishedTodoList: List[str] = CliHelpers.getToDosFromFile(finishedFile)

    while True:
        CliHelpers.menuItems()
        userAction: str = input("\nEnter your choice: ")
        print("")
        userAction = userAction.strip()

        if userAction == "0":
            print("Exiting the app...")
            break
        elif userAction == "1":
            todoList = AddTodos.addTodoToAListOfTodosCli(todoList, todoFile)
        elif userAction == "2":
            ShowTodos.printTodosCli(todoList)
            if len(finishedTodoList) != 0:
                print("")
                ShowTodos.printFinishedTodosCli(finishedTodoList)
        elif userAction == "3":
            todoList = EditTodos.editTodoInAListOfTodosCli(todoList, todoFile)
        elif userAction == "4":
            todoList = DeleteTodos.deleteTodoFromAListOfTodosCli(
                todoList, todoFile)
        elif userAction == "5":
            todoList, finishedTodoList = FinishTodos.finishTodoFromAListOfTodosCli(
                todoList, finishedTodoList, todoFile, finishedFile)
        else:
            print("Invalid choice - Try 1, 2, 3, 4, 5 or 0")

        print("")


if __name__ == "__main__":
    runTodoApp()

from typing import List
from utils import AddTodos, DeleteTodos, EditTodos, FinishTodos, Helpers, ShowTodos


todoFile = "CurrentTodos.txt"
finishedFile = "FinishedTodos.txt"


def runTodoApp() -> None:
    todoList: List[str] = Helpers.getToDosFromFile(todoFile)
    finishedTodoList: List[str] = Helpers.getToDosFromFile(finishedFile)

    while True:
        Helpers.menuItems()
        userAction: str = input("\nEnter your choice: ")
        print("")
        userAction = userAction.strip()

        if userAction == "0":
            print("Exiting the app...")
            break
        elif userAction == "1":
            todoList = AddTodos.addTodoToAListOfTodos(todoList, todoFile)
        elif userAction == "2":
            ShowTodos.printTodos(todoList)
            if len(finishedTodoList) != 0:
                print("")
                ShowTodos.printFinishedTodos(finishedTodoList)
        elif userAction == "3":
            todoList = EditTodos.editTodoInAListOfTodos(todoList, todoFile)
        elif userAction == "4":
            todoList = DeleteTodos.deleteTodoFromAListOfTodos(
                todoList, todoFile)
        elif userAction == "5":
            todoList, finishedTodoList = FinishTodos.finishTodoFromAListOfTodos(
                todoList, finishedTodoList, todoFile, finishedFile)
        else:
            print("Invalid choice - Try 1, 2, 3, 4, 5 or 0")

        print("")


if __name__ == "__main__":
    runTodoApp()

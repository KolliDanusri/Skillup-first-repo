'' Design and implement a simple TEXT EDITOR using the STACK data structure
The editor should allow the user to continuously type text and perform different operations through a menu-driven program.

The application must support the following operations:
1. Add new text to the editor
2.Display the current text
3.Undo the last operation
4.exit the application '''
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []

    def add_text(self, new_text):
        self.undo_stack.append(self.text)   # Save current state
        self.text += new_text
        print("Text added successfully!")

    def display_text(self):
        if self.text == "":
            print("Editor is empty.")
        else:
            print("Current Text:", self.text)

    def undo(self):
        if len(self.undo_stack) == 0:
            print("Nothing to undo!")
        else:
            self.text = self.undo_stack.pop()
            print("Last operation undone.")

def main():
    editor = TextEditor()

    while True:
        print("\n--- TEXT EDITOR ---")
        print("1. Add New Text")
        print("2. Display Current Text")
        print("3. Undo Last Operation")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_text = input("Enter text: ")
            editor.add_text(new_text)

        elif choice == 2:
            editor.display_text()

        elif choice == 3:
            editor.undo()

        elif choice == 4:
            print("Exiting Text Editor...")
            break

        else:
            print("Invalid choice! Please try again.")

main()
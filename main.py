from processing.welcome import password
from processing.select_file import select_file
from processing.bubblesheet_class import BubbleSheet, load_bubblesheet
from processing.home_menu import display_home_menu
from processing.tools.show_questions import show_questions
    # from processing.tools.add_question import add_question
password()
filename = select_file()
bubblesheet = load_bubblesheet(filename)
print(bubblesheet)

def main(): 
    display_home_menu()
    choice = input("Please enter your choice (1, 2, or 3): ")
    if choice == '1':
        print("Showing questions...")
        show_questions(bubblesheet)
        main()  # Return to the main menu after showing questions
    elif choice == '2':
        print("Adding questions...")
        # Code to add questions goes here
    elif choice == '3':
        print("Exiting the app. Goodbye!")
        return
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


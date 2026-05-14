from processing.welcome import password
from processing.select_file import select_file
from processing.bubblesheet_class import BubbleSheet, load_bubblesheet
from processing.home_menu import display_home_menu
from processing.tools.show_questions import show_questions
from processing.tools.add_question import add_question
from processing.horizontal_line import horizontal_line
from processing.check_ids import check_ids

read_only = True

def main(): 
    display_home_menu()
    choice = input("Please enter your choice (1, 2, 3, or 4.): ")
    horizontal_line()
    if choice == '1':
        print("Showing questions...")
        show_questions(bubblesheet)
        input("Press enter to return to the main menu...")
        horizontal_line()
        main()  # Return to the main menu after showing questions
    elif choice == '2':
        print("Adding questions...")
        if not read_only:
            add_question(bubblesheet)
        else:
            print("Cannot add questions in read-only mode.")
        main()  # Return to the main menu after adding a question
    elif choice == '3':
        print("Saving and exiting the app. Goodbye!")
        horizontal_line()
        from processing.bubblesheet_class import save_bubblesheet
        save_bubblesheet(bubblesheet, filename)
    elif choice == '4':
        print("Exiting the app. Goodbye!")
        return
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        horizontal_line()
        main()  # Return to the main menu after an invalid choice

# Startup process

horizontal_line()
password()
horizontal_line()
filename = select_file()
horizontal_line()
bubblesheet = load_bubblesheet(filename)
horizontal_line()
print(bubblesheet)
horizontal_line()
read_only = check_ids(bubblesheet)
horizontal_line()
main()




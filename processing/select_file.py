from pathlib import Path

from processing.horizontal_line import horizontal_line


def select_file():
    print("Do you want to create a new .bubblesheet file, or use an existing one? \nEnter 1 to use an existing file, or 2 to create a new one.")
    choice = input("Enter your choice (1 or 2): ")
    if choice=='1':
        print("Please place a file in the data folder, and then press Enter to continue.")
        input("Press enter to continue...")
        horizontal_line()
        filename = Path(input("Please enter the name of the file you want to use (excluding the .bubblesheet extension): ")).stem
        try :
            with open(f'data/{filename}.bubblesheet', 'r') as file:
                print("File found! Continuing...")
        except FileNotFoundError:
            print("File not found. Please place a file in the data folder and try again.")
            select_file()
        return filename
    elif choice=='2':
        return Path('default')

"""
tells a user if the file they entered is valid, and if not, prompts them to enter a new file name
args: none
returns: filename (str)

"""
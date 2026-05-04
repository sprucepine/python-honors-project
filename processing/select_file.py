from pathlib import Path


def select_file():
    print("Please place a file in the data folder, and then press Enter to continue.")
    input("Press enter to continue...")
    filename = Path(input("Please enter the name of the file you want to use (excluding the .bubblesheet extension): ")).stem
    try :
        with open(f'data/{filename}.bubblesheet', 'r') as file:
            print("File found! Continuing...")
    except FileNotFoundError:
        print("File not found. Please place a file in the data folder and try again.")
        select_file()
    return filename

"""
tells a user if the file they entered is valid, and if not, prompts them to enter a new file name
args: none
returns: filename (str)

"""
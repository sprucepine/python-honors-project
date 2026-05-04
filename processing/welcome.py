def password():
    while True:
        userInput = input("Input the access code (\"q\" to quit): ")
        if userInput == "q":
            break
            print("Login stopped. You must restart the program in order to continue.")
        elif userInput == "1234":
            print("Access granted.")
            break
"""
locks access to the function without a password
args: none
returns: none
"""
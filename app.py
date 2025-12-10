def greet(name):
    return f"Hello, {name}! Welcome to the app."
def farewell(name):
    return f"Goodbye, {name}! See you next time."
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    print(farewell(user_name))

def greet_decor(func):

    def wrapper(name):
        print(f"Preparing to greet {name}")
        func(name)
        print(f"Greeted {name} successfully.")

    return wrapper


@greet_decor
def greet(name):
    print(f"Hello, {name}")


greet("Bibek")

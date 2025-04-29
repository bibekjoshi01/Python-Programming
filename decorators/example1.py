def decor_func(func):
    def inner():
        print("Before the function runs.")
        func()
        print("After the function runs.")
    
    return inner


@decor_func
def say_hello():
    print("Hello !")


say_hello()

# Note: 
# Here, @decor_func is syntactic sugar for:
# say_hello = my_decorator(say_hello)


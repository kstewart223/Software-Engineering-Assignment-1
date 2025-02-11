def my_decorator(func):
    def wrapper():
        print("I love Animals!")
        func()
        print("And I also love golf.")
    return wrapper

@my_decorator
def best_class():
    print("I love Software Engineering!")

best_class()
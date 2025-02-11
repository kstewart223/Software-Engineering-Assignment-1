def my_decorator(func):
    def wrapper():
        print("I Hate Robots")
        func()
        print("And I also hate golf!")
    return wrapper

@my_decorator
def best_class():
    print("I Hate Writing Papers")

best_class()
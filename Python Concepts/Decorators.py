def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def greet(name, etext):
    print(f"Hello {name} {etext}")


greet("World", "How are you?")

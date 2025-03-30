def count_decorator_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Function '{func.__name__}' has been called {wrapper.count} times")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


# function calls
@count_decorator_calls
def say_hi():
    print("Hi!")


@count_decorator_calls
def say_cheers():
    print("Cheers!")


# Testing the decorator
say_hi()
say_cheers()
say_hi()

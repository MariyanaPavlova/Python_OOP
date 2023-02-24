def logged(func):
    def wrapper(*args):
        func_name = func.__name__
        func_res = func(*args)

        return f'you called {func_name}{args}\nit returned {func_res}'
    return wrapper

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
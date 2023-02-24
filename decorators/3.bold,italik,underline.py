def make_underline(func):
    def wrapper(*args):
        func_res = func(*args)
        return f'<u>{func_res}</u>'

    return wrapper


def make_italic(func):
    def wrapper(*args):
        func_res = func(*args)
        return f'<i>{func_res}</i>'

    return wrapper


def make_bold(func):
    def wrapper(*args):
        func_res = func(*args)
        return f'<b>{func_res}</b>'

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
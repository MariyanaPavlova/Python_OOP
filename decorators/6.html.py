def tags(tag_name):
    def decorator(func):
        def wrapper(*args):
            func_res = func(*args)
            return f'<{tag_name}>{func_res}</{tag_name}>'
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
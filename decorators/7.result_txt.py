def store_results(funct):
    def wrapped(*args):
        res = funct(*args)
        with open('./resul.txt', 'a') as file:
            file.write(f"Function '{funct.__name__}' was called. Result {res}\n")
    return wrapped


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
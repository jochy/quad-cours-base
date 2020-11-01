
def calculator(operation, a, b):
    if operation == '+':
        return sum(a, b)
    else:
        raise RuntimeError()


def sum(a, b):
    return a + b


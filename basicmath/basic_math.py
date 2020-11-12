
def calculator(operation, a, b):
    store_operation_in_database(operation, a, b)
    if operation == '+':
        return sum(a, b)
    else:
        raise RuntimeError()


def sum(a, b):
    return a + b


def store_operation_in_database(operation, a, b):
    f = open("logs.txt", "w+")
    f.write(str(a) + " " + operation + " " + str(b))
    f.close()

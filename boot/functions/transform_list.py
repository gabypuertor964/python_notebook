# Sumar 1 a cada elemento de una lista de números
def next(numbers: list[int|float]):
    for key, value in enumerate(numbers):
        numbers[key] = value + 1

    return numbers

# Restar 1 a cada elemento de una lista de números
def prev(numbers: list[int|float]):
    for key, value in enumerate(numbers):
        numbers[key] = value - 1

    return numbers

# Duplicar el valor de cada elemento
def double(numbers: list[int|float]):
    for key, value in enumerate(numbers):
        numbers[key] = value * 2

    return numbers

def execute(function, numbers: list[int|float]):
    print(function(numbers))

execute(next, [1, 2, 3, 4, 5])
execute(prev, [1, 2, 3, 4, 5])
execute(double, [1, 2, 3, 4, 5])

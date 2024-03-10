# Promediar una lista de números
def summary(numbers: list[int|float]):
    return sum(numbers) / len(numbers)

# Elevar al cuadrado un número
def pow(number: int|float):
    return number ** 2

# Ejecutar las funciones
def execute(numbers: list[int|float], function_1, function_2):
    
    # Elevar al cuadrado cada elemento de una lista de números
    for key, value in enumerate(numbers):
        numbers[key] = function_1(value)

    # Promediar y mostrar el resultado
    print(f"Los numeros elevados al cuadrado son: {numbers} y su promedio es: {function_2(numbers)}")

execute([1, 2, 3, 4, 5], pow, summary)
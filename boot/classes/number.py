from roman import toRoman, fromRoman

# Clase Numero
class Number:
    
    # Metodo constructor
    def __init__(self, number: int|float):
        if self.verify_number(number):
            self.number = number
            self.roman = toRoman(number)
        else:
            raise TypeError("El valor ingresado no es un numero")

    @staticmethod
    def verify_number(number):
        try:
            return isinstance(number, (int, float))
        except:
            return False

    @staticmethod
    def verify_roman(roman):
        try:
            fromRoman(roman)
            return True
        except:
            return False

    # Imprimir la informacion del objeto
    def __str__(self):
        return f"El numero {self.number} en romano es {self.roman}"

    # Sumar otro numero romano
    def add(self, roman_number: str):
        
        if self.verify_roman(roman_number):
            # Convertir el romano a numero
            number = fromRoman(roman_number)

            # Sumar el numero romano al numero actual
            self.number += number
            self.roman = toRoman(self.number)
        else:
            raise TypeError("El valor ingresado no es un numero romano")

# Clase MejorNumero
class BetterNumber(Number):

    def __init__(self, number: int|float):
        super().__init__(number)

    # Restar otro numero romano
    def subtract(self, roman_number: str):

        if self.verify_roman(roman_number):
            # Convertir el romano a numero
            number = fromRoman(roman_number)

            # Restar el numero romano al numero actual
            self.number -= number
            self.roman = toRoman(self.number)
        else:
            raise TypeError("El valor ingresado no es un numero romano")

    # Multiplicar por otro numero romano
    def multiply(self, roman_number: str):

        if self.verify_roman(roman_number):
            # Convertir el romano a numero
            number = fromRoman(roman_number)

            # Multiplicar el numero romano al numero actual
            self.number *= number
            self.roman = toRoman(self.number)
        else:
            raise TypeError("El valor ingresado no es un numero romano")

    # Sumar una lista de numeros romanos
    @staticmethod
    def add_from_list(numbers: list[int|float]):
        total = 0

        for number in numbers:

            if Number.verify_roman(number):
                total += fromRoman(number)
            else:
                return f"El valor {number} no es un numero romano"

        return total

number_1 = Number(100)        
print(f"Instanciamiento de la clase Number: {number_1}")

number_1.add("X")
print(f"Suma de un numero romano: {number_1}")



number_2 = BetterNumber(120)
print(f"Instanciamiento de la clase BetterNumber: {number_2}")

number_2.subtract("X")
print(f"Resta de un numero romano: {number_2}")

number_2.multiply("X")
print(f"Multiplicacion de un numero romano: {number_2}")



print(f"Suma de una lista de numeros romanos: {BetterNumber.add_from_list(["X", "X", "X"])}")
import os
import sys
from tabulate import tabulate

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.display.titles import title
from tools.input.get import wait

# Ejercicio 1 (Clase Student con propiedades publicas)
title("Ejercicio 1", False)

class Student:

    # Metodo constructor
    def __init__(self, name:str, califications: list[int|float]):
        self.name = name

        # Verificar que las calificaciones sean numeros
        for calification in califications:
            if not isinstance(calification, (int, float)):
                raise ValueError('Las calificaciones deben ser numeros')

        self.califications = califications

    # Calcular y retornar el promedio academico
    def get_average(self):
        return sum(self.califications) / len(self.califications)
    
    # Imprimir la informacion del estudiante
    def print_information(self):
        print(tabulate(
            # Valores de la tabla
            [
                ['Nombre', self.name],
                ['Calificaciones', self.califications],
                ['Promedio', self.get_average()]
            ],

            # Encabezados de la tabla
            headers=['Atributo', 'Valor'],

            # Estilo de la tabla
            tablefmt='fancy_grid'
        ))

# Instanciar un objeto de tipo Student
student = Student('Juan', [10, 9, 8, 7, 6, 5])

# Imprimir la informacion del estudiante
student.print_information()

# Ejercicio 2,3,4,5 (Propiedades privadas, Comportamiento al imprimir el objeto, Cambio simulataneo de la institucion y control numerico, impresion escalas)
title("Ejercicio 5", False)

class Student:

    # Atributo: Nombre institucion
    institution:str = "SENA"

    # Atributo: Cantidad de estudiantes
    __students_count: int = 0

    # Visualizar la lista de calificaciones
    @staticmethod
    def verify_califications(califications: list[int|float]):
        for calification in califications:
            if not isinstance(calification, (int, float)):
                raise ValueError('Las calificaciones deben ser numeros')
        
        return califications

    # Cambiar la institucion
    @classmethod
    def set_institution(cls, institution:str):
        cls.institution = institution

    # Imprimir escala de calificaciones
    @staticmethod
    def print_scale():
        print(tabulate(
            # Valores de la tabla
            [
                ['0 a 2.9', 'BAJA'],
                ['3 a 3.9', 'MEDIA'],
                ['4 a 4.5', 'ALTA'],
                ['4.6 a 5', 'SOBRESALIENTE'],
            ],

            # Encabezados de la tabla
            headers=['Nota', 'Escala'],

            # Estilo de la tabla
            tablefmt='fancy_grid'
        ))

    # Metodo constructor
    def __init__(self, name:str, califications: list[int|float], institution:str = None):
        self.__name = name
        self.__califications = self.verify_califications(califications)

        # Cambiar la institucion si se especifica
        if institution != None:
            self.set_institution(institution)

        # Incrementar la cantidad de estudiantes
        Student.__students_count += 1

    # Calcular y retornar el promedio academico
    def __get_average(self):
        return sum(self.__califications) / len(self.__califications)
    
    # Imprimir la informacion del estudiante
    def print_information(self):
        print(tabulate(
            # Valores de la tabla
            [
                ['Nombre', self.__name],
                ['Calificaciones', self.__califications],
                ['Promedio', self.__get_average()]
            ],

            # Encabezados de la tabla
            headers=['Atributo', 'Valor'],

            # Estilo de la tabla
            tablefmt='fancy_grid'
        ))

    # Declarar el comportamiento al imprimir el objeto
    def __str__(self):
        return f'Nombre: {self.__name}, Promedio: {self.__get_average()}'

# Imprimir escala de calificaciones
Student.print_scale()

wait()
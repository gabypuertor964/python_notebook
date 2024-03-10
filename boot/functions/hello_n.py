def execute():

    # Variable de control de ejecuciones
    number_execution = 1

    # Subfuncion saludar
    def hello():
        nonlocal number_execution
        print(f"Hello {number_execution}")
        number_execution += 1

    return hello

hello = execute()
hello()
hello()
hello()
hello()
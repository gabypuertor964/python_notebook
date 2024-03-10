def transform_str(string: str) -> str:
    
    # Reemplazar la letra "a" por "@"
    def replace_a():
        nonlocal string
        string = string.replace("a", "@")

    # Cambiar a letras minusculas
    def lower():
        nonlocal string
        string = string.lower()

    # Eliminar los espacios al comienzo y final de la cadena
    def remove_spaces():
        nonlocal string
        string = string.strip()

    # Eliminar a todos los numeros de la cadena
    def remove_numbers():
        nonlocal string
        string = ''.join([i for i in string if not i.isdigit()])

    # Ejecutar las funciones
    replace_a()
    lower()
    remove_spaces()
    remove_numbers()

    print(f"La cadena transformada es: {string}")

transform_str(input("Ingrese una cadena de texto: "))
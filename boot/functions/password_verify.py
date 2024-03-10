# Validar la longitud de la contraseña
def validate_length(password: str, length: int = 8) -> bool:
    if len(password) < length:
        return False
    return True

# Validar si la contraseña tiene caracteres especiales
def special_characters(password:str) -> bool:
    special_characters = ["!", "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
    
    for character in password:
        if character in special_characters:
            return False
    return True

# Manejador principal
def execute(password: str, function_1, function_2):
    if function_1(password) and function_2(password):
        print("La contraseña es válida")
    else:
        print("La contraseña no es válida")

execute("a", validate_length, special_characters)
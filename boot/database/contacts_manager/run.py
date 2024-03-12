from database import Contact

# Crear la tabla
print(Contact.create_table())

# Crear un registro
print(Contact.create("Juan","Perez","1234567890"))

# Obtener todos los registros
registers = Contact.select()

# Imprimir todos los registros
print(registers)

# Obtener un registro segun su id
for register in registers["result"]:
    print(Contact.delete(register))

print(Contact.select())


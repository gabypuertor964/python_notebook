import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from tools.display.titles import title
from tools.display.text_align import left
from tabulate import tabulate
from uuid import uuid4

# Clase Cuenta
class Account:

    # Metodo constructor
    def __init__(self, balance: float, interest):
        self.__id = uuid4()
        self.__balance = balance
        self.__interest = interest

    # Getters Methods    
    def get_balance(self):
        return self.__balance
    
    def get_interest(self):
        return self.__interest

    def set_balance(self, balance: float):
        self.__balance = balance

# Subclase Cuenta de Ahorros
class SavingAccount(Account):

    # Metodo constructor
    def __init__(self, balance: float, interest: float):
        super().__init__(balance,interest)

    # Aplicar Interes
    def apply_interest(self):

        # Obtener el balance actual de la cuenta
        balance = self.get_balance()

        # Actualizar el valor
        self.set_balance(balance + balance * self.get_interest())

# Subclase Cuenta Corriente
class CurrentAccount(Account):

    # Metodo constructor
    def __init__(self, balance: float, interest: float):
        super().__init__(balance,interest)

    # Aplicar Descuento segun tasa de interes
    def apply_discount(self):

        # Obtener el balance actual de la cuenta
        balance = self.get_balance()

        # Actualizar el valor
        self.set_balance(balance - balance * self.get_interest())

# Clase Cliente
class Client:

    # Metodo constructor
    def __init__(self, document: int, name: str, account):
        self.__document = document
        self.__name = name
        self.__account = account

    # Getters Methods
    def get_document(self):
        return str(self.__document)
    
    def get_name(self):
        return self.__name

    def get_account(self):
        return self.__account

    # Imprimir la informacion del cliente
    def __str__(self):
        return tabulate(
            # Valores de la tabla
            [
                ['Documento', self.get_document()],
                ['Nombre', self.get_name()],
                ['Saldo', self.get_account().get_balance()],
                ['Interes', self.get_account().get_interest()]
            ],

            # Encabezados de la tabla
            headers=['Atributo', 'Valor'],

            # Estilo de la tabla
            tablefmt='fancy_grid'
        )

# Clase Banco
class Bank:

    # Metodo constructor
    def __init__(self, name: str):
        self.__name = name
        self.__clients = []

    # Agregar un cliente
    def add_client(self, *args):
        for client in args:
            self.__clients.append(client)

    # Obtener el numero de clientes
    def get_num_clients(self):
        return len(self.__clients)

    # Retornar el listado de clientes
    def get_clients(self):

        # Inicializar la lista
        clients_list = []

        # Recorrer los clientes
        for client in self.__clients:
            clients_list.append([
                client.get_document(),
                client.get_name()
            ])

        return clients_list

    # Ver la informacion de los clientes
    def show_clients(self):
        print(tabulate(
            self.get_clients(),
            headers=['Documento', 'Nombre'],
            tablefmt='fancy_grid'
        ))

    # Obtener el total de saldo de cuentas de ahorro
    def get_total_savings(self):

        # Inicializar el total
        total = 0

        # Iterar los elementos
        for client in self.__clients:

            # Obtener la cuenta
            account = client.get_account()

            if isinstance(account, SavingAccount):
                total += account.get_balance()

        # Retornar el total
        return total

    # Obtener el total de saldo de cuentas Corriente
    def get_total_current(self):

        # Inicializar el total
        total = 0

        # Iterar los elementos
        for client in self.__clients:

            # Obtener la cuenta
            account = client.get_account()

            if isinstance(account, CurrentAccount):
                total += account.get_balance()

        # Retornar el total
        return total

    # Obtener el total de saldo en la bobeda
    def get_total_balance(self):
        return self.get_total_savings() + self.get_total_current()

    # Imprimir la informacion del banco
    def __str__(self):
        return tabulate(
            # Valores de la tabla
            [
                ['Nombre', self.__name],
                ['Clientes', self.get_num_clients()],
                ['Total en Cuentas de Ahorros', self.get_total_savings()],
                ['Total en Cuentas Corriente', self.get_total_current()],
                ['Total en la Bobeda', self.get_total_balance()]
            ],

            # Encabezados de la tabla
            headers=['Atributo', 'Valor'],

            # Estilo de la tabla
            tablefmt='fancy_grid'
        
        )

# Titulo
title("Instanciamiento del Banco", False)

# Instanciamiento del banco
new_bank = Bank("Banco Caja social")

# Imprimir la informacion del banco
print(new_bank)



# Titulo
title("Creacion y guardado de clientes", False)

# Creacion de clientes
client_1 = Client(123456789, "Jose Perez", SavingAccount(1000000, 0.05))
client_2 = Client(987654321, "Maria Lopez", CurrentAccount(5000000,0.03))

# Guardado de los registros en el banco
new_bank.add_client(client_1,client_2)

# Imprimir la informacion del banco
print(new_bank)



# Titulo
title("Informacion de los clientes", False)

# Imprimir la informacion de los clientes
new_bank.show_clients()


# Titulo
title("Aplicacion de interes y descuento", False)

print(left("Cuenta 1"),end="\n\n")
# Datos anteriores
print(client_1)

# Aplicar interes a la cuenta de ahorros e imprimir la informacion
client_1.get_account().apply_interest()
print(client_1)


print(left("Cuenta 2"),end="\n\n")
# Datos anteriores
print(client_2)

# Aplicar descuento a la cuenta corriente e imprimir la informacion
client_2.get_account().apply_discount()
print(client_2)


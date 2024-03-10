import os
import sys
from uuid import uuid4

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.display.titles import title

# Declaracion de clase
class AccountBank:

    # Metodo estatico: Depositar
    @staticmethod
    def deposit(account, amount: float) -> float:
        
        try:
            # Validacion de monto
            if float(amount) <= 0:
                raise ValueError("El monto a depositar debe ser mayor a 0")

            # Obtener saldo actual
            old_balance = account.get_balance()

            # Deposito
            account.set_balance(old_balance + amount)

            return {
                'status': True,
                'message': 'Deposito exitoso',
                'old_balance': old_balance,
                'balance': account.get_balance()
            }

        # Manejo de excepciones
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }
    
    # Metodo estatico: Retirar
    @staticmethod
    def withdraw(account, amount: float) -> float:
        
        try:

            # Validacion de monto
            if float(amount) <= 0:
                raise ValueError("El monto a retirar debe ser mayor a 0")
            
            # Validacion de saldo disponible
            if account.get_balance() < amount:
                raise ValueError("Saldo insuficiente")

            # Obtener saldo actual
            old_balance = account.get_balance()

            # Retiro
            account.set_balance(old_balance - amount)

            return {
                'status': True,
                'message': 'Retiro exitoso',
                'old_balance': old_balance,
                'balance': account.get_balance()
            }

        # Manejo de excepciones
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

    # Metodo estatico: Transferir solo entre cuentas de la misma moneda
    @staticmethod
    def transfer(account_origin, account_destiny, amount: float) -> float:
        
        try:

            # Validacion de monto
            if float(amount) <= 0:
                raise ValueError("El monto a transferir debe ser mayor a 0")
            
            # Validacion de saldo disponible
            if account_origin.get_balance() < amount:
                raise ValueError("Saldo insuficiente")
            
            # Validacion de moneda
            if account_origin.get_currency() != account_destiny.get_currency():
                raise ValueError("Las cuentas deben ser de la misma moneda para realizar la transferencia")

            # Obtener saldo actual
            old_balance_origin = account_origin.get_balance()
            old_balance_destiny = account_destiny.get_balance()

            # Retiro de cuenta origen
            account_origin.set_balance(old_balance_origin - amount)

            # Deposito en cuenta destino
            account_destiny.set_balance(old_balance_destiny + amount)

            return {
                'status': True,
                'message': 'Transferencia exitosa',
                'old_balance_origin': old_balance_origin,
                'balance_origin': account_origin.get_balance(),
                'old_balance_destiny': old_balance_destiny,
                'balance_destiny': account_destiny.get_balance()
            }

        # Manejo de excepciones
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

    # Metodo constructor
    def __init__(self, account_holder: str, balance: float, account_number: str = uuid4(), currency: str = "COP"):
        
        # Atributos
        self.__account_holder = account_holder
        self.__balance = balance
        self.__account_number = account_number
        self.__currency = currency

    # Getters
    def get_balance(self):
        return self.__balance

    def get_currency(self):
        return self.__currency

    # Setters
    def set_balance(self, balance: float):
        self.__balance = balance

    def set_currency(self, currency: str):
        self.currency = currency

    # Metodo de impresion
    def get_info(self):
        return {
            'account_holder': self.__account_holder,
            'balance': self.__balance,
            'account_number': self.__account_number,
            'currency': self.__currency
        }

title("Operaciones con cuentas bancarias")

# Instanciamineto y visualizacion de la informacion de la cuenta
account_1 = AccountBank("Juan Perez", 100000)
print(f"Informacion de la cuenta 1: {account_1.get_info()}", end="\n\n")

# Instanciamineto y visualizacion de la informacion de la cuenta
account_2 = AccountBank("Maria Gomez", 5000000)
print(f"Informacion de la cuenta 2: {account_2.get_info()}", end="\n\n")

# Depositar a la cuenta 1
print("Depositar 500000 a la cuenta 1")
print(f"Resultado de la transaccion: {AccountBank.deposit(account_1, 500000)}", end="\n\n")

# Retirar de la cuenta 2
print("Retirar 1000000 de la cuenta 2")
print(f"Resultado de la transaccion: {AccountBank.withdraw(account_2, 1000000)}", end="\n\n")

# Transferir de la cuenta 2 a la cuenta 1
print("Transferir 1000000 de la cuenta 2 a la cuenta 1")
print(f"Resultado de la transaccion: {AccountBank.transfer(account_2, account_1, 1000000)}", end="\n\n")


# Visualizacion de la informacion de las cuentas
print(f"Informacion de la cuenta 1: {account_1.get_info()}", end="\n\n")
print(f"Informacion de la cuenta 2: {account_2.get_info()}", end="\n\n")
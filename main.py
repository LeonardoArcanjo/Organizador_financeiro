"""
Main.py - Testando a Classe e o banco de Dados
"""

from Classes.financeObj import finance
from Context.Mongo_Context import connectar, desconnect

def main():
    # print("Creating a object....")

    # firstObject: finance = finance("Salario", 4500, "Renda", "")

    # print(firstObject)

    print("Creating a DB connect...")

    mongo = connectar()

    print(f"Object mongo: {mongo}")

    mongo = desconnect(mongo)

    print(f"Object mongo: {mongo}")




if "__main__" == __name__:
    main()
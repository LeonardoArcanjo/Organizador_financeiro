"""
Main.py - Testando a Classe e o banco de Dados
"""

from Classes.financeObj import finance
from Context.Mongo_Context import insert, list

def main():
    
    print("Criando um objeto: ")
    nome: str = input("Digite o nome: ")
    valor: float = float(input("Digite o valor R$: "))
    categoria: str = input("Digite a categoria do objeto: ")
    parcelas: str = input("Digite a quantidade de parcelas ou 'fixo': ")

    firstObject: finance = finance(nome, valor, categoria, parcelas)
    
    print("Salvando no Banco...")

    insert(firstObject.name, firstObject.value, firstObject.category, firstObject.numberInstalment)

    print("\n\nlistando o banco...")
    list()

if "__main__" == __name__:
    main()
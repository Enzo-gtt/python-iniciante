cliente = input("qual seu nome? ")
print(f"Ola {cliente}, estamos com uma taxa de R$10 por produto.")

produto = float(input("Qual o preço do produto? "))
print(f"O novo preço é R${produto + 10:.2f}")

from datetime import datetime

agora = datetime.now()
print(f"{agora.day}/{agora.month}/{agora.year}")

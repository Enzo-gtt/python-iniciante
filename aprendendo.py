cliente = input("qual seu nome? ")
print(f"Ola {cliente}, estamos com uma taxa de R$10 por produto.")

produto = float(input("Qual o preço do produto? "))
print(f"O novo preço é R${produto + 10:.2f}")

----------------------------------------------------------------

from datetime import datetime

agora = datetime.now()

datetime_atual = agora.strftime("%d/%m/%y")
print(datetime_atual)

----------------------------------------------------------------

idade = int(input("qual sua idade: "))
carteira = input("voce tem carteira? ").lower().strip()

if idade >= 18 and carteira == "sim":
    print("pode dirigir")
else:
    print("nao pode dirigir")

-----------------------------------------------------------------

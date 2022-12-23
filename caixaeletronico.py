#Exercício 09. Escreva um programa Python que solicita ao usuário um número inteiro n, correspondente a um determinado valor em reais, e calcula a quantidade mínima de notas que um caixa eletrônico hipotético deverá fornecer para perfazer tal valor. As notas disponíveis são de R$ 100, R$ 50, R$ 10 e R$ 1.

#Interação com o usuário
print(60 * "*")
nomeBanco = "Banco FIS"
print(nomeBanco.center(60))
print(60 * "*")

valor = eval(input("\nQual o valor que deseja sacar? R$ "))
print("(As notas disponíveis são de R$100, R$50, R$10 e R$1)")

#Código

saque = valor

cem = int(saque / 100)
saque = saque % 100
    
cinquenta = int(saque/50)
saque = saque % 50

dez = int(saque/10)
saque = saque % 10

um = saque

#Resultado
print("\nR$", valor, "=", cem, "* R$100 +", cinquenta, "* R$50 +", dez, "* R$10 +", um, "* R$1")
menu = """

[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
numero_saques = 0
numero_depositos = 0
limite_saques = 3
s = -1
d = -1
while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depositar")
        while d<0:
            d = int(input("Digite o valor do depósito:"))
        saldo = saldo + d
        numero_depositos = numero_depositos + 1
        d = -1

    elif opcao == "s":
        print("Sacar")
        if limite_saques == 0:
            print("O limite de saques ja foi atingido.")
        else:
            while s<0:
                s = int(input("Digite o valor do saque:"))
 
                if limite_saques == 0:
                    print("O limite de saques ja foi atingido.")
                elif s>saldo:
                    print("Não é possível sacar por falta de saldo.")
                elif s>500:
                    print("O limite de saque é de 500 reais.")
                else:
                    saldo = saldo - s
                    numero_saques = numero_saques + 1
                    limite_saques -= 1
            s = -1

        
    elif opcao == "e":
        print("O número de depósitos é igual a:",numero_depositos)
        print("O numero de saques é igual a:",numero_saques)
        print(f"O saldo atual da conta é igual a {saldo:.2f}")

    elif opcao == "q":
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada:")

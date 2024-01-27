print("""
██████╗░░░░░░░░░░██████╗░░█████╗░███╗░░██╗██╗░░██╗░█████╗░                ░░░░░░░░ ░░░░░███╗░░
██╔══██╗░██╗░██╗░██╔══██╗██╔══██╗████╗░██║██║░██╔╝██╔══██╗                ██╗░░░██╗░░░░████║░░
██████╔╝░╚████╔╝░██████╦╝███████║██╔██╗██║█████═╝░██║░░██║                ╚██╗░██╔╝░░░██╔██║░░
██╔═══╝░░░╚██╔╝░░██╔══██╗██╔══██║██║╚████║██╔═██╗░██║░░██║                ░╚████╔╝░░░░╚═╝██║░░
██║░░░░░░░░██║░░░██████╦╝██║░░██║██║░╚███║██║░╚██╗╚█████╔╝                ░░╚██╔╝░░██╗███████╗
╚═╝░░░░░░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░                ░░░╚═╝░░░╚═╝╚══════╝""")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print(""""Qual operação você deseja realizar? 
    [1] Depósito 
    [2] Saque 
    [3] Extrato 
    [4] Sair do Programa \n """)

    opcao = input()

    if opcao == "1":
        valor = float(input("Digite o valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(extrato)

        else:
            print("Operação não permitida, valor informado é inválido!")

    elif opcao == "2":
        valor = float(input("Digite o valor do Saque: "))

        if numero_saques >= LIMITE_SAQUES:
            print("Número Limite de Saques atingido")

        if valor > 0:
            if valor > saldo:
                print("Saldo insuficiente!")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(extrato)
                numero_saques = numero_saques + 1
        else:
            print("Operação não permitida, valor informado é inválido!")

    elif opcao == "3":
        print("\n=================Extrato=================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=========================================")

    elif opcao == "4":
        break

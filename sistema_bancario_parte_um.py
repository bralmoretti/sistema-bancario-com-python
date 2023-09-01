menu = """

[d] Depósito
[s] Saque
[e] Extrato
[f] Finalizar

=> """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na operação: o valor submetido é inválido.")


    elif opcao == "s":

        valor = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        execedeu_limite = valor > limite
        exedeu_limite_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação: você não possui saldo o suficiente para realizar esta operação.")

        elif execedeu_limite:
            print("Falha na operação: o valor deseja excede o valor permitido nesta operação.")

        elif exedeu_limite_saques:
            print("Falha na operação: você excedeu o limite diário de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Falha na operação: o valor submetido é inválido.")

    
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas novas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "f":
        break

    else:
        print("Operação inválida. Por favor, selecione a operação desejada.")


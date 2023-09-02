def deposito_operacao(saldo, quantia_a_depositar, extrato):
    
    if cliente:
        if quantia_a_depositar > 0:
                saldo += quantia_a_depositar
                extrato += f"Depósito: R$ {quantia_a_depositar:.2f}\n"

        else:
            print("Falha na operação: o valor submetido é inválido.")

        return saldo, extrato

    print("\nUsuário não encontrado. Por favor, cadastre-se no sistema antes de realizar uma operação.")


def saque_operacao(*, saldo, quantia_a_sacar, extrato, limite, numero_saques, LIMITE_SAQUES):

    if cliente:
        excedeu_saldo = quantia_a_sacar > saldo
        execedeu_limite = quantia_a_sacar > limite
        exedeu_limite_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação: você não possui saldo o suficiente para realizar esta operação.")

        elif execedeu_limite:
            print("Falha na operação: o valor deseja excede o valor permitido nesta operação.")

        elif exedeu_limite_saques:
            print("Falha na operação: você excedeu o limite diário de saques.")

        elif quantia_a_sacar > 0:
            saldo -= quantia_a_sacar
            extrato += f"Saque: R$ {quantia_a_sacar:.2f}\n"

        else:
            print("Falha na operação: o valor submetido é inválido.")

        return saldo, extrato

    print("\nUsuário não encontrado. Por favor, cadastre-se no sistema antes de realizar uma operação.")


def extrato_operacao(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas novas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=========================================")
    
    return


def cadastrar_cliente(clientes):

    cpf = input("Informe o CPF (APENAS NÚMEROS): ")
    cliente = checar_cliente(cpf, clientes)

    if cliente:
        print("\nInformamos que o CPF já se encontra cadastrado em nosso sistema! Tente outra operação.")

        return 

    else:
        nome = input("Informe nome completo: ")
        data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append(
            {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
        )

        print("Usuário cadastrado com sucesso!")

    return


def checar_cliente(cpf, clientes):

    clientes_checado = [cliente for cliente in clientes if cliente["cpf"] == cpf]

    return clientes_checado[0] if clientes_checado else None


def abrir_conta(agencia, numero_conta, clientes):

    cpf = input("Informe o CPF (APENAS NÚMEROS): ")
    cliente = checar_cliente(cpf, clientes)

    if cliente:

        print(f"Conta criada com sucesso! O número da conta é {numero_conta}.")
        
        return {"agencia":agencia, "numero_conta": numero_conta, "cliente":cliente}
    
    print("\nUsuário não encontrado. Por favor, cadastre-se no sistema antes de abrir uma conta corrente.")


def exibir_menu():
    opcao = input("""

    [d] Depósito
    [s] Saque
    [e] Extrato

    Ainda não possui conta? Vem com a gente:
    [ac] Criar conta corrente

    Ainda não está em nosso sistema? Faça seu cadastro:
    [cc] Cadastrar cliente


    [f] Finalizar

    => """)

    return opcao


def main():

    saldo = 0
    limite = 500
    numero_saques = 0
    extrato = ""
    clientes = []
    contas = []


    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
    
        opcao = exibir_menu()

        #escolheu depositar dinheiro
        if opcao == "d":
            valor = float(input("Informe o valor a ser depositado: "))

            saldo, extrato = deposito_operacao(saldo, valor, extrato)


        #escolheu sacar dinheiro
        elif opcao == "s":

            valor = float(input("Informe o valor a ser sacado: "))

            saldo, extrato = saque_operacao(
                saldo=saldo,
                quantia_a_sacar=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        

        #escolheu exibir o extrato da conta
        elif opcao == "e":
            extrato_operacao(saldo, extrato=extrato)

        
        #escolheu cadastrar cliente
        elif opcao == "cc":
            cadastrar_cliente(clientes)


        #escolheu abrir conta corrente
        elif opcao == "ac":
            numero_conta = len(contas) + 1
            conta = abrir_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)
        

        #escolheu finalizar atendimento
        elif opcao == "f":
            break

        #mensagem de erro
        else:
            print("Operação inválida. Por favor, selecione a operação desejada.")


if __name__ == "__main__":
    main()

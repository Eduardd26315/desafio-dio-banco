menu = """
[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado: R$ {valor:.2f}\n"
        print("Depósito efetuado com sucesso!")
    else:
        print("Erro! Valor inválido para depósito.")
    return saldo, extrato

def sacar(valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Erro! Saldo insuficiente para saque.")
    elif excedeu_limite:
        print("Erro! O valor do saque excede o limite permitido.")
    elif excedeu_saques:
        print("Erro! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque realizado: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque efetuado com sucesso!")
    else:
        print("Erro! Valor inválido para saque.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Nenhuma transação realizada." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

while True:
    operacao = input(menu)

    if operacao == "a":
        valor = float(input("Digite o valor para depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif operacao == "b":
        valor = float(input("Digite o valor para saque: "))
        saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES)

    elif operacao == "c":
        exibir_extrato(saldo, extrato)

    elif operacao == "d":
        print("Encerrando o sistema. Até a próxima!")
        break

    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")

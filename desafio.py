import datetime

menu_options = {
    "d": "  [d] Depositar \n",
    "s": " [s] Sacar \n",
    "e": " [e] Extrato \n",
    "q": " [q] Sair \n",
}

saldo = 0
extrato = ""
numero_saques = 0
limite = 500
LIMITE_SAQUES = 3

while True:

    opcao = input(f"{' '.join(menu_options.values())} => ")
    if opcao == "q":
        break

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            now = datetime.datetime.now()
            extrato += (
                f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
            )
        else:
            print("Valor inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo or excedeu_limite or excedeu_saques:
            if excedeu_saldo:
                print("Saldo insuficiente.")
            elif excedeu_limite:
                print("Limite de saque excedido.")
            elif excedeu_saques:
                print("Limite de saques excedido.")
        elif valor > 0:
            saldo -= valor
            now = datetime.datetime.now()
            extrato += f"{now.strftime('%Y-%m-%d %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    else:
        print("Operação inválida.")

print("Obrigado por utilizar o nosso sistema bancário.")

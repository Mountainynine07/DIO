menu = """
[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair
"""

saldo = 0
numero_saques = 0
print("Informe a opção desejada:")
LIMITE_DE_SAQUES = 3
LIMITE_SAQUE = 500

while True:
    opcao = input(menu)
    if opcao == "a":
        valor = float(input("informe o valor para o deposito:"))
        if valor > 0:
            saldo += valor
        else:
            print("Valor inválido. Informe um valor maior que zero.")

    elif opcao == "b":
        valor = float(input("Informe um valor para sacar:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE_SAQUE
        excedeu_saques = numero_saques >= LIMITE_SAQUE
        if excedeu_saldo:
            print("Seu saldo é insuficiente.")
        elif excedeu_saques:
            print("Limite de saques atingido.")
        elif excedeu_limite:
            print("O limite de valor para saque é 500. Informe outro valor.")
        elif valor > 0:
            saldo -= valor
            saque_dia = +1
        else:
            print("O valor é inválido.")

    elif opcao == "c":
        print("O saldo é de {saldo}")
    elif opcao == "d":
        break
    else:
        print("Operação invalida.")
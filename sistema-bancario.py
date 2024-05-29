import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = input("Digite o valor do Deposito: ")
        if  not deposito.isnumeric() or float(deposito) < 0:
            input("Valor invalido! \nPor favor digite um Valor Numerico Positivo\n Pressione qualquer tecla para continuar \n")
        else:
            deposito = float(deposito)
            saldo += deposito
            extrato += (f"Deposito no Valor de R$ {deposito: .2f} na data {datetime.date.today()}\n")
            input(f"""Deposito Efetuado com Sucesso
Seu Novo Saldo é de RS {saldo:.2f}
Aperte qualquer tecla para continuar\n""")

    elif opcao == "s":
        saque = input("Digite o valor do Saque: ")
        if  not saque.isnumeric() or float(saque) < 0:
            input("Valor invalido! \nPor favor digite um Valor Numerico Positivo\nPressione qualquer tecla para continuar \n")
        else:
            saque = float(saque)
            if LIMITE_SAQUES == 0:
                input("Limite de saques diarios esgotado, Saque disponivel no proximo dia \nAperte qualquer tecla para continuar \n")
            elif saque > saldo:
                input("Saque nao pode ser efetuado, Saldo insuficiente\nAperte qualquer tecla para continuar\n")
            else:
                saldo -= saque
                LIMITE_SAQUES -=1
                extrato += (f"Saque no Valor de R$ {saque: .2f} na data {datetime.date.today()}\n")
                input(f"Saque efetuado com Sucesso! \nSeu Novo Saldo é de RS {saldo:.2f} \nAperte qualquer tecla para continuar \n")
    elif opcao == "e":
        input(f"EXTRATO BANCARIO \n {extrato} \n Seu saldo Atual: R$ {saldo:.2f} \n Pressione qualquer tecla para continuar\n")

    elif opcao == "q":
        break

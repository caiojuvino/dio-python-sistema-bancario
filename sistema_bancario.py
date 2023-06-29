LIMITE_OPERACAO = 500
LIMITE_SAQUES = 3
MENU = """Selecione uma operação:
d - Depósito
s - Saque
e - Extrato
q - Sair

Operação: """

saldo = 0
extrato = ""
saques = 0
operacao = ""

print()

while operacao != "q":

    try:
        operacao = input(MENU).lower()
    except (KeyboardInterrupt):
        operacao = ""

    if operacao == "d":
        
        try:
            deposito = float(input("Valor do Depósito: "))
            saldo += deposito
            mensagem = f"Depositou R$ {deposito:.2f}\n"
            extrato += mensagem
            print(mensagem)

        except ValueError or deposito <= 0:
            print("O valor do depósito deve ser positivo!")

    elif operacao == "s":
        
        if saques < LIMITE_SAQUES:
            saque = float(input("Valor do Saque: "))
            
            if saque > LIMITE_OPERACAO:
                print("Seu limite é de R$ 500,00!")
            
            else:
                
                if saque > saldo:
                    print("Saldo insuficiente!\n")
                
                else:
                    saldo -= saque
                    mensagem = f"Sacou R$ {saque:.2f}\n"
                    extrato += mensagem
                    print(mensagem)
                    saques += 1
        else:
            print("Excedeu o limite de saques diários!\n")

    elif operacao == "e":
        print("\nEXTRATO")
        
        if extrato == "":
            print("Não houve operações no período!")
        else:
            print(extrato)
        print(f"Saldo de R$ {saldo:.2f}\n")

    else:

        if operacao != "q":
            print("Informe uma operação válida!\n")
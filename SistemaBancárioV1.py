import locale
locale.setlocale(locale.LC_ALL, "pt_BR.UTF8")
# Requisitos do desafio  ( Depósito - Saque - Extrato)
#1 Trabalha com apenas 1 usuario ( Não é necessario se preocupar com agencia e conta)
# 2.- Todos os depositos devem ser armazenados em uma variavel e exibidos no extrato
# 3.- O sistema deve permitir apenas 3 saques por dia, com limite de R$500,00 por saque. Caso o usuario tente sacar mais de 3 vezes ou mais de R$500,00, deve ser exibida uma mensagem de erro.
# 4.- Se o usuario nao tem saldo suficiente, deve ser exibida uma mensagem informando que o saque nao pode ser realizado por falta de saldo. Todos os saques devem ser armazenados em uma variavel e exibidos no extrato.
#5.- No extrato deve ser exibidos todos os depositos e saques realizados na conta. No fim da lista deve ser exibido o saldo atual da conta.
# 69.- Os valores devem ser exibidos no formato R$ 000,00

## UM TEMPLATE PRONTO COMO MODELO

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
deposito = 0
LIMITE_SAQUES = 3
SAQUE_POR_DIA = 500


while True:
    opcao = input(menu)  
    if opcao == "d":
        print("====== DEPOSITAR ======\n")
        deposito = input("Qual é o valor do depósito? ")
        
        if deposito == "":
            print("Campo não pode ser vazio. Selecione a opção novamente e digite o valor do depósito.")
            
        if deposito != "":
            deposito.strip()
            deposito = float(deposito)
            
            if deposito < 0 or deposito == 0:
                print("Valor deve ser maior que zero. Volte a operação, verifique e digite o valor do depósito novamente.")
            else:
                saldo += deposito
                print("Depósito realizado com sucesso!")
                print("========================================================\n")
                print("SALDO ATUAL: " + locale.currency(saldo, grouping=True))
                print("LIMITE: " + locale.currency(limite, grouping=True))
                #print(f"SALDO ATUAL: {saldo}\nLIMITE: {limite}")
                                    
    elif opcao == "s":
        opcao.strip().lower()
        print("=== Saque ===")
            
        saque = input("Qual é o valor do saque? ")
        
        if saque == "":
            print("Campo não pode ser vazio. Selecione a opção novamente e digite o valor do saque.")
            
        else:
            saque.strip()
            saque = int(saque)
                        
            if saque < 0 or saque == 0:
                    print("Valor deve ser maior que zero. Volte a operação, verifique e digite o valor do saque novamente.")
                    
            elif saque > saldo and saque > limite:
                print("Saldo insuficiente.\nVerifique seu saldo e tente realizar o saque de novo.")
            elif saque > SAQUE_POR_DIA:
                print("Não é possivel sacar mais do que $R 500 por dia.")
                    
            elif saque <= saldo and saque:
                saldo -= saque
                LIMITE_SAQUES -=1
                print("Saque realizado com sucesso!")
                print("==============================================================\n")
                print("SALDO ATUAL: " + locale.currency(saldo, grouping=True))
                print("LIMITE: " + locale.currency(limite, grouping=True))
                
            elif saldo == 0 and saque <= limite and saque:
                limite -= saque
                LIMITE_SAQUES -= 1

            if LIMITE_SAQUES == 0:
                print("Só é perimitido realizar 3 saques por dia.\nSerá possivel realizar outros saques a partir do próximo dia.")
                print("Obrigado por usar o nosso sistema.")
                break
                           
    elif opcao == "e":
        print("=== EXTRATO ===")
        print("==================================================================")
        print("ACOMPANHE NO EXTRATO O HISTÓRICO A SUA CONTA\n")
        print("Valor depositado:" + locale.currency(deposito, grouping=True))
        print("Limite: " + locale.currency(limite, grouping=True))
        print("Saldo atual: " + locale.currency(saldo, grouping=True))
        
    elif opcao == "q":
        print("=== Saindo do sistema ===")
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a opreção desejada.")
        continue
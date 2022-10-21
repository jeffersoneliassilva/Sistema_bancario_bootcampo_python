from tkinter import END


menu='''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''
saldo = 0
limite =500
extrato=""
numero_saques=0
conta_saques=0
LIMITE_SAQUES=3

while True:

    opcao = input(menu)

    if opcao =='d':
        deposito = int(input("Informe valor a despositar: "))
        saldo = saldo + deposito
        extrato = extrato + "\nDeposito: R$ "+str(deposito)+" - Saldo: R$ "+str(saldo)
        print("Depoosito realizado!")

    elif opcao=="s": 
        if conta_saques<3:
            saque = int(input("Informe valor a sacar: "))
            if saldo >= saque:
                saldo=saldo-saque                
                conta_saques+=1
                extrato = extrato + "\nSaque "+str(conta_saques)+": R$ "+str(deposito)+" - Saldo: R$ "+str(saldo)
                print("Saque realizado!")
            else: 
                print("Saldo Insuficiente") 
        else: 
            print("Excedeu limite Saques.")           

    elif opcao == "e":
        print(extrato)

    elif opcao=='q':
        break    

    else:
        print("Selecione uma opção válida.") 

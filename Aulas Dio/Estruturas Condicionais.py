conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450
#if saldo >= saque:
 #   print("Realizando saque!")

#if saldo <= saque:
#    print("Saldo insuficiente!")

#if saldo >= saque:
 #   print("Realizando saque!")

#else:
#    print("Saldo insuficiente!!")

#opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

#if opcao == 1:
 #   valor = float(input("Informe a quantia para saque: "))
#elif opcao == 2:
 #   print("Exibindo o extrato...")
#else:
  #  sys.exit("Opão inválida")

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else: 
        print("Não foi possível realizar o saque!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!!")

else: 
    print("Não foi possível reconhecer sua conta, entre em contato com o gerente da sua conta!")
print (" ")
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
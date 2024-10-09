#AND = Para ser True, tudo precisar ser True
#OR = Para ser True, apenas um precisa ser True

print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(False or False)
print(" ")

saldo = 1000
saque = 200
limite = 100
conta_emergencia = [100]

#print(saldo >= saque)

#print(saque <= limite)

#print(saldo >= saque and saque <= limite)

#print(saldo >= or saque <= limite)

print(not 1000 > 1500)

print(not conta_emergencia)

print(not "saque 1500")

print(not "")
print(" ")
print(" ")

exp = saldo >=saque and saque <= limite or conta_emergencia and saldo >= saque
print(exp)

exp_2 = (saldo >=saque and saque <= limite) or (conta_emergencia and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >=saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_emergencia and saldo >= saque)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
salario = 2000
def salario_bonus(hora_extra):
    global salario
    salario += hora_extra
    return salario

salario_total = salario_bonus(500)

print(salario_total)
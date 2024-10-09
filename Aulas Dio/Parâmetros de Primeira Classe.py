def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado= funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

def test(a,b):
    return a*2-b+5

exibir_resultado(10, 20, somar) #o resiltado será 30
exibir_resultado(10, 20, subtrair) 
exibir_resultado(10, 20, test) 

op = somar
print(somar(5,10))
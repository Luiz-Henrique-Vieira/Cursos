"""def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Henrique"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Luiz")
exibir_mensagem_2("Lala")
exibir_mensagem_3()
exibir_mensagem_3(nome="Daniel")"""

"""def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retornar_antecessor_e_sucessor(10))"""

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso!{marca}/{modelo}/`{ano} {placa}")

salvar_carro("Volkswagem", "Voyager", 2015, "LHZ-4544")
salvar_carro(marca="Volkswagem", modelo="Voyager", ano=2015, placa="LHZ-4544")
salvar_carro(**{"marca": "Volkswagem", "modelo": "Voyager", "ano": 2015, "placa": "LHZ-4544"})
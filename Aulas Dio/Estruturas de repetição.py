"""texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
print() 

#Range com For
for numero in range(0,11):
    print(numero, end=" ")

for numero in range(0,51,5):
    print(numero, end=" ")
print(" ")
#While
opcao = -1
while opcao != 0:
    opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato \n[0] Sair: \n "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else: 
    print("Obrigado por usar nosso sistemas bancário!")"""

#Break in While
while True:
    número = int(input("Informe um número: "))

    if número == 10:
        break
    print(número)

#Break in for
for numero in range(100):
    if numero == 10:
        break
    print(numero, end=" ")



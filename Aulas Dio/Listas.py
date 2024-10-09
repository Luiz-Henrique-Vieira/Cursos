"""frutas = ["frutas", "abacate", "melancia", "maça"]
print(frutas)

frutas1 = []
print(frutas)

letras = ["Python"]
print(letras)

letras = list["python"] # type: ignore
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["BMW", "M4", "Turbo", 500000, 2023, "São Paulo", True]
print(carro)

print()
print()


print(frutas[0]),print(frutas[3]),print(frutas[-1]),print(frutas[-3])
print()
print()


Matriz = [
    [1,"a",2],
    ["b",3,4],
    [5,6,"c"]
]

print(Matriz[0]),print(Matriz[0][0]),print(Matriz[0][-1]),print(Matriz[-1][-1])

print()
print()

lista = ["p", "y", "t", "h", "o", "n",]
print(lista[2:]),print(lista[:2]),print(lista[1:3]),print(lista[0:3:2]),print(lista[::-1]),print(lista[::])
"""
print()
print()

carros = ["gol", "bmw M-4", "GTR", "Supra" ]
for carro in carros:
    print(carro),print(carro[2])

print()
print()

carros = ["gol", "bmw M-4", "GTR", "Supra" ]
for indice, in carros in enumerate(carros):
    print(f"{indice}: {carro}")
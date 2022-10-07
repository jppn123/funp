from random import randint
tamanho = 10
lista = []

for i in range(tamanho):
    rand = randint(1, 100)
    lista.append(rand)
print(lista)
valor = int(input("digite um valor a ser localizado"))
for z in range(tamanho):
    if valor == lista[z]:
        print(f'o valor está presente no vetor e está na posição: {z}')

matriz = [[], [], [], [], [], [], [], [], [], [], [], []]
base = ['L', 'Time', 'P', 'J', 'V', 'E', 'D']
libam = []
csulam = []
rebaix = []
# input dos valores
for c in range(0, 12):
    pos = int(input('digite a posição'))
    time = input('digite o nome do time')
    pont = int(input('digite os pontos feitos'))
    jog = int(input('digite o numero de jogos'))
    vit = int(input('digite o numero de vitórias'))
    emp = int(input('digite o numero de empates'))
    der = int(input('digite o numero de derrotas'))
    matriz[c].append(pos)
    matriz[c].append(time)
    matriz[c].append(pont)
    matriz[c].append(jog)
    matriz[c].append(vit)
    matriz[c].append(emp)
    matriz[c].append(der)
#print da matriz(tabela)
for c in range(0, 7):
    print(f'{base[c]:^12}', end='')
for z in range(0, 12):
    print(end='\n')
    for x in range(0, 7):
        print(f'{matriz[z][x]:^12}', end='')

#calculos e indicações de posição na tabela
for w in range(0, 12):
    if matriz[w][0] == 1:
        print(end='\n')
        print(f'o campeão brasileiro foi o time: {matriz[w][1]}')
    for i in range(5):
        if matriz[w][0] == (i + 1):
            libam.append(matriz[w][1])
        elif matriz[w][0] == (i + 6):
            csulam.append(matriz[w][1])
    if matriz[w][0] == 11 or matriz[w][0] == 12:
        rebaix.append(matriz[w][1])

print(f'os times classificados para a libertadores da américa foram:', *libam, sep='  ')
print(f'os times classificados para a copa sul-america foram:', *csulam, sep='  ')
print(f'os times que foram rebaixados para a série B foram:', *rebaix, sep='  ')


from random import randint
from time import sleep
lista = list()
jogos = list()
print('xsz' * 55)
print('                                                                    JOGOS MEGA SENA           ')
print('xsz' * 55)
quantidade = int(input('Quantos jogos voce deseja sortear? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('xsz' * 5 , f'SORTEANDO {quantidade} JOGOS!!', 'xsz' * 5)
for i, l in enumerate (jogos):
    print(f'Jogo {i+1}: {l} ')
    sleep(2)
print('xsz' * 5, 'BOA SORTE!!!', 'xsz' * 5)
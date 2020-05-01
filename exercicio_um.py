listanumerica = []
maior = 0 
menor = 0 
for c in range (0,5):
    listanumerica.append(int(input(f'Digite um valor para a posiçao {c}: ')))
    if c == 0:
        maior = menor = listanumerica[c]
    else:
        if listanumerica[c]> maior:
            maior = listanumerica[c]
        if listanumerica[c]< menor:
            menor = listanumerica[c]
print('xsz' * 55)
print(f'Voçe digitou os numeros {listanumerica}')
print(f'O maior valor que voçe digitou foi {maior} na(s) posiçao(oes):', end='')
for i, v in enumerate(listanumerica):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor que voçe digitou foi {menor} na(s) posiçao(oes):', end='')
for i, v in enumerate(listanumerica):
    if v == menor:
        print(f'{i}...',end='')
print()

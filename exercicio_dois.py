numeros = list()
while True:
    n = int(input('Digite o valor: '))
    if n not in numeros:
        numeros.append(n)
        print('O valor foi adicionado! ')
    else:
        print('Queridao, esse valor ja existe. Nao posso adicionar! ')
    r = str(input('Quer adicionar mais? S/N '))
    if r in 'Nn':
        break
print('xsz' * 55)
numeros.sort()
print(f'Voçe digitou os numeros {numeros}')

temporario = []
principal = []
maior = menor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporario[1] 
    else: 
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resp = str(input('Quer continuar? S/N '))
    if resp in 'Nn':
        break
print('xsz' * 55)
print(f'Voce cadastrou {len(principal)} pessoas! ')
print(f'A maior peso cadastrado foi {maior} quilos. É o(a): ', end= '')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end= '')
print()
print(f'A maior peso cadastrado foi {menor} quilos. É o(a): ', end= '')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end= '')
print()
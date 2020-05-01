numeros = list ()
pares = list ()
impares = list ()
while True:
    numeros.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? S/N '))
    if resp in 'Nn':
        break
for i, v in enumerate(numeros): 
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('xsz' * 55)
print(f'A lista completa dos numeros é {numeros}')
print(f'A lista de numeros pares é {pares}')
print(f'A lista de numeros impares é {impares}')

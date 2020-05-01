valores = []
while True:
    valores.append (int(input('Digite um número: ')))
    resp = str(input('Quer continuar adicionando? S/N '))
    if resp in 'Nn': 
        break
print('xsz' * 55)
print(f'Voce digitou {len(valores)} valores!! ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {valores} ')
if 5 in valores:
    print('O valor 5 faz parte da lista!!! ')
else:
    print('O valor 5 nao esta na lista!!! ')
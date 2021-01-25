print('somar quantas vezes? ')
vezes = int(input())
contador = 0
resultado = 0
maior = 0
while(contador < vezes):
    contador += 1
    print('informe o valor da soma: ')
    a = int(input())
    if a > maior:
        maior = a
    resultado += a

print('A soma dos numeros foi = {}'.format(resultado))
print('O maior numero é {}'.format(maior))
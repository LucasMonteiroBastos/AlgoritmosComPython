print('quantas vezes voce deseja somar? ')
a = int(input())
cont = 0
soma = 0
maior = 0
menor = 0

while(cont < a):
    cont += 1
    b = int(input())
    soma += b

    # se b for maior que (a variavel maior) então (a variavel maior = recebe b)
    if b > maior:
        maior = b

    # menor é igual a zero?
    # se for menor = (b)
    if menor == 0:
        menor = b
    # se b for menor que (a variavel menor) então (a variavel menor = recebe b)
    if b < menor:
        menor = b


print("Soma total",soma)
print("Maior valor",maior)
print("Menor valor",menor)


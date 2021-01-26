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

    # se b for maior que (maior) (maior = recebe b)
    if b > maior:
        maior = b

    #
    if menor == 0:
        menor = b

    if b < menor:
        menor = b


print("Soma total",soma)
print("Maior valor",maior)
print("Menor valor",menor)


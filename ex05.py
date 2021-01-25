print('ano atual: ')
ano = int(input())
print('ano de nascimento: ')
nasc = int(input())
idade = ano - nasc
falta = 18 - idade

if idade >= 18:
    print('voce tem {}, e esta APTO a tirar sua CNH.'.format(idade))
elif idade < 18:
    print('voce tem {},ainda é dimenor, faltam {} anos para tirar sua CNH.'.format(idade,falta))
print('em que ano estamos? ')
ano = int(input())
print('em que ano voce nasceu?')
nasc = int(input())
idade = ano - nasc
print('em {} voce tera {}'.format(ano, idade))
if(idade >= 18):
    print('Voce ja atingiu a maior idade')
else:
    print('Voce é de menor')
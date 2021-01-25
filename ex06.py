print('nome do aluno: ')
nome = str(input())
print('primeira nota: ')
a = float(input())
print('segunda nota: ')
b = float(input())
media = (a + b) /2

if media >= 7:
    print('{}, a sua media é {}, PARABENS APROVADO'.format(nome,media))
elif media >= 5 and media < 7:
    print('{} sua media é {}, Voce esta de RECUPERAÇÃO, estude mais.'.format(nome,media))
elif media < 5:
    print('{}, sua media é {}, infelizmente voce esta REPROVADO.'.format(nome,media))
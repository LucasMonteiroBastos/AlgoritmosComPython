print('Bem vindo, informe o seu nome aluno: ')
nome = str(input())
print('1º nota: ')
a = float(input())
print('2º nota: ')
b = float(input())
media = (a + b) / 2
nota = 0
if media >= 9:
    nota = "A"
elif media > 8 and media < 8.9:
    nota = "B"
elif media > 7 and media <7.9:
    nota = "C"
elif media > 6 and media < 6.8:
    nota = "D"
elif media > 5 and media < 5.9:
    nota = "E"
elif media < 5:
    nota = "F"
print('{}, sua media foi {}, sua nota é: [{}]'.format(nome,media,nota))


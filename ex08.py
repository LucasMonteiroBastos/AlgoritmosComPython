print('qual o nome do funcionario? ')
nome = str(input())
print('qual o salario do funcionario?')
salario = float(input())
print('qual é a quantidade de dependetes?')
dep = int(input())
novo = 0
if dep == 0:
    novo = salario + (salario * 5 / 100)
elif dep == 1 or dep == 2 or dep == 3:
    novo = salario + (salario * 10 / 100)
elif dep == 4 or dep == 5 or dep == 6:
    novo = salario + (salario * 15 / 100)
elif dep >= 7:
    novo = salario + (salario * 18 / 100)

print('{}, voce tem {} depentes, com isso o ajuste do seu salario ficou em {}'.format(nome, dep, novo))
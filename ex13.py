print('Inicio: ')
inicio = int(input())
print('Fim: ')
fim = int(input())
saida = ''
if inicio < fim:
    while(inicio <= fim):
        saida +=f' {inicio}...'
        inicio += 1
elif inicio > fim:
    while(inicio >= fim):
        saida +=f' {inicio}...'
        inicio -= 1
print(saida)
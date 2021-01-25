print('[1] para doar R$ 10.00')
print('[2] para doar R$ 25.00')
print('[3] para doar R$ 50.00')
print('[4] para doar outros valores')
print('[5] para cancelar')

cond = True
while cond:
    opcao = int(input())
    doacao = 0
    if opcao == 1:
        doacao = 10.00
    elif opcao == 2:
        doacao = 25.00
    elif opcao == 3:
        doacao = 50.00
    elif opcao == 4:
        print('Informe o valor: ')
        doacao = float(input())

    elif opcao == 5:
        print('Operação cancelada.')
    elif opcao == 6:
        cond = False
    print('Digite 6 para sair')
    print('Obrigado por participar, sua doação foi {:.2f} Reais.'.format(doacao))


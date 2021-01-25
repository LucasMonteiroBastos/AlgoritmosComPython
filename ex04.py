print('Bom dia, me informe o seu Nome: ')
nome = str(input())
print('Informe o seu peso: (Kg)')
peso = float(input())
print('informe a sua altura: (m)')
altura = float(input())
imc = peso / (altura * altura)

if imc < 17:
    print('{}... Seu IMC é {:.2f}, e voce esta Muito abaixo do peso.'.format(nome,imc))
elif imc >= 17 and imc <= 18.5:
    print('{}... Seu IMC é {:.2f}, e voce esta Abaixo do peso.'.format(nome,imc))
elif imc >= 18.5 and imc <= 25:
    print('{}... Seu IMC é {:.2f}, e voce esta no Peso Ideal.'.format(nome,imc))
elif imc >= 25 and imc <= 30:
    print('{}... Seu IMC é {:.2f}, e voce esta Sobrepeso.'.format(nome,imc))
elif imc >= 30 and imc <= 35:
    print('{}... Seu IMC é {:.2f}, e voce esta com Obesidade.'.format(nome,imc))
elif imc >= 35 and imc <= 40:
    print('{}... Seu IMC é {:.2f}, e voce esta com Obesidade Severa.'.format(nome,imc))
elif imc >= 40:
    print('{}... Seu IMC é {:.2f}, e voce esta com Obesidade Mórbida.'.format(nome,imc))
print('Obrigado por participar.')
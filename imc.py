peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))


if imc < 17:
    print('Muito abaixo do peso')
elif imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Acima do peso')
elif imc < 35:
    print('Obesidade Grau I')
elif imc <= 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')



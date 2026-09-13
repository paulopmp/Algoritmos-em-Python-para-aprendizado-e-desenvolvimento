#CALCULO DE IMC
# ==============


nome = str(input('Digite o seu nome: '))
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura * altura)
if imc < 18:
    print('O seu peso é', peso, 'status: ABAIXO DO PESO')
elif imc >= 18 and imc < 25:
    print('O seu peso é',peso, 'status: PESO NORMAL')
elif imc >= 25 and imc < 29:
    print('O seu peso é', peso, 'status: ACIMA DO PESO')
elif imc >= 29 and imc < 34:
    print('O seu peso é', peso, 'status: OBESIDADE GRAU 1')
elif imc >= 34 and imc < 40:
    print('O seu peso é', peso, 'status: OBESIDADE GRAU II')
else:
    print('O seu peso é', peso, 'status: OBESIDADE GRAU III')

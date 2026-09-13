# PROGRAMA VERIFIFA SE UM NÚMERO É POSITIVO OU NEGATIVO

n = int(input('Digite um número inteiro qualquer: '))

if n == 0:
    print('O número digitado é igual a zero.')
elif n > 0:
    print('O número digitado é positivo (maior do que zero).')
else:
    print('O número digitado é negativo (menor do que zero).')

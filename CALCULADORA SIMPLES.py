# CALCULADORA SIMPLES


opcao_escolhida = int(input('Escolha a opção de operação a seguir: 1 - adiÇao; 2 - subtraÇao; 3- multiplicaÇao; 4- divisao: '))

# OPERAÇÃO DE ADIÇÃO
if opcao_escolhida == 1:
    print('A sua opção escolhida foi a operação de ADIÇÃO.')
    n1 = int(input('Digite o primeiro termo da ADIÇÃO: '))
    n2 = int(input('Digite o segundo termo da ADIÇÃO: '))
    soma = n1 + n2
    print('O resultado da SOMA foi', soma)

# OPERAÇÃO DE SUBTRAÇÃO

elif opcao_escolhida == 2:
    print('A sua opção escolhida foi a operação de SUBTRAÇÃO.')
    n1 = int(input('Digite o primeiro termo da SUBTRAÇÃO: '))
    n2 = int(input('Digite o segundo termo da SUBTRAÇÃO: '))
    subtracao = n1 - n2
    print('O resultado da SUBTRAÇÃO foi', subtracao)

# OPERAÇÃO DE MULTIPLICAÇÃO

elif opcao_escolhida == 3:
    print('A sua opção escolhida foi a operação de MULTIPLICAÇÃO.')
    n1 = int(input('Digite o primeiro termo da MULTIPLICAÇÃO: '))
    n2 = int(input('Digite o segundo termo da MULTIPLICAÇÃO: '))
    multiplicacao = n1 * n2
    print('O resultado da MULTIPLICAÇÃO foi', multiplicacao)

# OPERAÇÃO DE DIVISÃO

elif opcao_escolhida == 4:
    print('A sua opção escolhida foi a operação de DIVISÃO.')
    n1 = int(input('Digite o primeiro termo da DIVISÃO: '))
    n2 = int(input('Digite o segundo termo da DIVISÃO: '))
    divisao = n1 / n2
    print('O resultado da DIVISÃO foi', divisao)

# OPÇÃO FORA DO ESCOPO DO ALGORITMO

else:
    print('❌ erro! \n'
          'Por favor, digite uma opção válida (1, 2  3, ou 4).')

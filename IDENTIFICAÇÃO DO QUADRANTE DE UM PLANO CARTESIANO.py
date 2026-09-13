# IDENTIFICAÇÃO DO QUADRANTE DE UM PLANO CARTESIANO






# ALGORITMO


x = float(input('Digite o valor de X: '))

y = float(input('Digite o valor de Y: '))

if x > 0 and y > 0: 
    print('PRIMEIRO QUADRANTE')
    
elif x < 0 and y > 0: 
    print('SEGUNDO QUADRANTE')
    
elif x < 0 and y < 0: 
    print('TERCEIRO QUADRANTE')
    
else:
    print('QUARTO QUADRANTE')

# FIM ALGORITMO

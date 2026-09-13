# VERIFICAR SE A MEDIDA DE TRêS RETAS PODEM FORMAR UM TRIÂNGULO


m1 = float(input('Digite a medida da primeira reta: '))
m2 = float(input('Digite a medida da segunda reta: '))
m3 = float(input('Digite a medida da terceira reta: '))

if m1 < (m2 + m3) and m2 < (m1 + m3) and m3 < (m1 + m2):
    print('As três retas podem formar um triângulo!')

else:
     print('As três retas NÃO podem formar um triângulo!')

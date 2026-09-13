# VERIFICAR SE A MEDIDA DOS TRÊS LADOS DE UM TRIÂNGULO E CLASSIFICAR SE A CATEGORIA É: EQUILÁTERO, ISÓSCELES OU ESCALENO.

import sys
import os

m1 = float(input('Digite a medida da primeira reta: '))
m2 = float(input('Digite a medida da segunda reta: '))
m3 = float(input('Digite a medida da terceira reta: '))

if m1 < (m2 + m3) and m2 < (m1 + m3) and m3 < (m1 + m2):
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas NÃO podem formar um triângulo!')
    restart_program()

if m1 == m2 and m2 == m3:
    print('As medidas das retas informadas correspondem ao triângulo do tipo EQUILÁTERO. ')
elif m1 == m2 and m2 != m3 or m1 != m2 and m2 == m3:
    print('As medidas das retas informadas correspondem ao triângulo do tipo ISÓSCELES. ')
elif m1 != m2 and m2 != m3:
    print('As medidas das retas informadas correspondem ao triângulo do tipo ESCALENO.')


else:
    restart_program()

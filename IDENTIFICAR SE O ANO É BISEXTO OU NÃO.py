# IDENTIFICAR SE O ANO É BISEXTO OU NÃO

import calendar

ano = int(input('Digite o ano para verificar se é bisexto: '))

resultado = calendar.isleap(ano)

if resultado != False:
    print(f'O ano informado foi {ano}, é ano BISSEXTO.')
else:
    print(f'O ano informado foi {ano}, não é ano BISSEXTO.')

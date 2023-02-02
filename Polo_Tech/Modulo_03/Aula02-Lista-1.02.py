# 2. Peça a data de nascimento de uma pessoa e devolva a idade dela (desconsiderando anos bissextos)
from datetime import date

data = input('Digite sua data de nascimento [DD/MM/AAAA]: ')
dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[-4:])

hoje = date.today()
if hoje.month == mes:
    if hoje.day >= dia:
        idade = hoje.year - ano  
    else:
        idade = hoje.year-1 - ano
elif hoje.month > mes:
    idade = hoje.year - ano
else:
    idade = hoje.year-1 - ano

print(f'Sua idade é: {idade} ano(s)')

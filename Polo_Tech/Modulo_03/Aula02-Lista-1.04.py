# 4. Peça o nome completo de uma pessoa, e exiba separadamente o nome e o(s) sobrenome(s)
nome_completo = input('Insira seu nome completo: ')
nomes_list = nome_completo.split()

nome = nomes_list[0]
sobrenome = ' '.join(nomes_list[1:])
print(f'Nome: {nome}\nSobrenome(s): {sobrenome}')
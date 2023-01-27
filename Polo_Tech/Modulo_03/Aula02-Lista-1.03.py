# 3. Crie uma lista de 10 nomes e 10 sobrenomes, e apresente uma lista de todas as combinações entre nome e sobrenomes possíveis.
nomes = ['Vitor', 'Irla', 'Flavio', 'Fabio', 'Silvia', 'José', 'Maria', 'Manoel', 'Mariana', 'Hamilton']
sobrenomes = ['Silva', 'Rodrigues', 'Andrade', 'Maranhão', 'Coutinho', 'Souza', 'Vasconselos', 'Correia', 'Campos', 'Almeida']

compinacoes = []

for nome in nomes:
    for sobrenome in sobrenomes:
        combinacao = nome + ' ' + sobrenome
        compinacoes.append(combinacao)

print(compinacoes)
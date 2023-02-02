# 5. Faça um programa que peça o nome, a idade, a cidade de nascimento e a cidade de moradia atual da pessoa, e retorne se esta pessoa pode votar, e se precisa se deslocar de cidade pra votar.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade_nasc = input('Informe a cidade em que nasceu: ')
cidade_atual = input('Informe a cidade em que estás atualmente: ')


if cidade_nasc.upper() != cidade_atual.upper():
    print('Você precisa se deslocar de cidade pra votar.')
else:
    print('Você NÃO precisa se deslocar de cidade pra votar.')
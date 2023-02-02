# 1. Liste os primeiros 50 números primos
qtd_primos = 50
lista_primos = []
for i in range(2,qtd_primos+1):
    check_primo = 0
    for j in range(2, i+1):
        if i % j == 0:
            check_primo += 1
            if check_primo > 1:
                break
    # Se o valor de check_primo = 1, significa que o número é primo
    if check_primo == 1: 
        lista_primos.append(i)

print(f'Lista de primos de até o número {qtd_primos}: {lista_primos}')

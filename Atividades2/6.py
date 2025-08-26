# Importando lib
import os
import time
lista = []
minimo = 0
maximo = 10
print(f'{'-'*20} Lista dobrada {'-'*20}\n')

while minimo < maximo:
    try:
        numero = int(input('Digite números até chegar no 10: '))
        lista.append(numero * 2)
        time.sleep(0.3)
        os.system('cls')
        lista2 = lista

    except ValueError:
        print('Por favor, digite um número válido!')
        time.sleep(2)
        os.system('cls')
        continue

    minimo += 1 
    if minimo == maximo:
        print(f'A lista com o dobro de cada um dos números é: {[lista]} ')
        
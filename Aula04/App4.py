'''
    Programa: Sorteio V.3.0
    Importando bibliotecas
    Aula 04: 19/08/2025
    Random: escolha aleatória
    descrição: sistema recebe o nome dos candidatos e realiza o sorteio
'''
import random
import os
import time

lista_nomes = []
lista_sorteados = []

while True:
    nome = input('Digite o nome para o sorteio: ')
    if nome:
        lista_nomes.append(nome)
    else:
        break

while True:
    if lista_nomes:
        os.system('cls')
        escolhido = random.choice(lista_nomes)
        lista_sorteados.append(escolhido)

        print(f'O escolhido foi {escolhido}')

        lista_nomes.remove(escolhido)

        opcao = input('Deseja sortear outro nome? \n S - Sim \n| N - Não\n: ').lower()
        os.system('cls')

        if opcao != 's':
            break
    else:
        print('Não há nomes para serem sorteados.')
        break
print('Programa finalizado!')
print(f'Os sorteados foram {lista_sorteados}')
    
'''
    Programa: Adivinhação V.1.0
    Importando bibliotecas
    Aula 04: 19/08/2025
    Random: escolha aleatória
    descrição: sistema recebe o nome dos candidatos e realiza o sorteio
'''
# Importando lib
from random import randint

print('Tente adivinhar o numero!')
num1 = int(input('Digite um numero: '))

num_secreto = randint(1,10)

if num1 ==  num_secreto:
    print('Parabéns, você ganhou!')
else:
    print('Você perdeu!!')
    print(f'O número correto é {num_secreto}')
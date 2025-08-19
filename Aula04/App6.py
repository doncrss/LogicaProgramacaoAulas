'''
    Programa: Adivinhação V.2.0
    Importando bibliotecas
    Aula 04: 19/08/2025
    Random: escolha aleatória
    descrição: sistema recebe o nome dos candidatos e realiza o sorteio
'''
# Importando lib
import random
import os
import time
numero_secreto = random.randint(1,100)

tentativas = 0
max_tentativas = 10
acertou = False

print(30*'-', 'Bem vindo ao Adivinha logo!',30*'-')
print(f' Você tem {max_tentativas} tentativas para adivinhar um número entre 1 e 100')
print('Vamos começar?')

while tentativas < max_tentativas:
    try:
        palpite = int(input('Digite o seu palpite: '))

    except ValueError:
        print('Por favor, digite um número válido!')
        continue

    tentativas += 1

    # verificar palpite
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('Tente um número maior.')
        print(f' você já usou {tentativas} tentativas.')
        time.sleep(2)
        os.system('cls')
    
    else:
        print('Tente um número menor!')
        print(f' você já usou {tentativas} tentativas.')
        time.sleep(2)
        os.system('cls')

if acertou:
    print(f'Parabéns, você ganhou! Você acertou o numero {numero_secreto} em {tentativas} tentativas!')
else:
    print(f'Que pena! Você não conseguuiu adivinhar o número secreto {numero_secreto}')

        
import random
import os
import json

with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas\Aula08\py.json','r', encoding="utf-8") as f:
    Temas = json.load(f)

def menu():
    p = [['1 - programação'],
        [ '2 - Comida'      ],
        ['  3 - Animais  '],
        [' 4 - Sair do sistema']]
    for i in p:
        print(i)

    opcao = input('Informe a opção desejada: ')
        

    match opcao:
        case '1':
            return random.choice(Temas["Tema01"])
        case '2':
            return random.choice(Temas["Tema02"])
        case '3':
            return random.choice(Temas["Tema03"])
        case '4':
            print('Saindo do sistema!')
            exit()
        case _:
            print('Opção inválida')
            ...



def jogar_forca():
    palavra = menu()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6
    
    while True:
        palavra_escondida = ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida += letra
            else:
                palavra_escondida += '_'
        
        print('Palavra:', palavra_escondida)
        print('Letras erradas:', letras_erradas)
        print('Tentativas restantes:', tentativas)

        if palavra_escondida == palavra:
            print('Parabéns, você ganhou!')
            break
        elif tentativas == 0:
            print('Você perdeu! A palavra era:', palavra)
            break

        letra_usuario = input('Digite uma letra: ').lower()

        if letra_usuario in palavra:
            print('Letra correta!')
            letras_corretas.append(letra_usuario)
        else:
            print('Letra Errada!')
            letras_erradas.append(letra_usuario)
            tentativas -= 1
if __name__ == '__main__':
    jogar_forca()




    

 

print(30*'-', 'Lista de nomes', 30*'-')
import os
lista = []
while True:
    print(lista)

    print('O que você deseja fazer na lista?')
    print('1 - Adicionar nome | 2 - Remover nome')
    print('3 - Pesquisar nome | 4 - Alterar nome')
    escolha = int(input('Digite sua escolha: '))


    if escolha == 1:
        while True:
            add = input('Digite o nome que você deseja adicionar na lista: ')
            lista.append(add)
            os.system('cls')
            print('Nome adicionado com sucesso!')
            print('Deseja retornar ao menu?')
            print('S - Sim | N - Não')
            escolhas = input(':').lower()
            if escolhas == 'n':
                continue
            elif escolhas == 's':
                break
        
        
    elif escolha == 2:
        while True:
            print(lista)
            remover = (input('Digite o nome que você quer remover da lista: '))
            os.system('cls')
            if remover in lista:
                print(f'o nome {remover} foi removido com sucesso da lista!')
                lista.remove(remover)
            else:
                print('Esse nome não está na lista!')
            print('Deseja retornar ao menu?')
            print('S - Sim | N - Não')
            escolhas = input(':').lower()
            if escolhas == 'n':
                continue
            elif escolhas == 's':
                break

    elif escolha == 3:
        while True:
            nome = input('Digite o nome que você quer pesquisar na lista: ')
            os.system('cls')
            if nome in lista:
                print(f'o nome {nome} está presente na lista!')
            else:
                print('Esse nome não está na lista!')
            print('Deseja retornar ao menu?')
            print('S - Sim | N - Não')
            escolhas = input(':').lower()
            if escolhas == 'n':
                continue
            elif escolhas == 's':
                break
    elif escolha == 4:
        while True:
            print(lista)
            alterar = input('Digite o nome que você quer alterar: ')
            alterar2 = input('Agora digite o nome que você quer colocar no lugar: ')
            indice = lista.index(alterar)
            os.system('cls')
            if alterar in lista:
                print(f'o nome {alterar} foi alterado com sucesso!')
                lista[indice] = alterar2
            else:
                print('Esse nome não está na lista!')
            print('Deseja retornar ao menu?')
            print('S - Sim | N - Não')
            escolhas = input(':').lower()
            if escolhas == 'n':
                break
            elif escolhas == 's':
                continue
            os.system('cls')
            

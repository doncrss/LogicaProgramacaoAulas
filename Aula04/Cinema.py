
print(20* '-', 'Bem vindo ao Cinemark!', 20* '-')
sala1 = 'Quarteto Fantástico'
min1  = 16
sala2 = 'Super Man'
min2 = 14
sala3 = 'Lilo e Stitch'
min3 = 1
sala4  = 'Como treinar seu dragão'
min4 = 12
sala5 = 'Sorria 3'
min5 = 18
while True:
    print(f'Escolha um Filme: ')
    print(f'Sala 1 - {sala1} 16h30 | Idade mínima {min1} ')
    print(f'Sala 2 - {sala2} 18h30 | Idade mínima {min2} ')
    print(f'Sala 3 - {sala3} 19h30 | Idade mínima {min3} ')
    print(f'Sala 4 - {sala4} 20h30 | Idade mínima {min4} ')
    print(f'Sala 5 - {sala5} 21h30 | Idade mínima {min5} ')
    print('6 - Sair')
    opcao_filme = int(input('Digite o filme que você deseja: '))
    idade = int(input('Digite sua idade: '))
    if opcao_filme == 1:
        if idade >= min1:
            print('Imprimindo seu ingresso...')
            break
        else:
            print('Você não tem a idade necessária pra assistir o filme!')
    elif opcao_filme == 2:
        if idade >= min2:
            print('Imprimindo seu ingresso...')
            break

        else:
            print('Você não tem a idade necessária pra assistir o filme!')
    elif opcao_filme == 3:
        if idade >= min3:
            print('Imprimindo seu ingresso...')
            break
        else:
            print('Você não tem a idade necessária pra assistir o filme!')
    elif opcao_filme == 4:
        if idade >= min4:
            print('Imprimindo seu ingresso...')
            break          
        else:
            print('Você não tem a idade necessária pra assistir o filme!')
    elif opcao_filme == 5:
        if idade >= min5:
            print('Imprimindo seu ingresso...')
            break
        else:
            print('Você não tem a idade necessária pra assistir o filme!')            
    elif opcao_filme == 6:
        break
        


# FOR e LISTAS


nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joana', 'Maria', 'Mariana', 'Fulano']
nome = input('Informe o nome que deseja encontrar: ')
if nome in nomes_lista:
    print(nome)
else:
    print(f'{nome} não encontrado.')

# index
indice = nomes_lista.index(nome)
try:
    print(f'{nome} encontrado no índice {indice}.')
except:
    print(f'{nome} não encontrado.')
# Count

quantidade = nomes_lista.count(nome)
try:
    print(f'{nome} foi encontrado na lista {quantidade} vezes.')
except:
    print(f'{nome} não foi encontrado.')
    print(f'{nome} foi encontrado na lista {quantidade} vezes.')

nome_a_alterar = input('Digite o nome que deseja alterar: ')
nomes_lista[nomes_lista.index(nome_a_alterar)] = input('informe o novo nome: ')
for nome in nomes_lista:
    print(nome)



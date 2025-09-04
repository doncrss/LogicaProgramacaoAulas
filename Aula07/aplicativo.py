'''
    Programa: Banco
    Depositar, exibir dados, depositar, sacar valor, encerrar conta, sair do programa
    Aula 07: 02/09/2025
'''
import os
usuarios = []
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
def cadastro():
        usuarios['nome'] = input('Informe o nome: ').strip()
        usuarios['idade'] = input('Informe a idade: ')
        usuarios['email'] = input('Digite o email: ').strip().lower
        usuarios['saldo'] = int(input('Digite o saldo inicial: '))
            

        limpar()
        print('Usuário cadastrado com sucesso!')
        print(usuarios)
        print(type(usuarios))

def deposito():
    global dep
    usuarios['saldo'] += dep

    dep = float(input('Digite o valor que deseja depositar: '))
    print('Dinheiro depositado com sucesso!')
    saldo += dep

def sacar():
    global saldo
    saque = float(input('Digite o valor que deseja sacar: '))
    usuarios['saldo'] -= saque

def encerrar_conta():
    usuarios.clear()
    
def menu():
    
    print(f'O seu saldo é de R$') usuarios[saldo]
    print('1 - Cadastrar novo usuário')
    print('2 - Exibir dados')
    print('3 - Depositar valor')
    print('4 - Sacar valor')
    print('5 - Encerrar conta')
    print('6 - Sair do programa')
    opcao = input('Informe a opção desejada: ')
    return opcao

while True:
    print(f'{'-'*20} Banco {'-'*20}\n')

    match menu():
        case '1':
            cadastro()
 
        case '2':
            print(usuarios)
        case '3':
            deposito()

        case '4':
            sacar()

        case '5':
            encerrar_conta()
            print('Conta encerrada com sucesso! ')
            saldo = 0

        case '6':
            print('Saindo do programa...')
            break
        case _:
            print('Número inválido!')
            break

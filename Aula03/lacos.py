''' 
Problema 2: Um elevador de carga possui capacidade para 200kg. Crie 
um programa que receba do usuário seu peso e o peso da carga e veri-
fica se a carga está autorizada a usar o elevador ou não.
 
'''
'''
print(20* '-', 'Elevador de serviço', 20* '-')

peso = float(input('Digite seu peso: '))
peso_carga = float(input('Digite o peso da carga: '))
peso_limite = 200

if (peso + peso_carga) >= peso_limite:
    print('Você não está permitido a entrar no elevador!')
else:
    print('Você está permitido a entrar no elevador!')

# While
numero = 10

 while numero >= 0:
    print(numero)
    numero -= 1


# Loop IMC

print(40*'-','Calculadora IMC',40*'-')
while True:
    peso = float(input("Digite seu peso:"))
    altura = float(input("digite sua altura:"))
    IMC = peso / altura ** 2

    print(f'O seu imc é de: {IMC:.2f}')
    if IMC <18.5:
        print("Coma, você está abaixo do peso!")
    elif IMC <= 24.9:
        print("Parabéns! Você está no peso ideal!")
    elif IMC <= 29.9:
        print("Tome cuidado, você está com sobrepeso!")
    elif IMC >= 30.0:
        print("Você tem obesidade...")       
    opcao = input('Deseja calcular novamente? S - Sim | - Não: ').lower()

    if opcao == 's':
        continue
    elif opcao == 'n':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida!')
'''
print(40* '-', 'Cadastro de usuário', 40* '-')

saudacao = input('Digite seu nome:')
cpf = input('Digite seu CPF:')
telefone = input('Digite seu telefone:')
data_nasc = input('Digite sua data de nascimento: ')

print(50*'-')


while True:
    print(40* '-', 'Sistema Console 2º D.S', 40* '-')
    print('Bom dia', saudacao, ',Seja bem vindo ao sistema!')
    print('1 - Calculadora IMC')
    print('2 - Maioridade')
    print('3 - Calculadora')
    print('4 - Dados Pessoais')
    print('5 - Feliz Natal!')
    print('6 - Sair')

    opcao = input('Escolha sua opção: ')

    if opcao == "1":
        print(40*'-','Calculadora IMC',40*'-')

        peso = float(input("Digite seu peso:"))
        altura = float(input("digite sua altura:"))
        IMC = peso / altura ** 2

        print(f'O seu imc é de: {IMC:.2f}')
        if IMC <18.5:
            print("Coma, você está abaixo do peso!")
        elif IMC <= 24.9:
            print("Parabéns! Você está no peso ideal!")
        elif IMC <= 29.9:
            print("Tome cuidado, você está com sobrepeso!")
        elif IMC >= 30.0:
            print("Você tem obesidade...")
        
    elif opcao == "2":
        idade1 = int(input('Digite sua idade: '))
        print(saudacao, 'é maior de idade. ' if idade1 >= 18 else 'é menor de idade.')
    elif opcao ==  "3":

        while True:
            numero1 = float(input('digite o primeiro número:'))
            numero2 = float(input('digite o segundo número:'))
            print('1 - Soma')
            print('2 - Divisão')
            print('3 - Subtração')
            print('4 - Multiplicação')
            print('5 - Sair')
            opcao2 = input('Digite o número da operação: ')

            soma = numero1 + numero2
            divi = numero1 / numero2 # divisao comum
            mult = numero1 * numero2
            sub = numero1 - numero2
           
        
            if opcao2 == "1":
                print("o Resultado da soma:",numero1, "+",numero2, "é:", soma)
            elif opcao2 == "2":
                print("o Resultado da divisão:",numero1, "/",numero2, "é:", divi)
            elif opcao2 == "3":
                print("o Resultado da multiplicação:",numero1, "x",numero2, "é:", mult)   
            elif opcao2 == "4":
                print("o Resultado da multiplicação:",numero1, "x",numero2, "é:", mult)  
            elif opcao2 == "5":
                break
                
            
    elif opcao == "4":
        print(f'Nome: {saudacao} | Telefone: {telefone}' )
        print(f'CPF: {cpf} | Data de nascimento: {data_nasc}') 
    elif opcao == "5":
        linhas = 15
        j = 1

        while j<= linhas:
                espacos = linhas - j
                estrelas = 2 * j - 1

                print(" " * espacos + "^" * estrelas)
                j +=1


    elif opcao == "6":
        print('Saindo do sistema...')
        break
    else:
        print('Opção Inválida!')
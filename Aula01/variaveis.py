nome = "Cristiano"
idade = 16
nascimento = "01/04/2009"
print("Olá, me chamo", nome,"," "tenho", idade, "anos de idade e nasci no dia", nascimento) 

# Tipos de variáveis

nome = "Cristiano"
idade = 25
altura = 1.85
ativo = True

print("o tipo da variável é:",type(nome))
print("o tipo da variável é:",type(idade))
print("o tipo da variável é:",type(altura))
print("o tipo da variável é:",type(ativo))

# Operadores
print(30*'-','operadores',30*'-')
numero1 = 69
numero2 = 10
soma = numero1 + numero2
divi = numero1 / numero2 # divisao comum
divisao_inteira = numero1 // numero2 # divisão inteira
mult = numero1 * numero2
expo = numero1 ** numero2
sub = numero1 - numero2
resto = numero1 %2

print("o Resultado da soma:",numero1, "+",numero2, "é:", soma)
print("o Resultado da divisão:",numero1, "/",numero2, "é:", divi)
print("o Resultado da multiplicação:",numero1, "x",numero2, "é:", mult)
print("o Resultado da subtração:",numero1, "-",numero2, "é:", sub)
print("o Resultado da divisão inteira:",numero1, "/",numero2, "é:", divisao_inteira)
print("o Resultado do resto de:",numero1, "/",numero2, "é:", resto)
print("o Resultado da exponenciação entre:",numero1, "e",numero2, "é:", expo)

print()
print(30*'-','Operadores de comparação',30*'-')
# Operadores de comparação
numero1 > numero2
numero1 < numero2
numero1 == numero2
numero1 >= numero2
numero1 <= numero2
numero1 != numero2

ano = 2025
print("ano atual:", ano)
ano += 1
print('ano acrescido de +1:',ano)
ano -= 1
print('ano decrescido de -1:', ano)

# Operadores lógicos
# AND, OR, NOT

# Entrada de dados

print()
print(30*'-','Entrada de dados',30*'-')

nome_usuario = input("Digite o seu nome: ")
print('Seja bem-vindo ao sistema python', nome_usuario,"!!!")

# Calculadora básica

print()
print(30*'-','Calculadora Básica',30*'-')

numero1 = int(input('digite o primeiro número:'))
numero2 = int(input('digite o segundo número:'))
soma = numero1 + numero2
divi = numero1 / numero2 # divisao comum
divisao_inteira = numero1 // numero2 # divisão inteira
mult = numero1 * numero2
expo = numero1 ** numero2
sub = numero1 - numero2
resto = numero1 %2

print("o Resultado da soma:",numero1, "+",numero2, "é:", soma)
print("o Resultado da divisão:",numero1, "/",numero2, "é:", divi)
print("o Resultado da multiplicação:",numero1, "x",numero2, "é:", mult)
print("o Resultado da subtração:",numero1, "-",numero2, "é:", sub)
print("o Resultado da divisão inteira:",numero1, "/",numero2, "é:", divisao_inteira)
print("o Resultado do resto de:",numero1, "/",numero2, "é:", resto)
print("o Resultado da exponenciação entre:",numero1, "e",numero2, "é:", expo)

# Converte tipos de dados
print()
print(30*'-','Convertendo tipos de dados',30*'-')

ano_nascimento = input("Digite seu ano de nascimento:")
print(type(ano_nascimento))

# convertendo para inteiro
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))

saudacao = input('Digite seu nome:')
cpf = input('Digite seu CPF:')
telefone = input('Digite seu telefone:')

print(20*'-','Dados Pessoais',20*'-')
print('Nome:', saudacao)
print('CPF:', cpf, '| Telefone:' ,telefone)

print(50*'-')














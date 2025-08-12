#FIXME - concatenação com +
nome = "Cris"
idade = 16
altura = 1.85

# saída de dados
print("olá, meu nome é," + nome + ', tenho' + str(idade) + 'anos de idade')

#FIXME - concatenação com ,
print('olá, meu nome é', nome, ',tenho', idade, 'anos de idade')
#FIXME - concatenação com format
print('Olá, meu nome é {} , tenho  {}  anos de idade'.format(nome,idade))
#FIXME - concatenação com f-string
print(f'olá, meu nome é {nome} e tenho {idade+1} anos de idade')

# eliminando quebra de linha
print('O sábio sabia', end= "")
print(' Que o sabiá sabia assobiar.')

valor = 1.23456789
# exibindo o valor com duas casas depois da vírgula
print(f'{valor:.3f}')
print(50*'=')
peso = input('Digite seu peso:').replace(',','.')
peso = float(peso)
print(peso)

# Questão 4 da Atividade
numero = str(20)
numero = int(20)
numero2 = int(input('Digite o número a ser somado com 20:'))
print(f'A soma do seu número com 20 é:{numero + numero2}')
print(numero + numero2)

# calculadora IMC
peso = float(input("Digite seu peso:"))
altura = float(input("digite sua altura:"))
IMC = peso / altura ** 2
print(f'O seu imc é de:, {IMC:.2f}')
if IMC <18.5:
    print("Coma, você está abaixo do peso!")
elif IMC <= 24.9:
    print("Parabéns! Você está no peso ideal!")
elif IMC <= 29.9:
    print("Tome cuidado, você está com sobrepeso!")
elif IMC >= 30.0:
    print("Você tem obesidade...")       

# IF else de idade

idade = int(input("Digite sua idade:"))

if idade >= 18:
    print('Você é maior de idade!')
    print('Você está dentro do bloco IF')
else:
    print('Você é menor de idade!')
    print('Você está dentro do bloco ELSE')
print('Você está fora da estrutura condicional if else')

# Boletim escolar

print(40*'-','Boletim escolar',40*'-')
nome_aluno = str(input('Digite o nome do aluno:')).upper()
nota1 = float(input('Digite a nota do primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimestre: '))
nota3 = float(input('Digite a nota do terceiro bimestre: '))
nota4 = float(input('Digite a nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4)/4
if media >= 7:
    print(f"{nome_aluno}, Voce está aprovado!")
    print(f'Nota 1: {nota1} | Nota 2: {nota2}' )
    print(f'Nota 3: {nota3} | Nota 4 {nota4}') 
    print('sua média foi de: ', media)
elif media >= 5:
    print(f"{nome_aluno}, Você está de recuperação!")
    print(f'Nota 1: {nota1} | Nota 2: {nota2}' )
    print(f'Nota 3: {nota3} | Nota 4 {nota4}') 
    print(20*'-')
    print(f'sua média foi de:  {media}')
else:
    print(f"{nome_aluno}, Você está de recuperação!")
    print(f'Nota 1: {nota1} | Nota 2: {nota2}' )
    print(f'Nota 3: {nota3} | Nota 4 {nota4}') 
    print('sua média foi de: ', media)
    print(20*'-')

# Requisitos mínimos de usuário
print(20* '-', 'parque de diversões', 20* '-')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade:'))
altura = float(input('Digite sua altura:'))
if idade >=12 or altura >= 1.4:
    print(f'Sua entrada está autorizada, senhor {nome} ')
else:
    print(f'Sua entrada não foi autorizada, senhor {nome} ')

# operador ternário
nome1 = str(input('Digite o nome: '))
idade1 = int(input('Digite sua idade: '))
print(nome1, 'é maior de idade. ' if idade1 >= 18 else 'é menor de idade.')



        
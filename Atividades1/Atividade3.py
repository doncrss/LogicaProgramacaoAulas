'''
    Boletim Escolar
'''

print(40*'-','Boletim escolar',40*'-')
nome_aluno = str(input('Digite o nome do aluno:')).upper()
nota1 = float(input('Digite a nota do primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimestre: '))
nota3 = float(input('Digite a nota do terceiro bimestre: '))
nota4 = float(input('Digite a nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4)/4
if media >= 7:
    print(f"o aluno {nome_aluno} está aprovado!")
    print(f'Nota 1: {nota1} | Nota 2: {nota2}' )
    print(f'Nota 3: {nota3} | Nota 4 {nota4}') 
    print('sua média foi de: ', media)
elif media >= 5:
    print(f"o aluno {nome_aluno} está de recuperação!")
    print(f'Nota 1: {nota1} | Nota 2: {nota2}' )
    print(f'Nota 3: {nota3} | Nota 4 {nota4}') 
    print(20*'-')
    print(f'sua média foi de:  {media}')
else:
    print(f" o aluno {nome_aluno} está de recuperação!")
    print(f'Nota 1: {nota1} | Nota 2: {nota2}' )
    print(f'Nota 3: {nota3} | Nota 4 {nota4}') 
    print('sua média foi de: ', media)
    print(20*'-')

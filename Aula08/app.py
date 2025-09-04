import random
import string

def gerar_senha(comprimento=12, incluir_maiusculo=True, incluir_minusculo=True,
                incluir_numero=True, incluir_caracter=True):
    
    caracteres = ''
    if incluir_maiusculo:
        caracteres += string.ascii_uppercase

    if incluir_minusculo:
        caracteres += string.ascii_lowercase
    
    if incluir_numero:
        caracteres += string.punctuation
    
    if incluir_caracter:
        caracteres += string.punctuation
    
    if not caracteres:
        return ValueError('Deve ter pelo menos um tipo de caractere')

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f'Senha: {senha}')
    return senha

    

def main():
    print('Gerador de senhas fortes')
    comprimento = int(input('Digite o comprimento da senha (Padrão é 12: )') or 12)
    incluir_maiusculo = input('Incluir maiúscula (s/n, padrão = sim):').lower != 'n'
    incluir_minusculo = input('Incluir minúscula (s/n, padrão = sim):').lower != 'n'
    incluir_numero = input('Incluir números (s/n, padrão = sim):').lower != 'n'
    incluir_caracter = input('Incluir caractere especial (s/n, padrão = sim):').lower != 'n'
    senha = gerar_senha(comprimento, incluir_maiusculo, incluir_minusculo, incluir_numero, incluir_caracter)

    print(f'A senha gerada foi: {senha}')
    with open('senhas.txt', 'a') as s:
        s.write(f'\n{senha}')


if __name__ == '__main__':
    main()


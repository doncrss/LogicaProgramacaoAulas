'''
    Contador de números em ordem crescente
'''
lista = []
print(30*'-', 'Organizador de números em ordem crescente', 30*'-')
while True:
    numeros = (input('Digite um número ou S para finalizar: ')).lower()
    if numeros == 's':
        lista.sort()
        print(f' os números digitados em ordem crescente são {lista}')
        break
    else:
        lista.append(numeros)
        continue
        

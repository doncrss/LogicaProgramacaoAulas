import os

while True:
    try:
        novo_texto = input('Digite o texto: \n')
        nome_arquivo = input('Digite o nome do arquivo (sem extensão): ').strip().lower()

        with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas\Aula05/{nome_arquivo}.txt', 'w', encoding='utf-8') as f:
            f.write(novo_texto)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{nome_arquivo}.txt gravado com sucesso.')

        novo_texto_add = input('Digite o novo texto: \n')
        

        with open(fr'C:\Users\ead\Desktop\LogicaProgramacaoAulas\Aula05/{nome_arquivo}.txt', 'a', encoding='utf-8') as f:
            f.write(f'\n{novo_texto_add}')
        print('Gravado com sucesso.')

        # Ler os dados atualizados
        with open(f'{nome_arquivo}.txt', 'r', encoding='utf-8' ) as f:
            texto_final = f.read()
        print(f'Texto final: {texto_final}')

        while True:
            prosseguir = input('Deseja abrir outro arquivo? (s/n): ').strip().lower()
            if prosseguir == 's' or prosseguir == 'n':
                break
            else:
                print('Opção inválida')
                continue
        match prosseguir:
            case 's':
                continue
            case 'n':
                break
    except Exception as e:
        break
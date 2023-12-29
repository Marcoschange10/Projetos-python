def analise_texto(texto):
    
    palavras = len(texto.split())
    caracteres = len(texto)
    linhas =texto.count('\n')+1

    print(f'Número de palavras {palavras}')
    print(f'Número de caracteres {caracteres}')
    print(f'Número de linhas {linhas}')





texto_usuario=input('Insira seu texto aqui: \n')

analise_texto(texto_usuario)

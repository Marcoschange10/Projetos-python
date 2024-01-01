import random 
import string

def gerar_senha(comprimento):
    caracteres =  string.ascii_lowercase + string.digits 
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

comprimento_senha = int(input('Digite o comprimento da senha desejado: '))

nova_senha = gerar_senha(comprimento_senha)

print(f'A senha gerada é: {nova_senha}')

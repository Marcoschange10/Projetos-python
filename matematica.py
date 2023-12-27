import math

# Solicita ao usuário que insira um número
numero = float(input("Digite um número: "))

# Arredonda o número para baixo usando math.floor()
numero_arredondado = math.floor(numero)

# Exibe o número arredondado para baixo
print(f"O número {numero} arredondado para baixo é: {numero_arredondado}")

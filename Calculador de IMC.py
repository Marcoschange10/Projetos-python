#Calculador de IMC

peso=float(input('Por favor, digite seu peso: '))
altura=float(input('Por favor digite sua altura: '))

calcula = peso / (altura*altura)

if calcula <= 18.5:
    print('Você está abaixo do peso')
elif calcula > 18.5 and calcula <= 24.9:
    print('Seu peso está normal')
else:
    print('Você está acima do peso') 

print(f'Seu IMC é de: {calcula:.2f}')

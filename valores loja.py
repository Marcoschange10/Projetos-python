print(f'{" LOJAS QUALQUER COISA ":=^35}')

preco=float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTO
      [1] à vista no dinheiro  
      [2] à vista no cartão
      [3] 2X no cartão
      [4] 3X ou mais no cartão ''')

opcao =int(input('Qual é a opção? '))

if opcao == 1:
   total = preco - (preco * 10 / 100)
   # 10% de desconto

elif opcao == 2:
   total = preco - (preco * 5 /100)
   # 5% de desconto

elif opcao == 3:
   total = preco - (preco * -5 / 100)
   print(f'Sua compra será em 2 vezes de: {total / 2:.2f}. Sendo no valor total de {total:.2f}')
   # 5 % de acréscimo 

elif opcao == 4:
   total = preco - (preco * -10 / 100)
   print(f'Sua compra sera em 3 vezes de: {total / 3:.2f}. Sendo no valor total de: {total:.2f}')
   # 10% de acréscimo 

else: 
   print('Opção invalida')

if opcao in (1, 2):
   print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final')
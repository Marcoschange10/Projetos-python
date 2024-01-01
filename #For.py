#nomes=['pedro', 'paula', 'maria']
#for item in nomes:
#    print (item)

'''
nomes=['pedro', 'paula', 'maria'] #assim ele lista a quantidade de itens
for index in range (len(nomes)):
    print(nomes[index], index)
'''
'''
for index in range (5):
    if index == 0:
        print('primeira linha')
    else:
        print(f"outras linhas {index}")
'''

matrix_numeros=[
    [1,2,3],
    [4,5,6], 
    [7,8,9],
    [0],
]

for linha in matrix_numeros:
    print('---')
    for coluna in linha:
        print(coluna)
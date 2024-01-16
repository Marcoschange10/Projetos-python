import PyPDF2
import os

diretorio = 'C:\\Users\\marco\\OneDrive\\Área de Trabalho\\arquivos para treinar\\diretorio_arquivos'

merger = PyPDF2.PdfMerger()

lista_arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.lower().endswith('.pdf')]
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
        caminho_arquivo = os.path.join(diretorio, arquivo)
        with open (caminho_arquivo, 'rb') as file: 
            merger.append(file)
caminho_final= os.path.join(diretorio, 'Pdf_Final.pdf')
merger.write(caminho_final)
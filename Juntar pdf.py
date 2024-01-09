import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir('Pdf')
print(lista_arquivos)
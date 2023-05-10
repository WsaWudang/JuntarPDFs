import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir(r'C:\Users\wesle\OneDrive\Área de Trabalho\Wesley\CursoFrontEnd\Pdfs')

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"C:/Users/wesle/OneDrive/Área de Trabalho/Wesley/CursoFrontEnd/Pdfs/{arquivo}")

merger.write("PDF_Final.pdf")
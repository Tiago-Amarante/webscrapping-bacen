import patoolib
import os 

with os.scandir(r'C:\Users\tadbc\OneDrive\Área de Trabalho\codigos\Multimarcas\webscrapping-bacen\dados_rar') as entries:
    for entry in entries:
        file_name = 'C:\\Users\\tadbc\\OneDrive\\Área de Trabalho\\codigos\\Multimarcas\\webscrapping-bacen\\dados_rar\\'+entry.name
        patoolib.extract_archive(file_name, 
                                 outdir=r"C:\Users\tadbc\OneDrive\Área de Trabalho\codigos\Multimarcas\webscrapping-bacen\dados_unrar")
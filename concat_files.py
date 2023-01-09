import pandas as pd
import glob

def append_files(file_specification):
    #read the path
    file_path = "webscrapping-bacen\dados_unrar"+file_specification
    #list all the files from the directory
    file_list = glob.glob(file_path)

    df_concat = pd.concat((pd.read_csv(file, sep=';',encoding='mbcs') for file in file_list),ignore_index=True)
    return df_concat

df_moveis = append_files("\*_Moveis_Grupos.csv")
df_imoveis = append_files("\*_Imoveis_Grupos.csv")
df_segmentos = append_files("\*Segmentos_Consolidados.csv")

df_moveis.to_csv("webscrapping-bacen\dados_concatenados\Moveis.csv", sep=';', encoding='utf-8-sig',index=None)
df_imoveis.to_csv("webscrapping-bacen\dados_concatenados\Imoveis.csv", sep=';', encoding='utf-8-sig',index=None)
df_segmentos.to_csv("webscrapping-bacen\dados_concatenados\Segmentos.csv", sep=';', encoding='utf-8-sig',index=None)
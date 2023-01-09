# webscrapping-bacen
Projeto em andamento...

Este projeto tem o objetivo de extrair os dados do Banco Central sobre as administradoras de consórcio. 

O site do BACEN possui uma proteção que impossibilitou a raspagem diretamente via Browser Driver(e.g. Selenium). Para realizar essa tafa tive o auxílio do meu amigo Daniel Hott. A solução encontrata pode ser vista aqui:

https://github.com/DanielHott/automacao-dados-consolidados

Em resumo ele encontrou o URL que solicita o download, por sorte este URL possui os parâmetros de data de forma explicita que pudemos utilizar para baixar todos os dados necessários.

Então de forma simples este projeto faz o download de qualquer planilha da página 
https://www.bcb.gov.br/estabilidadefinanceira/consorciobd
descompacta estes arquivos e concatena as diversas planilhas de acordo com a data escolhida. 
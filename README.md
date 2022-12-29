# webscrapping-bacen
Projeto em andamento...

Este projeto tem o objetivo de extrair os dados do Banco Central sobre as administradoras de consórcio. 

O site do BACEN possui uma proteção que impossibilitou a raspagem diretamente via Browser Driver(e.g. Selenium). Para realizar essa tafa tive o auxílio do meu amigo Daniel Hott. A solução encontrata pode ser vista aqui:

https://github.com/DanielHott/automacao-dados-consolidados

Em resumo ele encontrou o URL que solicita o download, por sorte este URL possui os parâmetros de data de forma explicita que pudemos utilizar para baixar todos os dados necessários.

Utilizo o código dele como referência para o download dos dados.E dou sequência aos processos de extração, tratamento e geração do dataset para futuras aplicações em inteligÊncia de mercado. 
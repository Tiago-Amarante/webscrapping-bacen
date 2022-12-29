print("O Programa começou a rodar")

import undetected_chromedriver as uc
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions() 
options.headless = True
driver = uc.Chrome(options=uc.options.ChromeOptions())
for ano in reversed(range(23)):
    print(ano)
    for mes in reversed(range(13)):
        if 0 < ano < 10 and 0 < mes < 10:
          driver.get(f'https://www.bcb.gov.br/Fis/Consorcios/Port/BD/200{ano}0{mes}Consorcios.zip')
          sleep(2)
          
        elif 0 < ano < 10 and 0 < mes >= 10:
          driver.get(f'https://www.bcb.gov.br/Fis/Consorcios/Port/BD/200{ano}{mes}Consorcios.zip')
          sleep(2)
        
        elif 0 < ano >= 10 and 0 < mes >= 10:
            driver.get(f'https://www.bcb.gov.br/Fis/Consorcios/Port/BD/20{ano}{mes}Consorcios.zip')
            sleep(2)
        
        elif 0 < ano >= 10 and 0 < mes < 10:
            driver.get(f'https://www.bcb.gov.br/Fis/Consorcios/Port/BD/20{ano}0{mes}Consorcios.zip')
            sleep(2)
            
        elif ano == 0:
            for extra_ano in reversed(range(96, 100)):
                print(extra_ano)
                if 0 < mes >= 10:
                    driver.get(f'https://www.bcb.gov.br/Fis/Consorcios/Port/BD/19{extra_ano}{mes}Consorcios.zip')
                    sleep(2)
                elif 0 < mes < 10:
                    driver.get(f'https://www.bcb.gov.br/Fis/Consorcios/Port/BD/19{extra_ano}0{mes}Consorcios.zip')
                    sleep(2)
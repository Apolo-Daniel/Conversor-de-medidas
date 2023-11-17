from Texto import *
from Graus import *
from Distancia import *
from time import sleep

cabecalho()

while True:
    try:
        escolha = int(input('Escolha uma das opções: '))
        if escolha == 0:
            print('Encerrando o programa...')
            sleep(1)
            break
    except (ValueError, TypeError):
        print('\033[1:31mERRO! Digite um número inteiro válido!')
        continue
    else:
        number = float(input('Valor a ser calculado: '))
        if escolha == 1:
            print(f'{celsius_fahrenheit(number):.2f}Fº')
        elif escolha == 2:
            print(f'{fahrenheit_celsius(number):.2f}Cº')
        elif escolha == 3:
            print(f'{km_mh(number):.2f}mi')
        elif escolha == 4:
            print(f'{mh_km(number):.2f}Km')
        else:
            print('\033[1:31mERRO! Escolha um número válido!')
            continue
        cabecalho()

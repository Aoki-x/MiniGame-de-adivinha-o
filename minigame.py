import random
import os
import time
start = False
welcome_message = '''->>>>>\tSeja Bem-vindo(a) Ao jogo de Adivinhação\t<<<<<-\n\t\tDeseja Jogar?\n\t\tDigite \'START\''''

start = str(input(welcome_message))
if start == 'START':
    start = True
    luckyNumber = random.randint(0, 50)
    print('O Número já foi sorteado, tente descobrir qual foi.')

while start:
        whoIsLuckyNumber = int(input('QUAL FOI O NÚMERO SORTEADO?'))
        print(luckyNumber)
        if whoIsLuckyNumber == luckyNumber:
            print(f'Você acertou!!\nO número acertado era {luckyNumber}')
            time.sleep(2)
            os.system('cls')
            start = False
        elif whoIsLuckyNumber == luckyNumber-5 or whoIsLuckyNumber == luckyNumber+5:
            print('Passou perto!!')
        elif whoIsLuckyNumber < luckyNumber:
            print('Tente aumentar mais.')
        elif whoIsLuckyNumber > luckyNumber:
            print('Tente um número mais abaixo.')
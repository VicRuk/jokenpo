import random
import os

pedra = "pedra"
papel = "papel"
tesoura = "tesoura"
ptsPlayer1 = 0
ptsPlayer2 = 0
ptsIA1 = 0
ptsIA2 = 0

#Programa estar rodando ou não: Ao declarar como falso, ele para
a = True

print('''

░░█ █▀█ █▄▀ █▀▀ █▄░█ █▀█ █▀█
█▄█ █▄█ █░█ ██▄ █░▀█ █▀▀ █▄█
      
      ''')
modo = input("Qual o modo de jogo? (1 - Player X Player / 2 - Player X IA / 3 - IA X IA / 0 - SAIR) ")
if modo == "1":
    print("Você escolheu o modo Player vs Player")
elif modo == "2":
    print("Você escolheu o modo Player vs IA")
elif modo == "3":
    print("Você escolheu o modo IA vs IA")
elif modo == "0":
    print("Saiu")
    a = False
else:
    print("Insira um modo válido")
    a = False

#MODO PLAYER 1 VS PLAYER 2
while modo == "1" and a:
    player1 = input("Digite sua escolha (Pedra / Papel / Tesoura)! ")
    os.system('cls') or None
    player2 = input("Digite sua escolha (Pedra / Papel / Tesoura)! ")
    os.system('cls') or None

    if player1 == "pedra":
        if player2 == "pedra":
            print("Player 1 escolheu", player1, "\nPlayer 2 escolheu", player2, "\nEmpate!")
        elif player2 == "papel":
            print("Player 1 escolheu", player1, "\nPlayer 2 escolheu", player2, "\nPlayer 2 ganhou!")
            ptsPlayer2 += 1
        elif player2 == "tesoura":
            print("Player 1 escolheu", player1, "\nPlayer 2 escolheu", player2, "\nPlayer 1 ganhou!")
            ptsPlayer1 += 1
        else:
            print("PLAYER 2 NÃO INSERIU UMA JOGADA VÁLIDA")

    elif player1 == "papel":
        if player2 == "pedra":
            print("Player 1 escolheu", player1, "\nPlayer 2 escolheu", player2, "\nPlayer 1 ganhou!")
            ptsPlayer1 += 1
        elif player2 == "papel":
            print("Player 1 escolheu", player1, "\nPlayer 2 escolheu", player2, "\nEmpate!")
        elif player2 == "tesoura":
            print("Player 1 escolheu", player1, "\nPlayer 2 escolheu", player2, "\nPlayer 2 ganhou!")
            ptsPlayer2 += 1
        else:
            print("PLAYER 2 NÃO INSERIU UMA JOGADA VÁLIDA")
    
    elif player1 == "tesoura":
        if player2 == "pedra":
            print("Player 1 escolheu", player1, "\nPlayer 2 escolheu", player2, "\nPlayer 2 ganhou!")
            ptsPlayer2 += 1
        elif player2 == "papel":
            print("Player 1 escolheu", player1, "\nPlayer 2 escolheu", player2, "\nPlayer 1 ganhou!")
            ptsPlayer1 += 1
        elif player2 == "tesoura":
            print("Player 1 escolheu", player1, "\nPlayer 2 escolheu", player2, "\nEmpate!")
        else:
            print("PLAYER 2 NÃO INSERIU UMA JOGADA VÁLIDA")
    
    else:
        print("PLAYER 1 NÃO INSERIU UMA JOGADA VÁLIDA")

    continuar = input("CONTINUAR OU SAIR? ")
    #Se não for continuar ou sair, ele vai repetir
    while continuar != "continuar" and continuar != "sair":
        continuar = input("NÃO ENTENDI. CONTINUAR OU SAIR? ")
    if continuar == "continuar":
        a = True
    elif continuar == "sair":
        print("Player 1: ", ptsPlayer1, " pontos!\nPlayer 2: ", ptsPlayer2, " pontos!\n")
        print("Obrigado por jogar!\nJokenpo feito por Mateus Roese\nMatheus Yamamoto\nVictor Augusto\nVictor Tamezava")
        a = False

#MODO PLAYER 1 VS IA
while modo == "2" and a:
    #Gerador Jogada IA1
    computador_1 = random.randint(1, 3)
    if computador_1 == 1:
        ia1 = pedra
    elif computador_1 == 2:
        ia1 = papel
    else:
        ia1 = tesoura

    player1 = input("Digite sua escolha (Pedra / Papel / Tesoura)! ")

    if player1 == "pedra":
        if ia1 == "pedra":
            print("Player 1 escolheu", player1, "\nIA 1 escolheu", ia1, "\nEmpate!")
        elif ia1 == "papel":
            print("Player 1 escolheu", player1, "\nIA 1 escolheu", ia1, "\nIA ganhou!")
            ptsIA1 += 1
        elif ia1 == "tesoura":
            print("Player 1 escolheu", player1, "\nIA 1 escolheu", ia1, "\nPlayer 1 ganhou!")
            ptsPlayer1 += 1

    elif player1 == "papel":
        if ia1 == "pedra":
            print("Player 1 escolheu", player1, "\nIA 1 escolheu", ia1, "\nPlayer 1 ganhou!")
            ptsPlayer1 += 1
        elif ia1 == "papel":
            print("Player 1 escolheu", player1, "\nIA 1 escolheu", ia1, "\nEmpate!")
        elif ia1 == "tesoura":
            print("Player 1 escolheu", player1, "\nIA 1 escolheu", ia1, "\nIA ganhou!")
            ptsIA1 += 1

    elif player1 == "tesoura":
        if ia1 == "pedra":
            print("Player 1 escolheu", player1, "\nIA 1 escolheu", ia1, "\nIA ganhou!")
            ptsIA1 += 1
        elif ia1 == "papel":
            print("Player 1 escolheu", player1, "\nIA 1 escolheu", ia1, "\nPlayer 1 ganhou!")
            ptsPlayer1 += 1
        elif ia1 == "tesoura":
            print("Player 1 escolheu", player1, "\nIA 1 escolheu", ia1, "\nEmpate!")

    else:
        print("PLAYER 1 NÃO INSERIU UMA JOGADA VÁLIDA")

    continuar = input("CONTINUAR OU SAIR? ")
    #Se não for continuar ou sair, ele vai repetir
    while continuar != "continuar" and continuar != "sair":
        continuar = input("NÃO ENTENDI. CONTINUAR OU SAIR? ")
    if continuar == "continuar":
        a = True
    elif continuar == "sair":
        print("Player 1: ", ptsPlayer1, " pontos!\nIA: ", ptsIA1, " pontos!\n")
        print("Obrigado por jogar!\nJokenpo feito por Mateus Roese\nMatheus Yamamoto\nVictor Augusto\nVictor Tamezava")
        a = False

#MODO IA VS IA
while modo == "3" and a:
    #Gerador Jogada IA1
    computador_1 = random.randint(1, 3)
    if computador_1 == 1:
        ia1 = pedra
    elif computador_1 == 2:
        ia1 = papel
    else:
        ia1 = tesoura
    
    #Gerador Jogada IA2
    computador_2 = random.randint(1, 3)
    if computador_2 == 1:
        ia2 = pedra
    elif computador_2 == 2:
        ia2 = papel
    else:
        ia2 = tesoura

    if ia1 == "pedra":
        if ia2 == "pedra":
            print("IA 1 escolheu", ia1, "\nIA 2 escolheu", ia2, "\nEmpate!")
        elif ia2 == "papel":
            print("IA 1 escolheu", ia1, "\nIA 2 escolheu", ia2, "\nIA 2 ganhou!")
            ptsIA2 += 1
        elif ia2 == "tesoura":
            print("IA 1 escolheu", ia1, "\nIA 2 escolheu", ia2, "\nIA 1 ganhou!")
            ptsIA1 += 1

    elif ia1 == "papel":
        if ia2 == "pedra":
            print("IA 1 escolheu", ia1, "\nIA 2 escolheu", ia2, "\nIA 1 ganhou!")
            ptsIA1 += 1
        elif ia2 == "papel":
            print("IA 1 escolheu", ia1, "\nIA 2 escolheu", ia2, "\nEmpate!")
        elif ia1 == "tesoura":
            print("IA 1 escolheu", ia1, "\nIA 2 escolheu", ia2, "\nIA 2 ganhou!")
            ptsIA2 += 1

    elif ia1 == "tesoura":
        if ia2 == "pedra":
            print("IA 1 escolheu", ia1, "\nIA 2 escolheu", ia2, "\nIA 2 ganhou!")
            ptsIA2 += 1
        elif ia2 == "papel":
            print("IA 1 escolheu", ia1, "\nIA 2 escolheu", ia2, "\nIA 1 ganhou!")
            ptsIA1 += 1
        elif ia2 == "tesoura":
            print("IA 1 escolheu", ia1, "\nIA 2 escolheu", ia2, "\nEmpate!")

    continuar = input("CONTINUAR OU SAIR? ")
    #Se não for continuar ou sair, ele vai repetir
    while continuar != "continuar" and continuar != "sair":
        continuar = input("NÃO ENTENDI. CONTINUAR OU SAIR? ")
    if continuar == "continuar":
        a = True
    elif continuar == "sair":
        print("IA 1: ", ptsIA1, " pontos!\nIA 2: ", ptsIA2, " pontos!\n")
        print("Obrigado por jogar!\nJokenpo feito por Mateus Roese\nMatheus Yamamoto\nVictor Augusto\nVictor Tamezava")
        a = False
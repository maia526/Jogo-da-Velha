tabuleiro = [
    ['1','2','3'],
    ['4','5','6'], 
    ['7','8','9']
    ]

def user_input(jogador):
    #RECEBE O INPUT DO JOGADOR, VERIFICA SE A JOGADA É VÁLIDA E REGISTRA A JOGADA NO TABULEIRO
    coluna0 = [1, 4, 7]
    coluna1 = [2, 5, 8]
    coluna2 = [3, 6, 9]
    if jogador % 2 == 0:
        print("\nVez do jogador 1")
    if jogador % 2 != 0:
        print("\nVez do jogador 2")
    active = True
    while(active):
        jogada = int(input("\nDigite uma posição de 1 a 9 no tabuleiro: "))
        if (jogada > 0 and jogada < 10):
            print(f"\nPosição {jogada} válida.")
            active = False
        else:
            print(f"\nPosição {jogada} inválida.")

    if jogador % 2 == 0:
        if jogada in coluna0:
            tabuleiro[int((jogada-1)/3)][0] = 'X'
        if jogada in coluna1:
            tabuleiro[int((jogada-1)/3)][1] = 'X'
        if jogada in coluna2:
            tabuleiro[int((jogada-1)/3)][2] = 'X'
    if jogador % 2 != 0:
        if jogada in coluna0:
            tabuleiro[int((jogada-1)/3)][0] = 'O'
        if jogada in coluna1:
            tabuleiro[int((jogada-1)/3)][1] = 'O'
        if jogada in coluna2:
            tabuleiro[int((jogada-1)/3)][2] = 'O'

def draw_table():
    #DESENHA O TABULEIRO
    for i in range(3):
        print(tabuleiro[i])

def check_win(jogador):
    jogador_1 = ['X', 'X', 'X']
    jogador_2 = ['O', 'O', 'O']
    if jogador % 2 == 0:
        if tabuleiro[0] == jogador_1 or tabuleiro[1] == jogador_1 or tabuleiro[2] == jogador_1:
            return True
        elif [tabuleiro[0][0], tabuleiro[1][0], tabuleiro[2][0]] == jogador_1 or [tabuleiro[0][1], tabuleiro[1][1], tabuleiro[2][1]] == jogador_1 or [tabuleiro[0][2], tabuleiro[1][2], tabuleiro[2][2]] == jogador_1:
            return True
        elif [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]] == jogador_1 or [tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]] == jogador_1:
            return True
        else:
            return False


#O JOGO EM SI
active = True
while(active):
    draw_table()
    for play in range(9):
        if play % 2 == 0:
            user_input(play)
            draw_table()
            win = check_win(play)

            if win == True:
                print("Jogador 1 ganhou!\n")
                active = False
        if active == False:
            break
        if play % 2 != 0:
            user_input(play)
            draw_table()
            win = check_win(play)

            if win == True:
                print("Jogador 2 ganhou!\n")
                active = False
        if active == False:
            break

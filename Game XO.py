''' Игра «Крестики-нолики» '''

board = list(range(1, 10))    #список 1-9

# функция territory() рисует игровое поле 3x3 с цифрами от 1 до 9, горизонтально разделенное тире, а вертикально символом "|"
def territory(board):                           
    print("—" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")       # в первом круге i=0, во втором =1, в третем =2.  board=1,2,3- каждый круг.
        print("—" * 13)


# функция take_input() с аргументом player_token принимает и работает с вводимыми значениями
def take_input(player_token):
    flag = False
    while not flag:                   # цикл не закончится, пока flag не станет True. 
        enter_num = input("Введити цифру, куда поставим " + player_token + ":  ")
        try:
            enter_num = int(enter_num)            
        except ValueError:
            print("Некорректный ввод. Надо вводить цифру от 1 до 9.")
            continue
        if 1 <= enter_num <= 9:
            if str(board[enter_num - 1]) not in "XO":       # проверяем если в клетке доски не стоит Х или О, тогда меняем цифру    
                board[enter_num - 1] = player_token      # индекс доски равен Х или О вводимого числа (-1 так как индексация начинается с ноля).
                flag = True
            else:
                print("Клетка занята!")
        else:
            print("Некорректный ввод. Введите цифру от 1 до 9.")


# проверяем выигрышные комбинации по кортежу win
def bingo(board):                           
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for j in win:
        if board[j[0]] == board[j[1]] == board[j[2]]:
            return board[j[0]]
    return False


# в функции в цикле проверяем, какой игрок походил, после чего вызывается функция take_input() с символом игрока. Далее идёт проверка, какой игрок выиграл, или ничья.
def final(board):
    counter = 0
    flg = False
    while not flg:
        territory(board)        
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        x_o = bingo(board)
        if x_o:
            print(f" ★ ☆ ★  {x_o} выиграл!!! ★ ☆ ★ ")
            flg = True
            break
        if counter == 9:
            print("Ничья!")
            break
    territory(board)


final(board)


input("Для выхода нажмите Enter")
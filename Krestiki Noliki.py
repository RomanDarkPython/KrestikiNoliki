table = list(range(1, 10))
def draw_table(table):
    print("-------------")
    for i in range(3):
        print("|", table[0 + i * 3], "|", table[1 + i * 3], "|", table[2 + i * 3], "|")
        print("-------------")

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставите " + player_token + "?")
        try:
            player_answer = int(player_answer)
        except:
            print("Ошибка! Введите число")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(table[player_answer-1]) not in "XO"):
                table[player_answer-1] = player_token
                valid = True
            else:
                print("Эта ячейка занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(table):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if table[i[0]] == table[i[1]] == table[i[2]]:
            return table[i[0]]
    return False

def main(table):
    counter = 0
    win = False
    while not win:
        draw_table(table)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(table)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_table(table)

main(table)
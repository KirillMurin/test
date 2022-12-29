field = list(range(1, 10))
combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def draw_field():
    print('_____________')
    for i in range(3):
        print('|', field[0+i*3], '|' , field[1+i*3], '|' ,  field[2+i*3], '|')
    print('_____________')

def data_input(player):
    while True:
        value= input('Куда поставить: ' + player + '?')
        if not(value in '123456789'):
            print('Ошибка! Повторите ввод')
            continue
        value = int(value)
        if str(field[value - 1]) in 'XO':
            print('Клетка занята!')
            continue
        field[value - 1] = player
        break
def check_win():
    for each in combinations:
        if (field[each[0] - 1]) == (field[each[1] - 1]) == (field[each[2] - 1]):
            return field[each[1] - 1]
    else:
        return False

def main():
    counter = 0
    while True:
        draw_field()
        if counter % 2 == 0:
            data_input('X')
        else:
            data_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_field()
                print(winner, 'победил!')
                break
        counter += 1
        if counter > 8:
            draw_field()
            print('Ничья!')
            break
main()
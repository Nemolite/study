import random
# x - user,0-pk
game_place = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]
def step_pk():
    '''Ход ПК'''
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if game_place[x][y]=="_":
            game_place[x][y]="0"
            break

def step_user():
    '''Ход user'''
    while True:
        user_x = int(input("Введите координату x="))
        user_y = int(input("Введите координату y="))
        if game_place[user_x][user_y]=="_":
            game_place[user_x][user_y] = "x"
            break
        else:
            print("Вы ввели неправильные координаты")

def show_game_place():
    ''' Вывод игорового поля'''
    for i in range(3):
        for j in range(3):
            print(game_place[i][j],end=" ")
        print(end="\n")

def check_win(arr,sim):
    ''' Функция проверки победы'''
    marker = False
    # Проверяем горизонтальные клетки
    for i in range(len(arr)):
        if arr[i][0]==sim and arr[i][1]==sim and arr[i][2]==sim:
            marker = True
    # Проверяем вертикальные клетки
    for j in range(len(arr)):
        if arr[0][j]==sim and arr[1][j]==sim and arr[2][j]==sim:
            marker = True
    # Проверяем диагональные клетки (прямые)
    if arr[0][0]==sim and arr[1][1]==sim and arr[2][2]==sim:
        marker = True
    # Проверяем диагональные клетки (обратные)
    if arr[0][2]==sim and arr[1][1]==sim and arr[2][0]==sim:
        marker = True
    return marker

# Главная программа
print("Игра крестики-нолики")
while True:
    print("Ваш ход мисье!")
    show_game_place()
    step_user()
    if check_win(game_place, "x"):
        print("Вы победили")
        show_game_place()
        break

    show_game_place()

    print("Теперь мой ход!")
    step_pk()
    if check_win(game_place, "0"):
        print("Я победил")
        show_game_place()
        break


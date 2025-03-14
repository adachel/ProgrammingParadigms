# императивная, процедурной, структурная
def insert_zero(zone, x, y):
    if zone[x][y] == " ":
        zone[x][y] = "0"
    else: print("Ячейка занята, выберите другую")

def insert_plus(zone, x, y):
    if zone[x][y] == " ":
        zone[x][y] = "+"
    else:
        print("Ячейка занята, выберите другую")

def check_empty_zone(zone):
    for x in range(len(zone)):
        for y in range(len(zone)):
            if zone[x][y] == " ":
                return True
    return False

def print_zone(zone):
    for line in zone:
        print(line)


def game(zone):
    player1 = "one"
    player2 = "two"

    while check_empty_zone(zone):
        print(f"игрок {player1} делайте ход, введите координаты для '+' через пробел")
        try:
            x, y = map(int, input().split())
        except ValueError:
            print("Введите числа через пробел")
            continue
        if x < len(zone) and y < len(zone):
            insert_plus(zone, x, y)
        else:
            print("Координаты за пределами поля, введите другие")
            continue

        print_zone(zone)

        if not check_empty_zone(zone):
            break

        print(f"игрок {player2} делайте ход, введите координаты для '0' через пробел")
        try:
            x, y = map(int, input().split())
        except ValueError:
            print("Введите числа через пробел")
            continue
        if x < len(zone) and y < len(zone):
            insert_zero(zone, x, y)
        else:
            print("Координаты за пределами поля, введите другие")
            continue

        print_zone(zone)



zone = [[" " for x in range(3)] for y in range(3)]
game(zone)
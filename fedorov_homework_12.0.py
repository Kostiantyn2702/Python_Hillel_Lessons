import random

class My15:
    def __init__(self):
        self.my_15 = self.generate_15()
        self.row, self.col = self.get_space()

    def generate_15(self):
        my_15 = [[], [], [], []]
        for index, list_ in enumerate(my_15):
            while len(list_) != 4:
                random_number = str(random.randint(1, 16))
                if random_number == "16":
                    random_number = ""
                uniqe_numbers = random_number not in my_15[0] and \
                                random_number not in my_15[1] and \
                                random_number not in my_15[2] and \
                                random_number not in my_15[3]
                if uniqe_numbers:
                    my_15[index].append(random_number)
        return my_15

    def print_15(self):
        for row in self.my_15:
            line = " ".join(f"{val:2}" for val in row)
            print(line)

    def get_space(self):
        row_ = 0
        col_ = 0
        for i, row in enumerate(self.my_15):
            if "" in row:
                row_ = i
                for j, col in enumerate(row):
                    if "" == col:
                        col_ = j
        return row_, col_

    def move_up(self):
        row, col = self.get_space()
        space = self.my_15[row][col]
        if row == 0:
            print("Нельзя передвинуть за границу поля!")
            print("###############################")
        else:
            self.my_15[row][col] = self.my_15[row - 1][col]
            self.my_15[row - 1][col] = space

    def move_down(self):
        row, col = self.get_space()
        space = self.my_15[row][col]
        if row == 3:
            print("Нельзя передвинуть за границу поля!")
            print("###############################")
        else:
            self.my_15[row][col] = self.my_15[row + 1][col]
            self.my_15[row + 1][col] = space

    def move_right(self):
        row, col = self.get_space()
        space = self.my_15[row][col]
        if col == 3:
            print("Нельзя передвинуть за границу поля!")
            print("###############################")
        else:
            self.my_15[row][col] = self.my_15[row][col + 1]
            self.my_15[row][col + 1] = space

    def move_left(self):
        row, col = self.get_space()
        space = self.my_15[row][col]
        if col == 0:
            print("Нельзя передвинуть за границу поля!")
            print("###############################")
        else:
            self.my_15[row][col] = self.my_15[row][col - 1]
            self.my_15[row][col - 1] = space


def field_print(game):
    print("_______________")
    game.print_15()
    print("_______________")

def loop_actions(game):
    solution = [["1", "2", "3", "4"],["5", "6", "7", "8"],["9", "10", "11", "12"], ["13", "14", "15", ""]]
    if game.my_15 == solution:
        congratulations = "Вы победили!"
        return print(congratulations)
    return actions(input(), game)

def actions(acting:str, game):
    if acting == "w":
        game.move_up()
        field_print(game)
        return loop_actions(game)
    elif acting == "s":
        game.move_down()
        field_print(game)
        return loop_actions(game)
    elif acting == "d":
        game.move_right()
        field_print(game)
        return loop_actions(game)
    elif acting == "a":
        game.move_left()
        field_print(game)
        return loop_actions(game)
    else:
        print("Вы нажали неверную кнопку!")
        field_print(game)
        return loop_actions(game)

def start_the_game():
    game = My15()
    print("Чтобы начать игру, нажмите 1.\nЧтобы выйти, нажмите 2.")
    acting = input()
    if acting == "1":
        print("Это ваше поле.")
        print("_______________")
        game.print_15()
        print("_______________")
        print("Выберите действие из списка: "
              "\nЧтобы передвинуть 'пустоту' вверх нажмите w."
              "\nЧтобы передвинуть 'пустоту' вниз нажмите s."
              "\nЧтобы передвинуть 'пустоту' вправо нажмите d."
              "\nЧтобы передвинуть 'пустоту' влево нажмите a.")
        actions(input(), game)
    else:
        print("Досвидания!")

start_the_game()

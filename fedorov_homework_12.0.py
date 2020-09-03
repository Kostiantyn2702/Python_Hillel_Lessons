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

    def field_print(self):
        print("_______________")
        self.print_15()
        print("_______________")

    def loop_actions(self):
        solution = [["1", "2", "3", "4"],["5", "6", "7", "8"],["9", "10", "11", "12"], ["13", "14", "15", ""]]
        if self.my_15 == solution:
            congratulations = "Вы победили!"
            return print(congratulations)
        return self.do_actions(input())

    def do_actions(self, acting:str):
        if acting == "w":
            self.move_up()
            self.field_print()
            return self.loop_actions()
        elif acting == "s":
            self.move_down()
            self.field_print()
            return self.loop_actions()
        elif acting == "d":
            self.move_right()
            self.field_print()
            return self.loop_actions()
        elif acting == "a":
            self.move_left()
            self.field_print()
            return self.loop_actions()
        else:
            print("Вы нажали неверную кнопку!")
            self.field_print()
            return self.loop_actions()

    def start_the_game(self):
        # game = My15()
        print("Чтобы начать игру, нажмите 1.\nЧтобы выйти, нажмите 2.")
        acting = input()
        if acting == "1":
            print("Это ваше поле.")
            print("_______________")
            self.print_15()
            print("_______________")
            print("Выберите действие из списка: "
                  "\nЧтобы передвинуть 'пустоту' вверх нажмите w."
                  "\nЧтобы передвинуть 'пустоту' вниз нажмите s."
                  "\nЧтобы передвинуть 'пустоту' вправо нажмите d."
                  "\nЧтобы передвинуть 'пустоту' влево нажмите a.")
            self.do_actions(input())
        else:
            print("Досвидания!")

my_15 = My15()

my_15.start_the_game()
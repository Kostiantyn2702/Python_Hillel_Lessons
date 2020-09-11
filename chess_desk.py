class Desk:

    def __init__(self):
        self.desk = self.my_empty_desk()
        # self.piece_type = piece_type
        # self.place = place
        pass

    def __repr__(self):
        return (
            """
              _______________
            8|_|_|_|_|_|_|_|_|
            7|_|_|_|_|_|_|_|_|
            6|_|_|_|_|_|_|_|_|
            5|_|_|_|_|_|_|_|_|
            4|_|_|_|_|_|_|_|_|
            3|_|_|_|_|_|_|_|_|
            2|_|_|_|_|_|_|_|_|
            1|_|_|_|_|_|_|_|_|
              A B C D E F G H
        """)

    def my_empty_desk(self):
        desk = {"A" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "B" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "C" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "D" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "E" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "F" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "G" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"},
        "H" : {"1": "Пусто","2": "Пусто","3": "Пусто","4": "Пусто","5": "Пусто","6": "Пусто","7": "Пусто","8": "Пусто"}}
        return desk

    def print_my_desk(self):
        my_desk_print = """
                      _______________
                    8|_|_|_|_|_|_|_|_|
                    7|_|_|_|_|_|_|_|_|
                    6|_|_|_|_|_|_|_|_|
                    5|_|_|_|_|_|_|_|_|
                    4|_|_|_|_|_|_|_|_|
                    3|_|_|_|_|_|_|_|_|
                    2|_|_|_|_|_|_|_|_|
                    1|_|_|_|_|_|_|_|_|
                      A B C D E F G H
                """
        pass



    def get_piece_on(self, place):
        piece_type = self.desk[place[0]][place[-1]]
        return piece_type

    def remove_piece_from(self, place):
        pass

    def add_piece_on(self, place, type_piece):
        self.desk[place[0]][place[-1]] = type_piece




# desk = Desk()
#
# desk.print_my_desk()
#
# # print(desk.get_piece_on("A1"))
# #
# desk.add_piece_on("A1", "Pawn")
# #
# # print(desk.desk)
# print("____________________")
# desk.print_my_desk()

my_desk_print = """
  _______________
|A8|B8|C8|D8|E8|F8|G8|H8|
|A7|B7|C7|D7|E7|F7|G7|H7|
|A6|B6|C6|D6|E6|F6|G6|H6|
|A5|B5|C5|D5|E5|F5|G5|H5|
|A4|B4|C4|D4|E4|F4|G4|H4|
|A3|B3|C3|D3|E3|F3|G3|H3|
|A2|B2|C2|D2|E2|F2|G2|H2|
|A1|B1|C1|D1|E1|F1|G1|H1|
    A  B  C D E F G H
"""

print(my_desk_print.find("8"))
print(my_desk_print.find("7"))
print(my_desk_print.find("6"))
print(my_desk_print.find("5"))
print(my_desk_print.find("4"))
print(my_desk_print.find("3"))
print(my_desk_print.find("2"))
print(my_desk_print.find("1"))

print(my_desk_print.find("A"))
print(my_desk_print.find("B"))
print(my_desk_print.find("C"))
print(my_desk_print.find("D"))
print(my_desk_print.find("E"))
print(my_desk_print.find("F"))
print(my_desk_print.find("G"))
print(my_desk_print.find("H"))



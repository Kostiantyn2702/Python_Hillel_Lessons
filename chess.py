class Piece:
    def __init__(self, color, place):
        self.color = color # Цвет фигуры
        self.place = place # Координата фигуры
        self.moves = [] # Возможные ходы фигуры
        self.takes = [] # Возможные атаки фигуры
        self.target = "" # Цель атаки/хода

    def __repr__(self):
        return f"----------------\n" \
               f"color: {self.color}\n" \
               f"place:{self.place}\n" \
               f"target:{self.target}\n" \
               f"moves:{self.moves}\n" \
               f"takes:{self.takes}\n" \
               f"----------------"

    def get_moves(self):
        raise Exception("must override in child class")

    def get_takes(self):
        raise Exception("must override in child class")

    def new_target(self):
        raise Exception("must override in child class")



class Pawn(Piece):
    def __init__(self, color, place):
        super().__init__(color, place)
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = ""

    def _get_cell_up(self, place: str) -> str:
        place_number = int(place[-1]) # Цифреное значение координаты
        new_number = place_number + 1 if place_number < 8 else place_number
        new_place = place.replace(str(place_number), str(new_number)) # Новая координата на которую может пойти пешка (белая)
        return new_place

    def _get_cell_down(self, place: str) -> str:
        place_number = int(place[-1])
        new_number = place_number - 1 if place_number > 1 else place_number
        new_place = place.replace(str(place_number), str(new_number))
        return new_place

    def _get_cell_left(self, place: str) -> str:
        place_symbol = place[0]
        new_symbol = chr(ord(place_symbol) - 1) if place_symbol != "A" else place_symbol
        new_place = place.replace(place_symbol, new_symbol)
        return new_place # Новая буква

    def _get_cell_right(self, place: str) -> str:
        place_symbol = place[0]
        new_symbol = chr(ord(place_symbol) + 1) if place_symbol != "H" else place_symbol
        new_place = place.replace(place_symbol, new_symbol)
        return new_place

    def _get_cell_diagonal_left_up(self, place: str) -> str:
        new_number = str(self._get_cell_up(place)[-1])
        new_symbol = self._get_cell_left(place)[0]
        new_place = new_symbol + new_number
        new_place = self.place.replace(place, new_place)
        return new_place

    def _get_cell_diagonal_right_up(self, place: str) -> str:
        new_number = str(self._get_cell_up(place)[-1])
        new_symbol = self._get_cell_right(place)[0]
        new_place = new_symbol + new_number
        new_place = self.place.replace(place, new_place)
        return new_place

    def _get_cell_diagonal_left_down(self, place: str) -> str:
        new_number = str(self._get_cell_down(place)[-1])
        new_symbol = self._get_cell_left(place)[0]
        new_place = new_symbol + new_number
        new_place = self.place.replace(place, new_place)
        return new_place

    def _get_cell_diagonal_right_down(self, place: str) -> str:
        new_number = str(self._get_cell_down(place)[-1])
        new_symbol = self._get_cell_right(place)[0]
        new_place = new_symbol + new_number
        new_place = self.place.replace(place, new_place)
        return new_place

    def get_moves(self) -> list:
        place_number = int(self.place[-1])
        if self.color == "white":
            new_place = self._get_cell_up(self.place) if place_number < 8 else self.place
        elif self.color == "black":
            new_place = self._get_cell_down(self.place) if place_number > 1 else self.place
        else:
            new_place = "Вы ввели неправильный цвет!"
        return [new_place]

    def get_takes(self) -> list:
        takes = []
        place_number = int(self.place[-1])
        if self.color == "white":
            if place_number != 8:
                takes.append(self._get_cell_diagonal_left_up(self.place))
                takes.append(self._get_cell_diagonal_right_up(self.place))
            else:
                takes.append("Атака влево невозможна!")
                takes.append("Атака вправо невозможна!")
        elif self.color == "black":
            if place_number != 1:
                takes.append(self._get_cell_diagonal_left_down(self.place))
                takes.append(self._get_cell_diagonal_right_down(self.place))
            else:
                takes.append("Атака влево невозможна!")
                takes.append("Атака вправо невозможна!")
        else:
            takes.append("Вы ввели неправильный цвет!")
        return takes

    def new_target(self):
        print("Выберите цель для хода.")
        new_target = input()
        self.move_on(new_target)
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = ""

    def move_on(self, target):
        self.place = target

class Queen(Piece):
    def __init__(self, color, place):
        super().__init__(color, place)
        self.moves = self.get_moves()
        self.takes = self.get_takes()
        self.target = self.new_target()

    def get_moves(self):
        return []

    def get_takes(self):
        return []

    def new_target(self):
        return "A1"


pawn = Pawn('black', 'D5')
print(pawn)
print(pawn.new_target())
print(pawn)
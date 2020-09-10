class Piece:
    def __init__(self, color, place):
        self.color = color # Цвет фигуры
        self.place = place # Координата фигуры
        self.moves = [] # Возможные ходы фигуры
        self.takes = [] # Возможные атаки фигуры
        self.target = "" # Цель атаки

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
        self.target = self.new_target()

    def get_moves(self):
        """
        Функция которая передает варианты для хода пешек в зависимости от цвета
        :return: Список возможных ходов для пешки
        """
        place_number = int(self.place[-1]) # Цифреное значение координаты
        if self.color == "white": # Условие хода для белых пешек
            new_place = self._get_cell_up(self.place) if place_number < 8 else self.place # Новая координата пешки если она не вверху доски
        else: # Условие хода для черных пешек
            new_place = self._get_cell_down(self.place) if place_number > 1 else self.place # Новая координата пешки если она не внизу доски
        return [new_place]

    def _get_cell_up(self, place:str) -> str:
        """
        Функция которая возвращает новую координату для хода пешки (белая)
        :param place: Текущая координата пешки
        :return: Новая координата пешки
        """
        place_number = int(place[-1]) # Цифреное значение координаты
        new_number = place_number + 1 # Новая позиция цифровой координаты
        new_place = place.replace(str(place_number), str(new_number)) # Новая координата на которую может пойти пешка (белая)
        return new_place

    def _get_cell_down(self, place):
        place_number = int(place[-1])
        new_number = place_number - 1
        new_place = place.replace(str(place_number), str(new_number))
        return new_place

    def _get_cell_left(self, place):
        place_symbol = place[0]
        new_symbol = chr(ord(place_symbol) - 1)
        new_place = place.replace(place_symbol, new_symbol)
        return new_place

    def _get_cell_right(self, place):
        place_symbol = place[0]
        new_symbol = chr(ord(place_symbol) + 1)
        new_place = place.replace(place_symbol, new_symbol)
        return new_place

    def get_takes(self):
        takes = [] # Пустой список для варантов атаки пешки
        place_symbol = self.place[0] # Символьная координата пешки (Е2)
        place_number = int(self.place[-1]) # Цифреная координата пешки
        if self.color == "white": # Условия атаки для белых пешек
            new_number = place_number + 1 if place_number < 8 else place_number # Вариант атаки если пешка не вверху поля
            if place_symbol != "A": # Условия атаки пешки если она не вправом краю доски
                left_symbol = chr(ord(place_symbol) - 1) # Символьная координата, атака влево
                left_place = self.place.replace(place_symbol, left_symbol) # Координата для атаки влево (Е замена на D)
                new_place = left_place.replace(str(place_number), str(new_number)) # Координата для атаки влево (2 замена на 3)
                takes.append(new_place) # Итог Е2 заменили на D3
            if place_symbol != "H": # Условия атаки пешки если она не влевом краю доски
                right_symbol = chr(ord(place_symbol) + 1) # Символьная координата, атака вправо
                right_place = self.place.replace(place_symbol, right_symbol) # Координата для атаки влево (Е замена на F)
                new_place = right_place.replace(str(place_number), str(new_number)) # Координата для атаки влево (2 замена на 3)
                takes.append(new_place) # Итог Е2 заменили на F3


        return takes

    def new_target(self):
        return "A1"


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


pawn = Pawn('white', 'E2')
print(pawn)
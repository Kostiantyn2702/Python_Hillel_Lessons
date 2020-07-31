# тернарный оператор
x = -10
if x >= 0:
    value_sign = "+"
else:
    value_sign = "-"
value_sign = "+" if x >= 0 else "-"
print(value_sign)

# приведение к типу bool
value = -10
print(bool(value))

value = -0.0000000001
print(bool(value))

value = "False"
print(bool(value))

value = "False"
print(bool(value))

value = 'sjgvjaszvzj'
if value:
  print("Good!")
else:
  print("Bad!")

if (12 % 2) or "some":
  print("Good!")
else:
  print("Bad!")


# Строки в Python
my_str_1 = "qwerty"
my_str_2 = "123"

print(my_str_1 + my_str_2 * 2)
# len() - длина строки (количество объектов)
print(len(my_str_1))

name = "Vova"
age = 40.123456789

print("Меня зовут " + name + ". Мне " + str(age) + " лет.")

print(f"Меня зовут {name}. Мне {age:.2f} лет.")

print("Меня зовут {}. Мне {} лет.".format(name, age))


# Оператор принадлежности in

symbol = input("Введите букву англ алфавита")
if symbol in "eyuioa":
    print("Это гласная")
else:
    print("Это согласная")


# Цикл for
# str - итерируемый объект
my_long_string = "0123456789"
for symbol in my_long_string:
    if symbol in "eyuioa":
        print(symbol)
print("-----------------------")
print(symbol)

print(my_long_string[0], my_long_string[-3])
my_long_string = my_long_string[4:8]
my_long_string = my_long_string[::-1]   # разворот строки
print(my_long_string)

# Методы строк
my_str = "abc012abcABC"
my_str = my_str.upper()
print(my_str)
my_str = my_str.lower()
print(my_str)
my_str = my_str.capitalize()
print(my_str)
position = my_str.index("ad")
print(position)

name = input("Введи имя")
if name.lower() == "иван":
    print("!!!")
else:
    print("???")
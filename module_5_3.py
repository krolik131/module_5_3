
class House: #Создаём класс House
    def __init__(self, name, number_of_floors): #Метод инициализации с названием ЖК и количеством этажей
        self.name = name #Создаём атрибут название
        self.number_of_floors = number_of_floors #Создаём атрибут количество этажей

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other,int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    def __add__(self, value):
        if isinstance(value, House):
            return self.number_of_floors +value.number_of_floors
        elif isinstance(value, int):
            return self.number_of_floors +value

    def __radd__(self, value):
        if isinstance(value, House):
            return self.number_of_floors + value.number_of_floors
        elif isinstance(value, int):
            return self.number_of_floors + value

    def __iadd__(self, value):
        if isinstance(value, House):
            return self.number_of_floors + value.number_of_floors
        elif isinstance(value, int):
            return self.number_of_floors + value


    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

# Создание объектов класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

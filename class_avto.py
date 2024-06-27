class Cars:
    def __init__(self, model='', year=0, manufacturer=" ", engine_capacity="", color="", way=0, price=0):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__way = way
        self.__price = price

    def display_info(self):
        print(f" Название модели: {self.__model}")
        print(f" Год выпуска: {self.__year}")
        print(f" Производитель: {self.__manufacturer}")
        print(f" Объем двигателя: {self.__engine_capacity}")
        print(f" Цвет автомобиля: {self.__color}")
        print(f" Пробег: {self.__way}")
        print(f" Цена: {self.__price}")


cars = Cars("Toyota Roomy", 2018, "Toyota Motor", "1.0 литра", 'Red',74000, 1290000)
cars.display_info()
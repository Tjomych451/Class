class Stadium:
    def __init__(self, название, дата, страна, город, вместимость):
        self.название = название
        self.дата = дата
        self.страна = страна
        self.город = город
        self.вместимость = вместимость

    def inf_input(self):
        self.название = input("Введи название: ")
        self.дата = input("Введи дату открытия: ")
        self.страна = input("Введи страну: ")
        self.город = input("Введи город: ")
        self.вместимость = int(input("Введи вместимость: "))

    def inf_output(self):
        print("Стадион".center(35, "-"))
        print(f"Название стадиона: {self.название}")
        print(f"Дата выпуска: {self.дата}")
        print(f"Страна: {self.страна}")
        print(f" Город: {self.город}")
        print(f" Вместимость: {self.вместимость}")

    def output_название(self):
        print(f"Название стадиона: {self.название}")

    def output_дата(self):
        print(f"Дата выпуска: {self.дата}")

    def output_страна(self):
        print(f"Страна: {self.страна}")

    def output_город(self):
        print(f"Город: {self.город}")

    def output_вместимость(self):
        print(f"Вместимость: {self.вместимость}")


stadium = Stadium("ФИШТ", "07,02,2014", "Россия", "Сочи", 45994)
rez = {
    1: stadium.inf_input,
    2: stadium.output_вместимость,
    3: stadium.output_название,
    4: stadium.output_дата,
    5: stadium.output_страна,
    6: stadium.output_город,
    7: stadium.inf_output,

}

while True:

    try:
        print(
            "1. Добавить стадион\n"
            "2. Показать вместимость\n"
            "3. Показать название\n"
            "4. Показать дату выпуска\n"
            "5. Показать страну\n"
            "6. Показать город\n"
            "7. Показать всю информацию\n"
            "8. Выход"
        )
        choice = int(input("Выберите номер из списка: "))
        if 0 < choice < 8:
            rez[choice]()
        elif choice == 8:
            break

        else:
            print("ERROR!!!  Диапазон от 1 до  8!!!!!! ")

    except ValueError:
        print("ERROR!!!! Введи цифру")
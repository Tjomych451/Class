

class Books:
    def __init__(self, название, год, издатель, жанр, автор, цена):
        self.название = название
        self.год = год
        self.издатель = издатель
        self.жанр = жанр
        self.автор = автор
        self.цена = цена

    def data_input(self):
        self.название = input("Введите название книги: ")
        self.год = int(input("Введите год: "))
        self.издатель = input("Введи издателя: ")
        self.жанр = input("Введи жанр: ")
        self.автор = input("Введи автора: ")
        self.цена = float(input("Введи цену: "))

    def data_output(self):
        print("Описание книги".center(35, "-"))
        print(f"Название книги: {self.название}")
        print(f"Год выпуска: {self.год}")
        print(f"Издатель: {self.издатель}")
        print(f"Жанр: {self.жанр}")
        print(f"Автор: {self.автор}")
        print(f"Цена: {self.цена}")

    def output_название(self):
        print(f"Название книги: {self.название}")

    def output_год(self):
        print(f"Год выпуска: {self.год}".center)

    def output_издатель(self):
        print(f"Издатель: {self.издатель}")

    def output_жанр(self):
        print(f"Жанр: {self.жанр}")

    def output_автор(self):
        print(f"Автор: {self.автор}")

    def output_цена(self):
        print(f"Цена: {self.цена}")

    def output_ALL(self):
        print(f"Цена: {self.название,self.год,self.издатель, self.жанр, self.цена,self.автор}".center(35, "-"))


book = Books("Мастер и Маргарита", 1967, "Дрофа", "Роман", "Булгаков", 528)
menu = {
    1: book.data_input,
    2: book.data_output,
    3: book.output_название,
    4: book.output_год,
    5: book.output_издатель,
    6: book.output_жанр,
    7: book.output_автор,
    8: book.output_автор,
    9: book.output_ALL
}

while True:
    try:
        print(
            "1. Добавь книгу\n"
            "2. Показать описание \n"
            "3. Показать название \n"
            "4. Показать год выпуска \n"
            "5. Показать издательство \n"
            "6. Показать жанр \n"
            "7. Показать автора \n"
            "8. Показать цену \n"
            "9. Вывести все\n"
            "10. Выход"
        )
        choice = int(input("Выберите номер пункта: "))
        if 0 < choice < 10:
            menu[choice]()
        elif choice == 10:
            break
        else:
            print("Ошибка! Диапазон от 1 до 10")
    except ValueError:
        print("Ошибка! Введите цифру")
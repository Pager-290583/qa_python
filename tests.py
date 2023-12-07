from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # №1 Добавление новой книги в словарь без указания жанра
    def test_add_new_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление новой книги
        collector.add_new_book('Гарри Поттер')
        assert len(collector.get_books_genre()) == 1


    # №2 проверка добавление книги в фавориты
    def test_add_book_in_favorites(self):
        favorites = BooksCollector()
        name = "Гарри Поттер"

        favorites.add_book_in_favorites(name)
        assert favorites.get_books_genre() != None


    # №3 Проверка у добавленной книги есть жанр
    def test_add_new_book_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    # №4 Проверка у добавленной книги нет жанра
    def test_add_new_book_not_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер","")
        assert collector.get_book_genre("Гарри Поттер") == ""
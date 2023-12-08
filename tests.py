import pytest

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

    # №1 Проверка: Добавление новой книги в словарь без указания жанра
    def test_add_new_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавление новой книги
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.books_genre.keys()
        assert len(collector.get_books_genre()) == 1

    # №2 Проверка: Добавление книги в фавориты
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        name = "Гарри Поттер"

        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites(name)
        assert name in collector.favorites
        assert len(collector.favorites) == 1

    # №3 Проверка: Удаление жанра у книги
    def test_delete_book_in_favorites(self):
        favorites = BooksCollector()
        name = "Гарри Поттер"

        favorites.add_new_book(name)
        favorites.add_book_in_favorites(name)
        favorites.delete_book_from_favorites(name)

        assert favorites.get_books_genre() is not None

    # №4 Проверка: У добавленной книги есть жанр
    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    # №5 Проверка: У добавленной книги нет жанра
    def test_add_new_book_not_set_book_genre(self):
        collector = BooksCollector()

        name = "Гарри Поттер"
        collector.add_new_book(name)
        collector.set_book_genre(name, "")
        # print(collector.books_genre)
        assert collector.get_book_genre("Гарри Поттер") == ""

    # №6 Проверка: Наличие книги в списке Жанров
    def test_add_new_book_set_book_genre_validation_book_in_age_rating(self):
        collector = BooksCollector()

        name = "Гарри Поттер"
        genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.add_new_book(name)
        collector.set_book_genre(name, "Ужасы")
        # print(collector.books_genre)
        assert collector.get_book_genre(name) in genre



    # №7 Проверка:

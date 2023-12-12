import pytest

from main import BooksCollector


class TestBooksCollector:

    # №1 Проверка: Добавление 2-х книг в список
    def test_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # №2 Проверка: Добавление новой книги в словарь без указания жанра
    def test_add_new_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.books_genre.keys()
        assert len(collector.get_books_genre()) == 1

    # №3 Проверка: Добавление книги в фавориты
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        name = "Гарри Поттер"

        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites(name)
        assert name in collector.favorites
        assert len(collector.favorites) == 1

    # №4 Проверка: Удаление книги из фавориты
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        name = "Гарри Поттер"

        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites(name)

        assert name in collector.favorites
        assert len(collector.favorites) == 1

        collector.delete_book_from_favorites(name)
        assert len(collector.favorites) == 0


    # №5 Проверка: Удаление жанра у книги
    def test_delete_book_in_favorites(self):
        collector = BooksCollector()
        name = "Гарри Поттер"

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert collector.get_books_genre() is not None

    # №6 Проверка: У добавленной книги есть жанр
    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    # №7 Проверка: У добавленной книги нет жанра
    def test_add_new_book_not_set_book_genre(self):
        collector = BooksCollector()

        name = "Гарри Поттер"
        collector.add_new_book(name)
        collector.set_book_genre(name, "")
        assert collector.get_book_genre("Гарри Поттер") == ""

    # №8 Проверка: Наличие книги в списке Жанров
    def test_add_new_book_set_book_genre_validation_book_in_age_rating(self):
        collector = BooksCollector()

        name = "Гарри Поттер"
        genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.add_new_book(name)
        collector.set_book_genre(name, "Ужасы")
        assert collector.get_book_genre(name) in genre

    # №9 Проверка параметризации: Добавили список книг и добавили книги в Фавориты
    @pytest.mark.parametrize('name', ['Гарри Поттер', 'Винни Пух', 'Аленький цветочек', 'Золушка'])
    def test_add_new_books_add_books_in_favorites(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        assert len(collector.get_list_of_favorites_books()) == 1
        assert name in collector.favorites


    # 10 Проверка: Наличие списка книг в избраном
    @pytest.mark.parametrize('name', ['Гарри Поттер', 'Винни Пух', 'Аленький цветочек', 'Золушка'])
    def test_get_list_of_favotites_books(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

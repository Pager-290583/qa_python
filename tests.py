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
        assert collector.get_book_genre('Гарри Поттер') == ''
        assert len(collector.get_books_genre()) == 1

    # №3 Проверка: Добавление книги в фавориты
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        name = "Гарри Поттер"

        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

    # №4 Проверка: Удаление книги из фавориты
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        name = "Гарри Поттер"

        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites(name)

        collector.delete_book_from_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 0



    # №5 Проверка: Устанавливаем жанр
    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    # №6 Проверка: У добавленной книги нет жанра
    def test_add_new_book_not_set_book_genre(self):
        collector = BooksCollector()

        name = "Гарри Поттер"
        collector.add_new_book(name)
        collector.set_book_genre(name, "")
        assert collector.get_book_genre("Гарри Поттер") == ""

    # №7 Проверка: Наличие книги в списке Жанров
    def test_add_new_book_set_book_genre_validation_book_in_age_rating(self):
        collector = BooksCollector()

        name = "Гарри Поттер"
        genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.add_new_book(name)
        collector.set_book_genre(name, "Ужасы")
        assert collector.get_book_genre(name) in genre

    # №8 Проверка: Добавили список книг и добавили книги в Фавориты
    @pytest.mark.parametrize('name', ['Гарри Поттер', 'Винни Пух', 'Аленький цветочек', 'Золушка'])
    def test_add_new_books_add_books_in_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1
        assert name in collector.get_list_of_favorites_books()

    # №9 Проверка: возвращаем книги, подходящие детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert name in collector.get_books_for_children()

    # №10 Проверка: выводим список книг с определённым жанром
    def test_get_books_for_children_not_list(self):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')
        assert name not in collector.get_books_for_children()

    # №11 Негативный тест: выводим список книг с определённым жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        name_2 = 'Гаррик'
        collector.add_new_book(name)
        collector.add_new_book(name_2)
        collector.set_book_genre(name, 'Ужасы')
        collector.set_book_genre(name_2, 'Фантастика')
        assert name in collector.get_books_with_specific_genre('Ужасы')
        assert name_2 not in collector.get_books_with_specific_genre('Ужасы')

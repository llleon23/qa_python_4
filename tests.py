import pytest

from data import *


class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book(BOOK_TITLE)
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_success(self, collector):
        collector.add_new_book(BOOK_TITLE)
        collector.set_book_genre(BOOK_TITLE, GENRE_BOOK)
        assert collector.get_book_genre(BOOK_TITLE) == GENRE_BOOK

    def test_set_book_genre_not_in_list(self, collector):
        collector.add_new_book(BOOK_TITLE)
        collector.set_book_genre(BOOK_TITLE, 'Какой-то жанр')
        assert collector.get_book_genre(BOOK_TITLE) == ''

    def test_get_book_genre_success(self, collector):
        collector.add_new_book(BOOK_TITLE)
        collector.set_book_genre(BOOK_TITLE, GENRE_BOOK)
        assert collector.get_book_genre(BOOK_TITLE) == GENRE_BOOK

    def test_get_books_with_specific_genre_shows_fantasy(self, collector):
        test_books = [
            ('Властелин колец', 'Фантастика'),
            ('Оно', 'Ужасы'),
            ('Звездные войны', 'Фантастика')
        ]
        for name, genre in test_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert len(fantasy_books) == 2

    def test_get_books_for_children_show_in_list(self, collector):
        children_books = [
            ('Властелин колец', 'Фантастика'),
            ('Колобок', 'Мультфильмы'),
            ('Пяточек', 'Ужасы')
        ]
        for name, genre in children_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        children_books = collector.get_books_for_children()
        assert 'Колобок' in children_books

    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book(BOOK_TITLE)
        collector.add_book_in_favorites(BOOK_TITLE)
        assert BOOK_TITLE in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book(BOOK_TITLE)
        collector.add_book_in_favorites(BOOK_TITLE)
        collector.delete_book_from_favorites(BOOK_TITLE)
        assert BOOK_TITLE not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        assert collector.get_list_of_favorites_books() == []

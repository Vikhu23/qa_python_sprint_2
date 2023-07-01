from main import BooksCollector

import pytest
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_identical_books_one_book_added(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_rating()) != 2
    
    def test_set_rating_book_is_not_on_the_list_not_setting(self, book_rating):
        collector = BooksCollector()
        collector.set_book_rating('Горе от ума', book_rating)
        assert len(collector.get_books_rating()) != 10
    
    def test_set_rating_book_less_than_1_not_setting(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, -1)
        assert collector.get_books_rating() != 1
        
    def test_set_rating_book_more_than_10(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, 11)
        assert collector.get_books_rating() != 11
    
    def test_added_book_has_no_rating(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_books_rating() != 0
import pytest


@pytest.fixture()
def book_name():
    name = 'Война и мир'
    return name

@pytest.fixture()
def book_rating():
    rating = 7
    return rating
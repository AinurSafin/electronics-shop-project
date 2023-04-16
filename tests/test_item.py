"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import pathlib

from src.item import Item
from src.errors import InstantiateCSVError
from pathlib import Path

dir_path = pathlib.Path.cwd()

@pytest.fixture
def test_data():
    return Item("Смартфон", 10000, 20)


def test_item_init(test_data):
    assert type(test_data.name) == str
    assert type(test_data.price) == int
    assert type(test_data.quantity) == int
    assert type(test_data.all) == list

    assert test_data.name == "Смартфон"
    assert test_data.price == 10000
    assert test_data.quantity == 20


def test_calculate_total_price(test_data):
    assert test_data.calculate_total_price() == test_data.price * test_data.quantity


def test_apply_discount(test_data):
    test_data.apply_discount()
    assert test_data.price == 10000


def test_name(test_data):
    item = test_data
    item.name = "Смартфон"
    assert item.name == "Смартфон"
    item.name = "Смартфон-Redme"
    assert item.name == "Смартфон"


def test_string_to_number():
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('7.0') == 7
    assert Item.string_to_number('8.7') == 8


def test_str(test_data):
    assert str(test_data) == "Смартфон"


def test_repr(test_data):
    assert repr(test_data) == "Item('Смартфон', 10000, 20)"


def test_FileNotFoundError_errors():
    file = ''
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(file)


def test_InstantiateCSVError_errors():
    path_incorrect_file = Path(dir_path, 'incorrect_item.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path_incorrect_file)
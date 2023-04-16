import csv

import items

from src.errors import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        res = str(self.__class__).split('.')[-1][:-2]
        return f"{res}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        res = f"{self.name}"
        return res

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("ERROR: class Item + other type not implemented")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """

        try:
            with open(file_name) as file:
                res = csv.DictReader(file)
                for i in res:
                    if list(i.keys()) == ['name', 'price', 'quantity']:
                        cls(i['name'], i['price'], i['quantity'])
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(value):
        """
        Cтатический-метод, возвращающий число из числа-строки
        """

        return int(float(value))
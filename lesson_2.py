"""
1. Проверить механизм наследования в Python. Для этого создать два класса.
Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену.
Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса.
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
4. Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего
(функция, отвечающая за отображение информации о товаре в одной строке).
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве
аргумента в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
6. Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
Далее реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def __str__(self):
        return f'name: {self.__name}; price: {self.__price}'

    def new_price(self, new_price):
        self.__price = new_price
        return self.__str__()


class ItemDiscountReport_1(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount
        self.price_with_discount = self.get_price() - (self.get_price() * self.discount // 100)

    def __str__(self):

        return f'name: {self.get_name()}; price: {self.price_with_discount}'

    def get_parent_data(self):
        return f'name: {self.get_name()}; price: {self.get_price()}'


    def get_info(self):
        return f'name: {self.get_name()}'


class ItemDiscountReport_2(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount
        self.price_with_discount = self.get_price() - (self.get_price() * self.discount // 100)

    def __str__(self):
        return f'name: {self.get_name()}; price: {self.price_with_discount}'

    def get_parent_data(self):
        return f'name: {self.get_name()}; price: {self.get_price()}'

    def get_info(self):
        return f'price: {self.price_with_discount}'


parent = ItemDiscount('first', 5)
inheritor = ItemDiscountReport_1('second', 10, 3)
inheritor2 = ItemDiscountReport_2('second', 10, 3)

print(parent)
print(inheritor)
print(inheritor.new_price(100))
print(inheritor.get_parent_data())
print(inheritor)
print(inheritor.get_info())
print(inheritor2.get_info())




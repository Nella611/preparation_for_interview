"""
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла,
а затем «выделение» из этого пути имени файла (без расширения).
"""

import re

def name_of_file(full_name_of_file):

    """
    предполагаем, что в названии файла или есть расширение,
    или, если его нет, то в названии нет точки
    """
    pattern = f'[^\/]+'
    matctes = re.findall(pattern, full_name_of_file)
    pattern2 = f'\.'
    answer = re.split(pattern2, matctes[-1])
    if len(answer) > 2:
        name_file = ''
        for i in range(len(answer) - 1):
            name_file += answer[i]
        return name_file
    else:
        return answer[0]


"""
2. Написать программу, которая запрашивает у пользователя ввод числа. 
На введенное число она отвечает сообщением, целое оно или дробное. 
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. 
Если они совпадают, программа должна возвращать значение True, иначе False.
"""

def what_numder():
    number = input('Введите число: ')
    pattern = f'[\.,]'
    number_list = re.split(pattern, number)
    if len(number_list) > 1:
        print('Число дробное')
        if number_list[0] == number_list[1]:
            return True
        else:
            return False
    else:
        print('Число целое')


"""
3. Создать два списка с различным количеством элементов. 
В первом должны быть записаны ключи, во втором — значения. 
Необходимо написать функцию, создающую из данных ключей и значений словарь. 
Если ключу не хватает значения, в словаре для него должно сохраняться значение None. 
Значения, которым не хватило ключей, необходимо отбросить.
"""


def lists_to_dict(list1, list2):
    new_dict = {}
    for i in range(len(list1)):
        if i >= len(list2):
            new_dict[list1[i]] = None
        else:
            new_dict[list1[i]] = list2[i]
    return new_dict


list_key = [1, 2, 3]
list_value1 = ['a', 'b', 'c', 'd']
list_value2 = ['a', 'b']
#
# print(lists_to_dict(list_key, list_value1))
# print(lists_to_dict(list_key, list_value2))


"""
4. Написать программу, в которой реализовать две функции. 
В первой должен создаваться простой текстовый файл. 
Если файл с таким именем уже существует, выводим соответствующее сообщение. 
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией. 
Для создания списков использовать генераторы. Применить к спискам функцию zip(). 
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, 
чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию. 
В нее должна передаваться ссылка на созданный файл. 
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. 
Вся программа должна запускаться по вызову первой функции.
"""


def write_file(file):
    with open(file) as f:
        for line in f:
            print(line, end='')


def create_file():
    file = input('Введите имя файла: ')
    try:
        f = open(file, 'x', encoding='UTF-8')
    except FileExistsError:
        print('Файл с таким именем уже существует!')
    else:
        size_list = int(input('Введите число для генерации числового списка: '))
        list_num = [x for x in range(size_list)]
        list_str = [f'str {x}' for x in range(size_list)]
        text_list = list(zip(list_num, list_str))
        for text in text_list:
            f.write(f'{text[0]}: {text[1]}\n')
        f.close()
        write_file(file)

# create_file()




"""
5. Усовершенствовать первую функцию из предыдущего примера. 
Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число). 
Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных). 
Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: 
вывод первого вхождения, вывод всех вхождений. 
Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок, 
состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""
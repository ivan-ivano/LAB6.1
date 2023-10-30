import random


def generate_list():
    b = []
    for k in range(22):
        b.append(random.randint(-40, 50))
    return b


def sum_of_elements(lst):
    i = 0
    sm = 0
    while i < len(lst):
        if not (lst[i] > 0 and lst[i] % 5 == 0):
            sm += lst[i]
        i += 1
    return sm


def count_elements(lst):
    i = 0
    cnt = 0
    while i < len(lst):
        if not (lst[i] > 0 and lst[i] % 5 == 0):
            cnt += 1
        i += 1
    return cnt


def replace_elements(lst):
    i = 0
    while i < len(lst):
        if not (lst[i] > 0 and lst[i] % 5 == 0):
            lst[i] = 0
        i += 1
    return lst


if __name__ == '__main__':
    a = generate_list()
    print(a)
    print('Сума елементів, які підпадають під критерії:', sum_of_elements(a))
    print('Кількість обчислених елементів:', count_elements(a))
    print(replace_elements(a))

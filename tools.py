from typing import List
from math import sqrt


def unique_numbers(value: List[int]) -> list:
    res = []
    for i in value:
        if i not in res:
            res.append(i)
    return res


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def range_list(start: int, end: int) -> list:
    result = []
    for i in range(start, end + 1):
        if is_prime(i):
            result.append(i)
    return result


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, x, y):
        return sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

    def set_cords(self, x, y):
        self.x = x
        self.y = y

    def get_cords(self):
        return self.x, self.y


def sort_by_length(strings: List[str]):
    sorted_straight = sorted(strings, key=len)
    print(sorted_straight)
    sorted_reverse = sorted(strings, key=len, reverse=True)
    print(sorted_reverse)


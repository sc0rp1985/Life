import random
import hashlib


class LifeWorld:

    def __init__(self, size, random_init):
        self.__size = size
        self.__world = self.__get_empty_world()
        if random_init:
            self.__test_random_ini()
        else:
            self.__test_init()
        self.__empty = False
        self.__generation = 0

    def __test_init(self):
        #                  0 1 2 3 4 5 6 7 8 9
        self.__world[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__world[1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__world[2] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__world[3] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__world[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__world[5] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__world[6] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__world[7] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.__world[8] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
        self.__world[9] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
        self.__empty = False

    def __test_random_ini(self):
        for row in range(self.__size):
            for col in range(self.__size):
                self.__world[row][col] = random.randint(0, 1)

    def __get_neighbor_count(self, col, row):
        count = 0
        for i in range(row - 1, row + 2):
            row_index = i if 0 <= i < self.__size else abs(abs(i) - self.__size)
            for j in range(col - 1, col + 2):
                col_index = j if 0 <= j < self.__size else abs(abs(j) - self.__size)
#                if i >= 0 and i < self.__size and j >= 0 and j < self.__size and (i != row or j != col):
#                    if self.__world[i][j] == 1:
                if row_index != row or col_index != col:
                    if self.__world[row_index][col_index] == 1:
                        count += 1
        return count

    def __get_empty_world(self):
        a = [[0] * self.__size for i in range(self.__size)]
        return a

    def __dif(self, new_world):
        for row in range(self.__size):
            a = new_world[row]
            b = self.__world[row]
            c = list(set(a).intersection(set(b)))
            if a != b:
                return True
        return False

    def next_generation(self):
        if self.__generation == 0:
            self.__generation += 1
            return not self.__empty

        self.__empty = True
        tmp = self.__get_empty_world()
        for row in range(self.__size):
            for col in range(self.__size):
                count = self.__get_neighbor_count(col, row)
                if count > 3 or count < 2:
                    tmp[row][col] = 0
                elif count == 2:
                    tmp[row][col] = self.__world[row][col]
                elif count == 3:
                    tmp[row][col] = 1
                    self.__empty = False

        self.__world = tmp
        self.__generation += 1
        return not self.__empty

    def get_world(self):
        return self.__world

    def get_generation(self):
        return self.__generation

    def get_empty(self):
        return self.__empty

    def get_hash(self):
        _str = ''.join(map(lambda x: ''.join(map(str, x)), self.__world))
        _hash = hashlib.md5(_str.encode('utf-8')).hexdigest()
        return _hash

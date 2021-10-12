import copy
import random


class SudokuGenerator:

    size = 9
    valid = set(range(1, 10))
    remove = {"easy": 15, "medium": 30, "hard": 60}
    solution = []
    possibilities = {}
    puzzle = []

    def __init__(self, difficulty="easy"):
        self.fill_grid()
        self.remove_values(difficulty)

    def fill_grid(self):
        for i in range(self.size):
            self.solution.append([0]*self.size)
        self.init_possibilities(self.possibilities)
        self.rec_fill_grid(0, 0)

    def rec_fill_grid(self, row, col):
        valid = self.possibilities[(row, col)]
        tmp_valid = valid.copy()
        n = len(tmp_valid)
        if n == 0:
            return False
        if row == self.size-1 and col == self.size-1:
            self.solution[row][col] = list(valid)[0]
            return True
        good = True
        while n > 0:
            index = 0
            if n > 1:
                index = random.randint(0, n - 1)
            item = list(tmp_valid)[index]
            self.solution[row][col] = item
            change_back = set()
            good = self.eliminate_row(row, item, self.possibilities, change_back)
            if good:
                good = self.eliminate_col(col, item, self.possibilities, change_back)
                if good:
                    good = self.eliminate_square(row, col, item, self.possibilities, change_back)
                    if good:
                        new_row = row
                        new_col = col + 1
                        if new_col == self.size:
                            new_row = row + 1
                            new_col = 0
                        good = self.rec_fill_grid(new_row, new_col)
            if good:
                return True
            else:
                self.change_back(change_back, item)
                tmp_valid.remove(item)
                n = len(tmp_valid)
        if not good:
            self.solution[row][col] = 0
            return False

    def eliminate_row(self, row, item, possibilities, change_back=None):
        good = True
        for i in range(self.size):
            valid = possibilities[(row, i)]
            if item in valid:
                valid.remove(item)
                if change_back:
                    change_back.add((row, i))
                if len(valid) < 1 and self.solution[row][i] == 0:
                    good = False
                    break
        return good

    def eliminate_col(self, col, item, possibilities, change_back=None):
        good = True
        for i in range(self.size):
            valid = possibilities[(i, col)]
            if item in valid:
                valid.remove(item)
                if change_back:
                    change_back.add((i, col))
                if len(valid) < 1 and self.solution[i][col] == 0:
                    good = False
                    break
        return good

    def eliminate_square(self, row, col, item, possibilities, change_back=None):
        good = True
        square_size = int(self.size / 3)
        row_min = int(row / square_size) * square_size
        col_min = int(col / square_size) * square_size
        for i in range(row_min, row_min + square_size):
            if i == row:
                continue
            for j in range(col_min, col_min + square_size):
                if j == col:
                    continue
                valid = possibilities[(i, j)]
                if item in valid:
                    valid.remove(item)
                    if change_back:
                        change_back.add((i, j))
                    if len(valid) < 1 and self.solution[i][j] == 0:
                        good = False
                        break
            if not good:
                break
        return good

    def change_back(self, change_back, item):
        for loc in change_back:
            self.possibilities[loc].add(item)

    def init_possibilities(self, possibilities):
        for i in range(self.size):
            for j in range(self.size):
                possibilities[(i, j)] = self.valid.copy()

    def remove_values(self, difficulty):
        to_remove = self.remove[difficulty]
        removed = 0
        self.puzzle = copy.deepcopy(self.solution)
        locations = self.init_locations()
        n = len(locations)
        while n > 0:
            index = 0
            if n > 1:
                index = random.randint(0, n - 1)
            (row, col) = list(locations)[index]
            self.puzzle[row][col] = 0
            if self.solvable():
                removed += 1
                if removed >= to_remove:
                    break
            else:
                self.puzzle[row][col] = self.solution[row][col]
            locations.remove((row, col))
            n = len(locations)

    def init_locations(self):
        locations = set()
        for i in range(self.size):
            for j in range(self.size):
                locations.add((i,j))
        return locations

    def solvable(self):
        possibilities = self.get_possibilities()
        n = len(possibilities.keys())
        while n > 0:
            good = False
            count = 0
            for row, col in possibilities:
                valid = possibilities[(row, col)]
                if len(valid) == 1:
                    item = list(valid)[0]
                    self.eliminate_row(row, item, possibilities)
                    self.eliminate_col(col, item, possibilities)
                    self.eliminate_square(row, col, item, possibilities)
                    good = True
                elif len(valid) > 1:
                    count += 1
            n = count
            if not good:
                return False
        return True

    def get_possibilities(self):
        possibilities = {}
        self.init_possibilities(possibilities)
        for row in range(self.size):
            for col in range(self.size):
                item = self.puzzle[row][col]
                if item != 0:
                    self.eliminate_row(row, item, possibilities)
                    self.eliminate_col(col, item, possibilities)
                    self.eliminate_square(row, col, item, possibilities)
        return possibilities



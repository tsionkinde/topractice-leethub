import random

class RandomizedSet:

    def __init__(self):
        self.arrays = []
        self.position = {}  

    def insert(self, val: int) -> bool:
        if val in self.position:
            return False

        self.arrays.append(val)
        self.position[val] = len(self.arrays) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.position:
            return False

        index = self.position[val]
        last_value = self.arrays[-1]

        self.arrays[index] = last_value
        self.position[last_value] = index

        self.arrays.pop()
        del self.position[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arrays)
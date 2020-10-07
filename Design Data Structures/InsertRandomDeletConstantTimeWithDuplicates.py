import collections
import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = collections.defaultdict(set)
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        flag = val in self.pos
        self.arr.append(val)
        self.pos[val].add(len(self.arr)-1)
        return not flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.pos: return False
        if val == self.arr[-1]:
            self.pos[val].remove(len(self.arr)-1)
            self.arr.pop()
        else:
            pos = self.pos[val].pop()
            self.pos[self.arr[-1]].add(pos)
            self.pos[self.arr[-1]].remove(len(self.arr)-1)
            self.arr[pos] = self.arr.pop()
        if len(self.pos[val]) < 1: self.pos.pop(val)

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.arr[random.randint(0, len(self.arr) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
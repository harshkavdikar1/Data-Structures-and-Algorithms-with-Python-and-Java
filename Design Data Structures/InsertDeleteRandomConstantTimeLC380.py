import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos: return False
        self.arr.append(val)
        self.pos[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos: return False
        self.arr[self.pos[val]] = self.arr[-1]
        self.pos[self.arr.pop()] = self.pos[val]
        self.pos.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[random.randint(0, len(self.arr) - 1)]
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
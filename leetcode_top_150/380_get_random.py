from typing import List
import random

class RandomizedSet:

    def __init__(self):
        self.numHashMap = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        res  = val not in self.numHashMap
        if res:
            self.numHashMap[val]= len(self.numList)
            self.numList.append(val)
        return res
        
    def remove(self, val: int) -> bool:
        res = val in self.numHashMap
        if res:
            index = self.numHashMap[val]
            lastValue = self.numList[-1]
            self.numList[index] = lastValue
            self.numHashMap[lastValue] = index
            # Remove the last element from the list and dictionary
            self.numList.pop()
            del self.numHashMap[val]
            return True


    def getRandom(self) -> int:
        return random.choice(self.numList)
        


def main():
    # Create an object of RandomizedSet
    randomizedSet = RandomizedSet()

    # Insert values and test the insert method
    print(randomizedSet.insert(1))  # Expected True
    print(randomizedSet.insert(1))  # Expected False (1 already inserted)
    print(randomizedSet.insert(2))  # Expected True

    # Test remove method
    print(randomizedSet.remove(1))  # Expected True (1 is removed)
    print(randomizedSet.remove(1))  # Expected False (1 is already removed)

    # Test getRandom method
    print(randomizedSet.getRandom())  # Expected 2, as it's the only element left

    # Insert more values and test getRandom with multiple elements
    print(randomizedSet.insert(3))  # Expected True
    print(randomizedSet.insert(4))  # Expected True
    print(randomizedSet.getRandom())  # Expected a random element from [2, 3, 4]

    # Test remove method again
    print(randomizedSet.remove(3))  # Expected True
    print(randomizedSet.remove(3))  # Expected False (3 already removed)

if __name__ == "__main__":
    main()
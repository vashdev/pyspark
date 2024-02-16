# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections
from itertools import groupby, accumulate

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}  # if we let LRUCache inherits collections.OrderedDict,
        # then we don't need to have a dict composition here. Better use _cache
        self.capacity=capacity
        #self.size=0  #turned out to be unnecessary, as len(cache) has the info

    def get(self, key: int) -> int:
        if key not in self.cache: # equiv. if self.cache.get(key)==None:
            return -1
        self.cache[key]=self.cache.pop(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
                del self.cache[key]  # almost equiv to self.cache.pop(key,None)
        elif len(self.cache)==self.capacity:
                self.cache.pop(next(iter(self.cache.keys()),-1))  # next(iter(dict.keys()),-1) efficient way to get 1st key
        self.cache[key]=value


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ''' Implement LRU    '''
    cache=LRUCache(3)
    cache.put(1, 1); # cache is {1 = 1}
    cache.get(1); # return 1








# See PyCharm help at https://www.jetbrains.com/help/pycharm/

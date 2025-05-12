# https://leetcode.com/problems/lru-cache/description/
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.od = OrderedDict()  # key -> value

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key, last=False)  # 맨 앞으로(가장 최신)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key, last=False)
        self.od[key] = value
        self.od.move_to_end(key, last=False)
        if len(self.od) > self.cap:           # LRU = 맨 뒤
            self.od.popitem(last=True)
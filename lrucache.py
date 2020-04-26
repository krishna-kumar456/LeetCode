from collections import OrderedDict


class LRUCache():
    def __init__(self, n):
        self.vals = OrderedDict()
        self.max_size = n

    def set(self, key, value):
        if key in self.vals:
            del self.vals[key]
            self.vals[key] = value

        else:
            if len(self.vals) < self.max_size:
                self.vals[key] = value

            else:
                del self.vals[next(iter(self.vals))]
                self.vals[key] = value

    def get(self, key):
        if key in self.vals:
            tempval = self.vals[key]
            del self.vals[key]
            self.vals[key] = tempval
            return self.vals[key]
        return None


cache = LRUCache(2)

cache.set("cookie", 10)
cache.set("milk", 20)
cache.set("cheese", 30)
cache.set("goat", 40)
a = cache.get("milk")

if a is None:
    cache.set()
print(a)

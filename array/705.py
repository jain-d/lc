# Design HashSet

class MyHashSet:
    def __init__(self):
        self.hash_set: list[int] = []

    def add(self, key: int) -> None:
        if not self.hash_set.count(key):
            self.hash_set.append(key)

    def remove(self, key: int) -> None:
        try:
            if (index := self.hash_set.index(key)) > -1:
                self.hash_set.pop(index)
        except:
            pass

    def contains(self, key: int) -> bool:
        return True if self.hash_set.count(key) else False

my_hash_set = MyHashSet()

my_hash_set.add(1)
my_hash_set.add(1000000)
my_hash_set.add(2)
print(my_hash_set.hash_set)
print(f"contains 2? {my_hash_set.contains(2)}")
my_hash_set.remove(2)
print(my_hash_set.hash_set)
print(f"contains 2? {my_hash_set.contains(2)}")

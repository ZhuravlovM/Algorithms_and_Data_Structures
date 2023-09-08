class HashMap:
    def __init__(self):
        self.hash_map = {}

    def add_entry(self, key, value):
        index = hash(key)
        self.hash_map[index] = value

    def get_value(self, key):
        index = hash(key)
        return self.hash_map.get(index, None)


map_example = HashMap()

map_example.add_entry("Ray", 92)
map_example.add_entry("Charles", 44)
map_example.add_entry("Corey", 31)

print(map_example.get_value("Ray"))
print(map_example.get_value("Corey"))
print(map_example.get_value("Mike"))

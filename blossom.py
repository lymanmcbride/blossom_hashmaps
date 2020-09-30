from linked_list import Node
class hashmap:
    def __init__(size):
        self.array_size = size
        self.array = [None for i in range(self.array_size)]

    def hash(self, key):
        sum(key.encode())
    def compress(hash_code):
        result = hash_code % self.array_size
        return result

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        self.array[array_index] = [key, value]
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        payload = self.array[array_index]
        if payload:
            if payload[0] == key:
                return payload[1]
            else:
                return None

from linked_list import Node
class hashmap:
    def __init__(size):
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)]

    def hash(self, key):
        sum(key.encode())
    def compress(hash_code):
        result = hash_code % self.array_size
        return result

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if item[0] == key:
                item[1] = value
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if item[0] == key:
                return item[1]
            else:
                return None
        

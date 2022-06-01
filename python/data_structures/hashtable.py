from data_structures.linked_list import LinkedList


class Hashtable:
    """
    set
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from the value argument given to this method.
    get
        Arguments: key
        Returns: Value associated with that key in the table
    contains
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
    keys
        Returns: Collection of keys
    hash
        Arguments: key
        Returns: Index in the collection for that key
    """

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def set(self, key, value):
        index = self.hash(key)

        bucket = self.buckets[index]

        if bucket is None:
            bucket = LinkedList()
            self.buckets[index] = bucket

        bucket.insert((key, value))

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]

            current = current.next

        return None

    def contains(self, key):
        hash_index = self.hash(key)
        bucket = self.buckets[hash_index]

        if bucket is None:
            return False
        current = bucket.head
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False

    def keys(self):
        key_collection = set()
        for bucket in self.buckets:
            if bucket is not None:
                current = bucket.head
                while current:
                    pair = current.value
                    current_key = pair[0]
                    key_collection.add(current_key)
                    current = current.next
        return key_collection

    def hash(self, key):

        sum_of_chars = 0

        for char in key:
            sum_of_chars += ord(char)

        primed = sum_of_chars * 599

        index = primed % self.size

        return index


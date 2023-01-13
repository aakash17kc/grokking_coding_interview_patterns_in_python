class Bucket:
    def __init__(self):
        self.bucket = []

    def update(self, key, value):
        if key is None or value is None:
            return -1
        found = False
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def get(self, key):
        for k, v in enumerate(self.bucket):
            if k == key:
                return v
        return -1

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]


class MyMap:
    def __init__(self, key_space):
        self.key_space = key_space
        self.map = [Bucket() for i in range(self.key_space)]

    def put(self, key, value):
        if key is None or value is None:
            return
        hash = key % self.key_space
        self.map[hash].update(key, value)

    def get(self, key):
        if key is None:
            return -1
        hash = key % self.key_space
        return self.map[hash].get(key)

    def remove(self, key):
        if key is None:
            return -1
        self.map[key % self.key_space].remove(key)

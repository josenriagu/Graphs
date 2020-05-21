'''
defining a Queue class to help in dfs
'''


class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)
        # return self to allow chaining
        return self

    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        return None

    def size(self):
        return len(self.storage)

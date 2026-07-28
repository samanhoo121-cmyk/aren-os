class MemoryManager:

    def __init__(self):
        self.memory = {}

    def save(self, key, value):
        self.memory[key] = value

    def load(self, key):
        return self.memory.get(key)

    def delete(self, key):
        if key in self.memory:
            del self.memory[key]

    def clear(self):
        self.memory.clear()


class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            result = self.stack.pop()
            return result

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def __iter__(self):
        self.current = len(self.stack) - 1
        return self

    def __next__(self):
        if self.current >= 0:
            result = self.stack[self.current]
            self.current -= 1
            return result
        else:
            raise StopIteration

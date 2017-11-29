class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def is_empty(self):
        return not self.size()


if __name__ == '__main__':
    s = Stack()

    print('is_empty?:', s.is_empty())
    print('Size:', s.size())

    for i in range(10):
        s.push(i)

    print('is_empty?:', s.is_empty())
    print('Size:', s.size())

    for i in range(3):
        print('pop:', s.pop())

    print('is_empty?:', s.is_empty())
    print('Size:', s.size())
from node import Node

class LinkedList():
    def __init__(self):
        self._root = None
        self._last = None
        self._size = 0

    # TODO
    # add_after
    # add_before
    # add_at_the_end
    # add_at_the_beginning

    def add(self, data):
        new_node = Node(data)

        if self._size == 0:
            self._root = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node

        self._size += 1


    def find(self, data):
        node = self._root

        for i in range(self._size):
            if node.data == data:
                return node
            else:
                node = node.next

        return None

    # TODO
    # remove_node?

    def remove(self, data):
        node = self._root
        while node.next:
            if node.next.data == data:
                node.next = node.next.next if node.next.next else None # ekhm.
                self._size -= 1
            node = node.next


    def __repr__(self):
        node = self._root
        out = '({} items): {}'.format(self._size, node.data)
        while node.next:
            node = node.next
            out += ' -> {}'.format(node.data)
        return out

    def __len__(self):
        return self._size


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add(10)
    linked_list.add(20)
    linked_list.add(30)
    print(linked_list)

    node = linked_list.find(20)
    print('Data: {}, Next: {}'.format(node.data, node.next))

    linked_list.remove(20)
    print(linked_list)
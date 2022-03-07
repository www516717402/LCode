
class Node:
    def __init__(self, data=None, pre_node=None, next_node=None) -> None:
        self._data = data
        self._pre_node = pre_node
        self._next_node = next_node

    def set_data(self, data):
        self.data = data

    def set_node(self, pre_node=None, next_node=None):
        if pre_node is not None:
            self._pre_node = pre_node
        if next_node is not None:
            self._next_node = next_node

    def __repr__(self) -> str:
        return self._data


class SingleLinkedList():
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def add(self):
        pass

    def remove(self):
        pass

    def insert(self):
        pass

    def show(self):
        pass


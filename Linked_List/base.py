
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

    def _unlink(self):
        pre_node = self._pre_node
        next_node = self._next_node

        pre_node._next_node = next_node
        if next_node is not None:
            next_node._pre_node = pre_node

    def __repr__(self) -> str:
        return self._data


class DoubleLinkedList():
    def __init__(self, iter_data=None) -> None:
        self.root = Node()
        self.length = 0
        if iter_data is not None:
            self.add_iter(iter_data)
 
    def __len__(self):
        return self.length
    
    def add(self, data, tail=True):
        start = self.root
        orient, oppsite = '_next_node', '_pre_node'
        if not tail:
            orient, oppsite = oppsite, orient
        while getattr(start, orient):
            start = getattr(start, orient)
        self._add_node(start, data)
        self.length += 1

    def add_iter(self, iter_data, tail=True):
        for data in iter_data:
            self.add(data, tail)
    
    # only support insert by tail
    def _add_node(self, node, data):
        new_node = Node(data=data, pre_node=node)
        if node._next_node is not None:
            node._next_node._pre_node = new_node
            new_node._next_node = node._next_node
        node._next_node = new_node
    
    def remove(self, data=None, item=None):
        if data is not None:
            self._remove_data(data)
        elif item is not None:
            self._remove_item(item)
        else:
            pass

    def _remove_data(self, data):
        start = self.root
        orient = '_next_node'
        while getattr(start, orient):
            if start._data == data:
                self._remove_node(start)
                self.length -= 1
                break
            start = getattr(start, orient)
    
    def _remove_item(self, item):
        if not (item >= 0 and item < self.length):
            return
        start = self.root
        orient = '_next_node'
        cur_item = 0
        for cur_item in range(self.length + 1):
            if cur_item == item + 1:
                self._remove_node(start)
                self.length -= 1
                break
            start = getattr(start, orient)

    def _remove_node(self, node):
        node._unlink()
        del node
    
    def insert(self, item, data):
        if not (item >= 0 and item <= self.length):
            return
        start = self.root
        orient = '_next_node'
        for cur_item in range(self.length+1):
            if cur_item == item:
                self._add_node(start, data)
                self.length += 1
                break
            start = getattr(start, orient)

    def show(self, tail=True):
        start = self.root
        orient, oppsite = '_next_node', '_pre_node'
        if not tail:
            orient, oppsite = oppsite, orient
        while getattr(start, orient):
            start = getattr(start, orient)
            print(f'\ndata --> {start._data}')


class CircleDoubleLinkedList():
    def __init__(self, iter_data=None) -> None:
        self.root = Node()
        self.root.set_node(self.root, self.root)
        self.length = 0
        if iter_data is not None:
            self.add_iter(iter_data)
 
    def __len__(self):
        return self.length
    
    def add(self, data, tail=True):
        # todo 未完成！！此方法比较复杂，实用性较差
        # orient, oppsite = '_next_node', '_pre_node'
        # if not tail:
        #     orient, oppsite = oppsite, orient
        # tmp_node = getattr(self.root, orient)
        # new_node = Node(data, **{orient:self.root, oppsite:tmp_node})
        # setattr(getattr(self.root, orient), oppsite, new_node)
        # tmp_node = getattr(getattr(self.root, orient), oppsite)
        if tail:
            self.root._next_node = self.root._next_node._pre_node = Node(data, self.root, self.root._next_node)
        else:
            self.root._pre_node = self.root._pre_node._next_node = Node(data, self.root._pre_node, self.root)
        self.length += 1

    def add_iter(self, iter_data, tail=True):
        for data in iter_data:
            self.add(data, tail)
    
    # only support insert by tail
    def _add_node(self, node, data):
        new_node = Node(data=data, pre_node=node)
        if node._next_node is not None:
            node._next_node._pre_node = new_node
            new_node._next_node = node._next_node
        node._next_node = new_node
    
    def remove(self, data=None, item=None):
        if data is not None:
            self._remove_data(data)
        elif item is not None:
            self._remove_item(item)
        else:
            pass

    def _remove_data(self, data):
        start = self.root
        orient = '_next_node'
        while getattr(start, orient):
            if start._data == data:
                self._remove_node(start)
                self.length -= 1
                break
            start = getattr(start, orient)
    
    def _remove_item(self, item):
        if not (item >= 0 and item < self.length):
            return
        start = self.root
        orient = '_next_node'
        cur_item = 0
        for cur_item in range(self.length + 1):
            if cur_item == item + 1:
                self._remove_node(start)
                self.length -= 1
                break
            start = getattr(start, orient)

    def _remove_node(self, node):
        node._unlink()
        del node
    
    def insert(self, item, data):
        if not (item >= 0 and item <= self.length):
            return
        start = self.root
        orient = '_next_node'
        for cur_item in range(self.length+1):
            if cur_item == item:
                self._add_node(start, data)
                self.length += 1
                break
            start = getattr(start, orient)

    def show(self, tail=True):
        start = self.root
        orient, oppsite = '_next_node', '_pre_node'
        if not tail:
            orient, oppsite = oppsite, orient
        while getattr(start, orient) != self.root:
            start = getattr(start, orient)
            print(f'\ndata --> {start._data}')

if __name__ == '__main__':
    link = CircleDoubleLinkedList()
    link.add_iter([0,2,3,10,1], tail=False)
    #link.remove(data=10)
    link.show(tail=False)
    
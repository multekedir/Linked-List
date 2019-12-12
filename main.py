class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = Node()

    def __len__(self):
        cur = self.head
        num = 0
        # count until last
        while cur.next is not None:
            num += 1
            cur = cur.next
        return num

    def __str__(self):
        elem = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            elem.append(cur.data)
        return str(elem)

    def append(self, data):
        # create a new node
        new_node = Node(data)
        # set current node
        cur = self.head
        # find last node
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def to_list(self):
        elem = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            elem.append(cur.data)
        return elem

    def check_out_of_range(self, index):
        if index >= len(self):
            raise IndexError('Index out of bounds')

    def get(self, index):
        try:
            self.check_out_of_range(index)
        except IndexError:
            print('ERROR')
        else:
            cur_index = 0
            cur_node = self.head
            while True:
                cur_node = cur_node.next
                if cur_index == index:
                    return cur_node.data
                cur_index += 1

    def remove(self, index):
        try:
            self.check_out_of_range(index)
        except IndexError:
            print('ERROR')
        else:
            cur_index = 0
            cur_node = self.head
            while True:
                per_node = cur_node
                cur_node = cur_node.next
                if cur_index == index:
                    per_node.next = cur_node.next
                    return True
                cur_index += 1


if __name__ == "__main__":
    l_l = LinkedList()
    for i in range(10):
        l_l.append(i)

    l_l.display()

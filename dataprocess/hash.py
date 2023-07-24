import random
class Node:
    def __init__(self, key, val, prev=None, succ=None):
        self.key = key
        self.val = val
        # 前驱
        self.prev = prev
        # 后继
        self.succ = succ

    def __repr__(self):
        return str(self.val)
    def get_val(self):
        return self.val
    def get_key(self):
        return self.key


class LinkedList:
    def __init__(self):
        self.head = Node(None, 'header')
        self.tail = Node(None, 'tail')
        self.head.succ = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
        # 将node节点添加在链表尾部
        prev = self.tail.prev
        node.prev = prev
        node.succ = prev.succ
        prev.succ = node
        node.succ.prev = node
        self.size += 1

    def delete(self, node):
        # 删除节点
        prev = node.prev
        succ = node.succ
        succ.prev, prev.succ = prev, succ
        self.size -= 1

    def get_list(self):
        # 返回一个包含所有节点的list，方便上游遍历
        ret = []
        cur = self.head.succ
        while cur != self.tail:
            ret.append(cur)
            cur = cur.succ
        return ret

    def get_by_key(self, key):
        cur = self.head.succ
        while cur != self.tail:
            if cur.key == key:
                return cur
            cur = cur.succ
        return None


class HashMap:
    def __init__(self, capacity=16, load_factor=5):
        self.capacity = capacity
        self.load_factor = load_factor
        self.headers = [LinkedList() for _ in range(capacity)]

    def get_hash_key(self, key):
        return hash(key) & (self.capacity - 1)

    def put(self, key, val):
        hash_key = self.get_hash_key(key)
        linked_list = self.headers[hash_key]
        if linked_list.size >= self.load_factor * self.capacity:
            self.reset()
            hash_key = self.get_hash_key(key)
            linked_list = self.headers[hash_key]
        node = linked_list.get_by_key(key)
        if node is not None:
            node.val = val
        else:
            node = Node(key, val)
            linked_list.append(node)

    def get(self, key):
        hash_key = self.get_hash_key(key)
        linked_list = self.headers[hash_key]
        node = linked_list.get_by_key(key)
        return node.val if node is not None else None

    def getnode(self, key):
        hash_key = self.get_hash_key(key)
        linked_list = self.headers[hash_key]
        node = linked_list.get_by_key(key)
        return node if node is not None else None

    def delete(self, key):
        node = self.getnode(key)
        if node is None:
            return False
        hash_key = self.get_hash_key(key)
        linked_list = self.headers[hash_key]
        linked_list.delete(node)
        return True

    def reset(self):
        headers = [LinkedList() for _ in range(self.capacity * 2)]
        cap = self.capacity
        self.capacity = self.capacity * 2
        for i in range(cap):
            linked_list = self.headers[i]
            nodes = linked_list.get_list()
            for u in nodes:
                hash_key = self.get_hash_key(u.key)
                head = headers[hash_key]
                head.append(u)
        self.headers = headers




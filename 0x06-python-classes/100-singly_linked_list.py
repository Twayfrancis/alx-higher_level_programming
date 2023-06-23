#!/usr/bin/python3
"""Define singly linked list classes"""


class Node:
    """node in singly linked list"""

    def __init__(self, data, next_node=None):
        """new node initilization

        Args: 
            data (init): data of new Node.
            next_node (Node): next node of the new Node
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """ set data of the node"""
            return (self.__data)

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            return (self.__next_node)

        @next_node.setter
        def next_node(self, value):

            if value is None or isinstance(value, Node):
                self.__next_node = value
            else:
                raise TypeError("next_node must be None or a Node object")

class SinglyLinkedList:
    """ a singly linked list"""

    def __init__(self):
        """ new singly linked list initialization"""
        self.head = None

    def __str__(self):
        if self.head is None:
            return ""
        else:
            return '\n'.join(str(node.data) for node in self)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node


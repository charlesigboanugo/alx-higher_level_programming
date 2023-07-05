#!/usr/bin/python3
""" Defines a singly linked list and a node """


class Node:
    """ A Node class """
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ returns the data stored in node """
        return self.__data

    @data.setter
    def data(self, value):
        """ set node data to value"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ returns the next_node object"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ stores the next_node object """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ A singly linked list class """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new node into the sorted linked list """
        temp = self.__head
        if temp is None:
            self.__head = Node(value)
            return
        if temp.data < value:
            while temp.next_node is not None and \
             temp.next_node.data < value:
                temp = temp.next_node
            temp.next_node = Node(value, temp.next_node)
        else:
            self.__head = Node(value, temp)

    def __str__(self):
        temp = self.__head
        string = ""
        while temp is not None:
            string = "{}\n{}".format(string, temp.data)
            temp = temp.next_node
        return string[1:]

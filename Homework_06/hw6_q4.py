from DoublyLinkedList import *


def copy_linked_list(lnk_lst: DoublyLinkedList):
    cursor = lnk_lst.header.next
    duplicate = DoublyLinkedList()
    while cursor.data is not None:
        duplicate.add_last(cursor.data)
        cursor = cursor.next
    return duplicate


def deep_copy_linked_list(lnk_lst: DoublyLinkedList):
    cursor = lnk_lst.header.next
    duplicate = DoublyLinkedList()
    while cursor.data is not None:
        if isinstance(cursor.data, DoublyLinkedList):
            duplicate.add_last(deep_copy_linked_list(cursor.data))
        else:
            duplicate.add_last(cursor.data)
        cursor = cursor.next
    return duplicate


def main():
    lnk_lst1 = DoublyLinkedList()
    elem1 = DoublyLinkedList()
    elem1.add_last(1)
    elem1.add_last(2)
    lnk_lst1.add_last(elem1)
    elem2 = 3
    lnk_lst1.add_last(elem2)
    lnk_lst2 = deep_copy_linked_list(lnk_lst1)
    e1 = lnk_lst1.header.next
    e1_1 = e1.data.header.next
    e1_1.data = 10
    e2 = lnk_lst2.header.next
    e2_1 = e2.data.header.next
    print(e2_1.data)
    
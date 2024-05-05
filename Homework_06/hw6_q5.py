from DoublyLinkedList import *


def merge_linked_lists(srt_lnk_lst1: DoublyLinkedList, srt_lnk_lst2: DoublyLinkedList):
    res = DoublyLinkedList()

    def merge_sublists(cursor1: DoublyLinkedList.Node, cursor2: DoublyLinkedList.Node):
        if cursor2.data is None:
            res.add_last(cursor1.data)
            cursor1 = cursor1.next
        elif cursor1.data is None:
            res.add_last(cursor2.data)
            cursor2 = cursor2.next
        elif cursor1.data <= cursor2.data:
            res.add_last(cursor1.data)
            cursor1 = cursor1.next
        else:
            res.add_last(cursor2.data)
            cursor2 = cursor2.next
        if (cursor1.data is not None) | (cursor2.data is not None):
            merge_sublists(cursor1, cursor2)
        return res
    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next)


def main():
    srt_lnk_lst1 = DoublyLinkedList()
    for i in [1, 3, 5, 6, 8]:
        srt_lnk_lst1.add_last(i)
    srt_lnk_lst2 = DoublyLinkedList()
    for i in [2, 3, 5, 10, 15, 18]:
        srt_lnk_lst2.add_last(i)
    print(merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display_list(self):
        temp_list = self.head
        while temp_list:
            print(f"{temp_list.data} => ", end="")
            temp_list = temp_list.next

if __name__=='__main__':
    first_list = [3, 2, 5, 1, 6]
    second_list = [7, 3, 2, 0, 5]
    third_list = [8, 2, 1, 3, 5]


    main_list = LinkedList()
    main_list.head = Node(first_list)
    second = Node(second_list)
    third = Node(third_list)

    main_list.head.next = second
    second.next = third
    main_list.display_list()
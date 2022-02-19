class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def insert_first(self, value):
        new_node = Node(value)
        self.length += 1

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_last(self, value):
        new_node = Node(value)
        self.length += 1

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert(self, previous_value, value):
        """途中に挿入する
        previous_value
            値を挿入する直前の値（場所）
        value
            挿入する値
        """

        self.__check_emptey()

        current_node = self.head
        while current_node.value != previous_value:
            if current_node.next is None:
                print('The inserting index is not found.')
                return
            current_node = current_node.next

        new_node = Node(value)
        new_node.next = current_node.next
        current_node.next = new_node
        self.length += 1

    def remove_first(self):
        self.__check_emptey()

        self.length -= 1
        self.head = self.head.next

    def remove_last(self):
        self.__check_emptey()

        self.length -= 1
        current_node = self.head

        if current_node.next is None:
            self.head = None

        else:
            previous_node = None

            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next

            previous_node.next = None

    def remove(self, value):
        self.__check_emptey()

        current_node = self.head
        previous_node = None
        while current_node.value != value:
            if current_node.next is None:
                print('The removing value is not found.')
                return
            previous_node = current_node
            current_node = current_node.next

        if previous_node is None:
            self.head = current_node.next
            self.length -= 1
        else:
            previous_node.next = current_node.next
            self.length -= 1

    def begin(self):
        self.__check_emptey()
        return self.head.value

    def end(self):
        self.__check_emptey()

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        return current_node.value

    def __str__(self):
        """printの実装

        """

        elements = ''
        current_node = self.head
        while current_node:
            if current_node.next is None:
                elements += str(current_node.value)
            else:
                elements += str(current_node.value) + ', '
            current_node = current_node.next
        return '[' + elements + ']'

    def __len__(self):
        """len()の実装

        """

        return self.length

    def __check_emptey(self):
        if self.head is None:
            print('List is Empty.')
            return

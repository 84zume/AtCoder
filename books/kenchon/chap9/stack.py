from linked_list import LinkedList


class Stack:
    def __init__(self) -> None:
        self.l = LinkedList()

    def push(self, value):
        self.l.insert_first(value)

    def pop(self):
        pop_val = self.l.begin()
        self.l.remove_first()
        return pop_val

    def __len__(self):
        return len(self.l)

    def __str__(self):
        return str(self.l)

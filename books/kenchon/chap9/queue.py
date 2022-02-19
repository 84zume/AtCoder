from linked_list import LinkedList


class Queue:
    def __init__(self) -> None:
        self.l = LinkedList()

    def enqueue(self, value):
        self.l.insert_first(value)

    def dequeue(self):
        pop_val = self.l.end()
        self.l.remove_last()
        return pop_val

    def __len__(self):
        return len(self.l)

    def __str__(self):
        return str(self.l)

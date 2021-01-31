class Queue:
    def __init__(self):
        self.size = 0
        self.elements = []

    def __str__(self):
        return str(self.elements)

    def enqueue(self, element):
        self.elements.append(element)
        self.size += 1

    def dequeue(self):
        self.elements.pop(0)
        self.size -= 1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

'''
Pass in multiple args to this function and it will create a queue
and push the provided arguments as elements onto the newly created
queue. 
'''


def add_to_queue(*args):
    queue = Queue()
    for elem in args:
        queue.enqueue(elem)
    return queue


def main():
    queue = add_to_queue("str1", 2, False)
    while not (queue.is_empty()):
        print(f"Before: {queue}")
        queue.dequeue()
        print(f"After: {queue}")
    print(queue.is_empty())


if __name__ == "__main__":
    main()


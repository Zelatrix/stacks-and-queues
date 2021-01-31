class Stack:
    def __init__(self):
        self.size = 0
        self.elements = []

    def __str__(self):
        return str(self.elements)

    def pop(self):
        self.elements.remove(self.elements[-1])
        self.size -= 1

    def push(self, element):
        self.elements.append(element)
        self.size += 1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


'''
Pass in multiple args to this function and it will create a stack
and push the provided arguments as elements onto the newly created
stack. 
'''


def add_to_stack(*args):
    stack = Stack()
    for elem in args:
        stack.push(elem)
    return stack


# def main():
#     stack = add_to_stack("str1", 2, False)
#
#     while not (stack.is_empty()):
#         print(f"Before: {stack}")
#         stack.pop()
#         print(f"After: {stack}")
#     print(stack.is_empty())
#
#
# if __name__ == '__main__':
#     main()

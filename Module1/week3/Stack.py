class Stack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack_list = []

    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.stack_list) == self.capacity:
            return True
        else:
            return False

    def pop(self):
        if not self.is_empty():
            return self.stack_list.pop()

    def push(self, value):
        if not self.is_full():
            self.stack_list.append(value)

    def top(self):
        if not self.is_empty():
            return self.stack_list[-1]


if __name__ == "__main__":
    stack1 = Stack(capacity=5)
    stack1.push(1)
    stack1.push(2)
    print(stack1.is_full())  # False
    print(stack1.top())  # 2
    print(stack1.pop())  # 2
    print(stack1.top())  # 1
    print(stack1.pop())  # 1
    print(stack1.is_empty())  # True

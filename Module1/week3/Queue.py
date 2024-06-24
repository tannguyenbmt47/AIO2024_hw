class Queue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue_list = []

    def is_empty(self):
        if len(self.queue_list) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.queue_list) == self.capacity:
            return True
        else:
            return False

    def dequeue(self):
        if not self.is_empty():
            return self.queue_list.pop(0)

    def enqueue(self, value):
        if not self.is_full():
            self.queue_list.append(value)

    def front(self):
        if not self.is_empty():
            return self.queue_list[0]


if __name__ == "__main__":
    queue1 = Queue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.is_full())  # False
    print(queue1.front())  # 1
    print(queue1.dequeue())  # 1
    print(queue1.front())  # 2
    print(queue1.dequeue())  # 2
    print(queue1.is_empty())  # True

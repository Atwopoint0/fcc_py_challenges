class CircularQueue:
    def __init__(self, size):
        self.maxSize = size
        self.queueArray = [0] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queueArray[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.maxSize
            if self.isFull():
                self.rear = (self.rear - 1 + self.maxSize) % self.maxSize
                return "Queue is full"
            else:
                self.queueArray[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        if self.isFull():
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.maxSize

    def peek(self):
        if self.isempty():
            return "Queue is empty"
        return self.queueArray[self.front]
    
    def size(self):
        return len(self.queueArray)

    def isEmpty(self):
        return self.front == -1 and self.rear == -1
    
    def isFull(self):
        return self.rear == self.front
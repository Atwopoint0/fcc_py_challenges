# Queue data structure with enqueue, dequeue and peek functions.

class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def dequeue(self):
        if self.queue.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def enqueue(self, element):
        self.queue.append(element)

    def peek(self):
        if self.queue.isEmpty():
            return "queue is empty"
        return self.queue[0]
    
homeworkQueue = Queue()
class PriorityQueue(object):

    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
 
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            exit()
 
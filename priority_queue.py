
class PriorityQueue:
    def __init__(self, queue=None):
        if queue is None:
            self.queue = queue
        self.queue = queue

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def __len__(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == []

    def insert(self, data):
        self.queue.append(data)

    def Extract_Min(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

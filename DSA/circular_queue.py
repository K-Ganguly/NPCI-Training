class CircularQueue :
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.front = self.rear = -1

    def enqueue(self, value):
        if ((self.rear + 1) % self.capacity == self.front):
            print("Queue overflow. Cannot Add")

        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = value

   
    def dequeue(self):
        if (self.front == -1):
            print("Queue empty. Cannot delete.")

        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return temp

    def display_queue(self):
        if(self.front == -1):
            print("Queue empty. No element to display.")

        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

    
if __name__ == "__main__" :
    queue = CircularQueue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(23)
    queue.enqueue(2)
    queue.dequeue()
    queue.display_queue()

         

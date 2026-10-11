class LabSolutions:
    
    # --- Question 1: Implement Stack using Python ---
    class Stack:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return len(self.items) == 0

        def push(self, item):
            self.items.append(item)
            print(f"Pushed {item} to stack.")
         
        def pop(self):
            if self.is_empty():   
                return "Stack is empty (Underflow)"
            return self.items.pop()

        def peek(self):
            if self.is_empty():
                return "Stack is empty"
            return self.items[-1]

        def size(self):
            return len(self.items)

    # --- Question 2: Implement Queue using Python ---
    class Queue:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return len(self.items) == 0

        def enqueue(self, item):
            self.items.append(item)
            print(f"Enqueued {item} to queue.")

        def dequeue(self):
            if self.is_empty():
                return "Queue is empty (Underflow)"
            return self.items.pop(0)

        def front(self):
            if self.is_empty():
                return "Queue is empty"
            return self.items[0]

        def size(self):
            return len(self.items)

    # --- Question 3: Binary Search Implementation ---
    @staticmethod
    def binary_search(arr, target):
        low = 0
        high = len(arr) - 1
        step = 1

        while low <= high:
            mid = (low + high) // 2
            print(f"#{step} -> Low: {low}, High: {high}, Mid: {mid} (Value at Mid: {arr[mid]})")
            
            if arr[mid] == target:
                print("Successful Search !!")
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            step += 1
            
        return -1


# ==========================================
# Execution / Testing All Questions
# ==========================================
if __name__ == "__main__":
    
    print("--- QUESTION 1: STACK DEMO ---")
    stack = LabSolutions.Stack()
    stack.push(10)
    stack.push(20)
    print("Stack Peek:", stack.peek())
    print("Popped:", stack.pop())
    print()

    print("--- QUESTION 2: QUEUE DEMO ---")
    queue = LabSolutions.Queue()
    queue.enqueue(100)
    queue.enqueue(200)
    print("Queue Front:", queue.front())
    print("Dequeued:", queue.dequeue())
    print()

    print("--- QUESTION 3: BINARY SEARCH DEMO ---")
    numbers = [6, 12, 17, 23, 38, 45, 77, 84, 90]
    target_value = 45
    result_index = LabSolutions.binary_search(numbers, target_value)
    print(f"Target {target_value} found at index: {result_index}")

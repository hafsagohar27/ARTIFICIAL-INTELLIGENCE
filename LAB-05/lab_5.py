from collections import deque
import heapq

# =========================
# TASK 1: BFS
# =========================

graph1 = {
    0: [1, 4],
    1: [0, 4, 3, 2],
    2: [1, 3],
    3: [1, 4, 2], 
    4: [0, 1, 3]
}

def bfs_task1(graph, start):
    queue = deque([start])
    visited = {start}

    print("Task 1 - BFS:")
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print()


# =========================
# TASK 2: BFS with Goal
# =========================

graph2 = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}

def bfs_task2(graph, start, goal):
    queue = deque([start])
    visited = {start}

    print("Task 2 - BFS:")
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")

        if node == goal:
            print("\nGoal G achieved!")
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# =========================
# TASK 3: Priority Queue
# =========================

def priority_queue():
    pq = []

    heapq.heappush(pq, (2, "Task B"))
    heapq.heappush(pq, (1, "Task A"))
    heapq.heappush(pq, (3, "Task C"))

    print("\nTask 3 - Priority Queue:")

    while pq:
        priority, task = heapq.heappop(pq)
        print(task, "Priority =", priority)


# =========================
# RUN ALL TASKS
# =========================

bfs_task1(graph1, 0)

bfs_task2(graph2, 'A', 'G')

priority_queue()

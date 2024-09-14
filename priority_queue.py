""" Understanding Priority Queue """

import heapq

class Task:
    """ Task class to represent individual tasks, and storing relevant information """
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

class MinHeapPriorityQueue:
    """ Minimum heap priority queue which will store lowest priority element first """
    def __init__(self):
        self.heap = []

    def shift_down(self, index):
        """ Function to restore min heap property """
        parent = (index - 1) // 2

        # Make sure that the lowest priority is at the root
        while index > 0 and self.heap[parent].priority > self.heap[index].priority:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def insert(self, task):
        """ Insert task into the priority queue as a heap """
        self.heap.append(task)
        self.shift_down(len(self.heap) - 1)

    def heap_mimimum_element(self):
        """ Return the minimum element from the heap """
        if self.is_empty():
            raise IndexError("Minimum Heap Priority queue is empty.")
        return self.heap[0]

    def shift_up(self, index):
        """ Function to shift minimum a subtree rooted with node index """
        heap_size = len(self.heap)
        left = 2 * index + 1                        # Left child index with parent index
        right = 2 * index + 2                       # Right child index with parent index

        # Check to see if the left child of root exists and if it does,
        # check to see if the priority is smaller than the root.
        # Set the smallest to the smaller value index between left child and root
        if (left < heap_size) and (self.heap[left].priority < self.heap[index].priority):
            smallest = left
        else:
            smallest = index

        # Check to see if the right child of root exists and if it does,
        # check to see if the value is smaller than the root.
        # Set the smallest to the right child index in order to swap
        if (right < heap_size) and (self.heap[right].priority < self.heap[smallest].priority):
            smallest = right

        # If the smallest is either left or right child, swap it with the root
        if smallest is not index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]

            # Recursively heapify the affected subtree
            self.shift_up(smallest)

    def extract_min(self):
        """ Function to get the minimum element from the heap """
        max_value = self.heap_mimimum_element()
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.shift_down(0)

        return max_value

    def decrease_key(self, task_id, new_priority):
        """ Function to decrease the priority of a element in the heap """
        for index, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority < task.priority:
                    task.priority = new_priority
                    self.shift_down(index)
                else:
                    raise ValueError("New priority must be smaller than current priority.")
                break

    def is_empty(self):
        """ Return if the heap is empty or not """
        return len(self.heap) == 0

# Task: (ID, Priority, Arrival, Deadline)
pq = MinHeapPriorityQueue()

# Insert tasks
pq.insert(Task(1, 3, '10:00', '12:00'))
pq.insert(Task(2, 5, '10:05', '12:05'))
pq.insert(Task(3, 1, '10:10', '12:10'))

# Extract max
print("Extracted:", pq.extract_min().task_id)  # Should extract the task with the highest priority (Priority 5)

# Increase priority
pq.decrease_key(2, 2)  # Increase task 3's priority to 4

# Check queue state
print("Queue:")
for i in pq.heap:
    print("Task ID: ", i.task_id, " Priority: ", i.priority)

# Check if empty
print("Is queue empty?", pq.is_empty())

heapq.heappush()

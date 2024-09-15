""" Understanding Priority Queue """

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

    def shift_up(self, index):
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
        self.shift_up(len(self.heap) - 1)

    def heap_minimum_element(self):
        """ Return the minimum element from the heap """
        if self.is_empty():
            raise IndexError("Minimum Heap Priority queue is empty.")
        return self.heap[0]

    def shift_down(self, index):
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
            self.shift_down(smallest)

    def extract_min(self):
        """ Function to get the minimum element from the heap """
        min_value = self.heap_minimum_element()         # Get the minimum priority element from the heap
        self.heap[0] = self.heap[-1]
        self.heap.pop()                                 # Remove the last task
        self.shift_down(0)                              # Get the lowest priority element to top

        return min_value

    def decrease_key(self, task_id, new_priority):
        """ Function to decrease the priority of a element in the heap """
        for index, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority < task.priority:
                    task.priority = new_priority
                    self.shift_up(index)                # Maintain heap property
                else:
                    raise ValueError("New priority must be smaller than current priority.")
                break

    def is_empty(self):
        """ Return if the heap is empty or not """
        return len(self.heap) == 0

task_priority_queue = MinHeapPriorityQueue()

# Insert tasks in the queue
task_priority_queue.insert(Task(1, 3, '10:00', '12:00'))
task_priority_queue.insert(Task(2, 5, '10:05', '12:05'))
task_priority_queue.insert(Task(3, 2, '10:10', '12:10'))
task_priority_queue.insert(Task(4, 3, '10:23', '12:15'))
task_priority_queue.insert(Task(5, 1, '10:16', '12:20'))
task_priority_queue.insert(Task(6, 5, '10:30', '12:30'))

# Check queue state
print("Queue before extracting lowest element:")
for i in task_priority_queue.heap:
    print("Task ID: ", i.task_id, " Priority: ", i.priority)

# Extract heap_minimum_element
# Should extract the task with the lowest priority (Task_ID: 5, Priority: 1)
print("Extracted task with task_id:", task_priority_queue.extract_min().task_id)

# Should extract the task with the lowest priority (Task_ID: 3, Priority: 2)
print("Extracted task with task_id:", task_priority_queue.extract_min().task_id)

# Decrease priority
task_priority_queue.decrease_key(2, 2)  # Decrease task 2's priority to 2
task_priority_queue.decrease_key(6, 4)  # Decrease task 6's priority to 3

# Should extract the task with the lowest priority (Task_ID: 3, Priority: 2)
print("Extracted task with task_id:", task_priority_queue.extract_min().task_id)

# Check queue state
print("Queue after extraction:")
for i in task_priority_queue.heap:
    print("Task ID: ", i.task_id, " Priority: ", i.priority)

# Check if empty
print("Is queue empty?", task_priority_queue.is_empty())

# Should extract the task with the lowest priority (Task_ID: 4, Priority: 3)
print("Extracted task with task_id:", task_priority_queue.extract_min().task_id)

# Should extract the task with the lowest priority (Task_ID: 1, Priority: 3)
print("Extracted task with task_id:", task_priority_queue.extract_min().task_id)

# Should extract the task with the lowest priority (Task_ID: 6, Priority: 4)
print("Extracted task with task_id:", task_priority_queue.extract_min().task_id)

# Check if empty
print("Is queue empty?", task_priority_queue.is_empty())

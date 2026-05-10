class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        highest_freq = max(task_counter.values())
        groups = highest_freq - 1
        min_size = groups * (n + 1) # excludes the last group
        last_group_count = sum(highest_freq == v for v in task_counter.values())
        size = min_size + last_group_count
        return max(size, len(tasks))
from collections import deque
import typing as tp


def calculate_max_intervals(intervals: list[tuple[int, int]]) -> int:
    """
    Calculates max intervals without overlap.

    Args:
        intervals: list of intervals sorted by end times in ascending order
                  where intevrals are represented by tuple of ints
    """
    # This is a single interval scheduling problem, optimal solution
    # is a greedy algorithm which  always the interval which ends first
    # and doesn't overlap with any of the previous intervals as the next interval

    START_TIME, END_TIME = 0, 1

    # Converting list to a double ended queue as left pop complexity
    # will be lowered from O(n) to O(1)
    intervals: tp.Deque = deque(intervals)

    last_end_time: int = None
    max_intervals = 0
    while intervals:
        current_interval = intervals.popleft()
        if last_end_time is None or last_end_time <= current_interval[START_TIME]:
            last_end_time = current_interval[END_TIME]
            max_intervals += 1
            print(current_interval)

    return max_intervals

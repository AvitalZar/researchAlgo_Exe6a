import heapq
class sorted_subset_sums:
    """
    An iterator that generates the sums of all subsets of a given set of integers in sorted order.
    The implementation uses a min-heap to efficiently generate the next smallest sum.
    The sets doesn't included in the heap, only the sums.
    examples:
    >>> sorted_subset_sums({1, 2})
    0, 1, 2, 3
    >>> sorted_subset_sums({1, 2, 3})
    0, 1, 2, 3, 3, 4, 5
    >>> sorted_subset_sums({})
    0
    >>> sorted_subset_sums({-1, 0, 2, -2})
    -3, -2, -1, 0, 0, 1, 2, 2
    >>> sorted_subset_sums({0.5, 2.6, 3})
    0.5, 2.6, 3, 3.1, 3.5, 5.6, 6.1
    """
    def __init__(self, s: set):
        self.s = sorted(s)
        self.heap = [] # In the heap there will be a set of the indexes of elements and sum
        heapq.heappush(self.heap, (0, -1)) #(sum, last index)
	
    def __iter__(self):
        return self
        
    def __next__(self):
        if not self.heap:
            raise StopIteration
        sum, last_index = heapq.heappop(self.heap)
        if last_index == -1:
            heapq.heappush(self.heap, (self.s[0], 0))
        elif last_index < len(self.s) - 1:
            next_index = last_index + 1
            heapq.heappush(self.heap, (sum + self.s[next_index], next_index))
            heapq.heappush(self.heap, (sum + self.s[next_index] - self.s[last_index], next_index))
        return sum



if __name__ == '__main__':
    # from itertools import takewhile, islice
    # for i in eval(input()):
    #     print(i, end=", ")
    pass

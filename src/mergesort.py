def merge(t, start, middle, end):
    """Merge parts of t at start and middle."""
    result = []
    left_i = start
    right_i = middle
    while left_i < middle and right_i < end:
        if t[left_i] < t[right_i]:
            result.append(t[left_i])
            left_i += 1
        else:
            result.append(t[right_i])
            right_i += 1
    while left_i < middle:
        result.append(t[left_i])
        left_i += 1
    while right_i < end:
        result.append(t[right_i])
        right_i += 1
    for value in result:
        t[start] = value
        start += 1

def run_merge(t, step):
    """Run an iteration of mergesort."""
    start = 0
    while start + step < len(t):
        merge(t, start, start + step, min(len(t), start + step*2))
        start += step*2


def mergesort(t):
    """Sort t in place."""
    step = 1
    while step < len(t):
        run_merge(t, step)
        step *= 2

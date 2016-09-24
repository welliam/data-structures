def merge(t, start, middle, end):
    result = []
    left_i = start
    right_i = middle
    while left_i < middle and right_i < end:
        print('at left_i={}: {}'.format(left_i, t[left_i]))
        print('at right_i={}: {}'.format(right_i, t[right_i]))
        print('result', result)
        print()
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

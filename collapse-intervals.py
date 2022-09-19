def collapse_intervals(items):
    items = list(items)

    intervals = []
    while (items):
        start = items.pop(0)
        last = start
        end = start
        while items:
            end = items[0]
            if end != last+1:
                break
            last = items[0]
            items.pop(0)
        interval = str(start)
        interval += '-'+str(last) if start != last else ''
        intervals.append(interval)
    ans = ','.join(intervals)
    return ans

print(collapse_intervals([1, 2, 4, 6, 7, 8, 9, 10, 12, 13]))
print(collapse_intervals([42]))
print(collapse_intervals([3, 5, 6, 7, 9, 11, 12, 13]))
print(collapse_intervals([]))
print(collapse_intervals(range(1, 1001)))
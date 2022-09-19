def frequency_sort(items):
    d = {}
    for ai in items:
        d[ai] = d.get(ai, 0)+1
    ordered_pairs = sorted(d.items(), key=lambda x : (-x[1],x[0]))
    ans = []
    for k , v in ordered_pairs:
        ans.extend(v*[k])
    return ans

print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
print(frequency_sort([4, 6, 1, 2, 2, 1, 1, 6, 1, 1, 6, 4, 4, 1]))
print(frequency_sort([17, 99, 42]))
print(frequency_sort(['bob','bob','carl','alex','bob']))
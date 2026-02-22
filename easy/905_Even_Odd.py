
"""
Complexity
- Time: O(n)
- Space: O(1) (in-place)
- Stable? No (relative order not preserved, but problem doesn’t require it)
"""

def even_odd(arr):

    next_even, next_odd = 0, len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -=1

    return arr
    
    
print(even_odd([1, 2, 3, 4, 5, 6]))
print(even_odd([0, 3, 1, 2, 4]))


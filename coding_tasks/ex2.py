# Space complexity - O(2n)
# Time complexity - O(n*mˆ2)

# In this case we can assume that mˆ2 = const = 26ˆ2

def max_sub_str(s):
    s = s.replace(" ", "")
    s = s[3:(len(s)-1)]

    arr = []
    max_s = 0

    """
    m - number of different chars in s
    0 < m < 27
    """

    for i in s: # O(n) Worst case
        if i in arr: # O(m) Worst case
           if len(arr) > max_s:
               max_s = len(arr)
           j = 0
           while arr[j] != i: # O(m) Worst case
               arr.pop(0)
           arr.pop(0)
           arr.append(i)
        else:
            arr.append(i)
    return max_s


st = input()
print(max_sub_str(st))

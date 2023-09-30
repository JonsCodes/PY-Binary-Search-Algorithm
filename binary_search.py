# code your iterative algorithm here

def recursive_bsearch(data, el, first=0, last=None):
    if last is None:
        last = len(data) - 1

    if first <= last:
        mid = (first + last) // 2
        if data[mid] == el:
            return True
        elif el < data[mid]:
            return recursive_bsearch(data, el, first, mid-1)
        else:
            return recursive_bsearch(data, el, mid+1, last)
    else:
        return False

lst = [5, 8, 12, 14, 17, 23, 27]

print(recursive_bsearch(lst, 12))  # Expected output: True
print(recursive_bsearch(lst, 11))  # Expected output: False

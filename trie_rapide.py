def quick_sort(data: list) -> list:
    """
    >>> for data in ([2, 1, 0], [2.2, 1.1, 0], "quick_sort"):
    ...     quick_sort(data) == sorted(data)
    True
    True
    True
    """
    if len(data) <= 1:
        return data
    else:
        return (
            quick_sort([e for e in data[1:] if e <= data[0]])
            + [data[0]]
            + quick_sort([e for e in data[1:] if e > data[0]])
        )



chaine = "quick_sort"
liste = [3,25,6,7,1,8]
result = quick_sort(chaine)

print(result)
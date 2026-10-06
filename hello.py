print("Hello, World!")


def quick_sort(items):
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    middle = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    sample_data = [3, 6, 1, 8, 2, 9, 4]
    print(quick_sort(sample_data))

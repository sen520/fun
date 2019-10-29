# coding=utf-8

"""realize timsort"""


def binary_search(arr, left, right, value):
    """
    二分查找
    :param arr: 列表
    :param left: 左索引
    :param right: 右索引
    :param value: 需要插入的值
    :return: 插入值所在的列表位置
    """
    if left >= right:
        if arr[left] <= value:
            return left + 1
        else:
            return left
    elif left < right:
        mid = (left + right) // 2
        if arr[mid] < value:
            return binary_search(arr, mid + 1, right, value)
        else:
            return binary_search(arr, left, mid - 1, value)


def insertion_sort(arr):
    """
    针对run使用二分折半插入排序
    :param arr: 列表
    :return: 结果列表
    """
    length = len(arr)
    for index in range(1, length):
        value = arr[index]
        pos = binary_search(arr, 0, index - 1, value)
        arr = arr[:pos] + [value] + arr[pos:index] + arr[index + 1:]
    return arr


def merge(l1, l2):
    """
    合并
    :param l1: 列表1
    :param l2: 列表2
    :return: 结果列表
    """
    if not l1:
        return l2
    if not l2:
        return l1
    if l1[0] < l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])


def timsort(arr):
    """
    timsort
    :param arr: 待排序数组
    :return:
    """
    if not arr:  # 空列表
        return
    runs, sorted_runs = [], []
    new_run = [arr[0]]
    length = len(arr)
    # 划分run区，并存储到runs里，这里简单的按照升序划分，没有考虑降序的run
    for index in range(1, length):
        if arr[index] < arr[index - 1]:
            runs.append(new_run)
            new_run = [arr[index]]
        else:
            new_run.append(arr[index])
        if length - 1 == index:
            runs.append(new_run)
            break

    # 由于仅仅是升序的run，没有涉及到run的扩充和降序的run
    # 因此，其实这里没有必要使用insertion_sort来进行run自身的排序
    for run in runs:
        insertion_sort(run)

    # 合并runs
    sorted_arr = []
    for run in runs:
        sorted_arr = merge(sorted_arr, run)
    print(sorted_arr)


if __name__ == '__main__':
    timsort([1, 2, 42, 12, 23, 12, 43, 546, 678, 435, 23, 544, 76, 54])

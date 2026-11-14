"""Модуль алгоритмов поиска (ЛР7)."""

def linear_search(nums: list[int], x: int) -> int:
    """Индекс первого вхождения x или -1.
    Работает за O(n), не требует сортировки.
    """
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

def binary_search(sorted_nums: list[int], x: int) -> int:
    """Индекс x в отсортированном по возрастанию списке или -1.
    На неотсортированном списке результат не определён.
    """
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def two_sum_brute(nums: list[int], target: int) -> tuple[int, int] | None:
    """Перебор пар: O(n^2). Возвращает индексы (i, j) или None."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    """Через словарь: O(n). Возвращает индексы (i, j) или None."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None
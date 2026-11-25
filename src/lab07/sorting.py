"""Модуль алгоритмов сортировки (ЛР7)."""

def bubble_sort(nums: list[int]) -> list[int]:
    """Пузырьковая сортировка. Возвращает НОВЫЙ отсортированный список."""
    res = list(nums)
    for i in range(len(res)):
        swapped = False
        for j in range(0, len(res) - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
                swapped = True
        if not swapped: break
    return res
  
def insertion_sort(nums: list[int]) -> list[int]:
    """Сортировка вставками. Возвращает НОВЫЙ отсортированный список."""
    res = list(nums)
    for i in range(1, len(res)):
        key = res[i]
        j = i - 1
        while j >= 0 and res[j] > key:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = key
    return res

def selection_sort(nums: list[int]) -> list[int]:
    """Сортировка выбором. Возвращает НОВЫЙ отсортированный список."""
    res = list(nums)
    for i in range(len(res)):
        min_idx = i
        for j in range(i + 1, len(res)):
            if res[j] < res[min_idx]: min_idx = j
        res[i], res[min_idx] = res[min_idx], res[i]
    return res
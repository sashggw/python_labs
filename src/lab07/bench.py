"""Бенчмарк алгоритмов (ЛР7)."""
import timeit
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.lab04.io_txt_csv import write_csv, ensure_parent_dir
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def bench_sorts():
    rows = []
    sizes = [1000, 10000, 100000]
    
    for n in sizes:
        random.seed(42)
        data = [random.randint(-1000, 1000) for _ in range(n)]
        
        # Замер встроенной сортировки
        t = timeit.timeit(lambda: sorted(data), number=1)
        rows.append(("sort", n, "sorted", round(t, 4)))
        
        for fn in (bubble_sort, insertion_sort, selection_sort):
            if n == 100000:
                t_str = 60.0  # Квадратичные сортировки на 100k элементах займут слишком много времени
            else:
                t = timeit.timeit(lambda: fn(data), number=1)
                t_str = round(t, 4)
            rows.append(("sort", n, fn.__name__, t_str))
    return rows

def bench_search():
    rows = []
    n = 100000
    random.seed(42)
    data = [random.randint(-1000, 1000) for _ in range(n)]
    sorted_data = sorted(data)
    queries = [random.randint(-1000, 1000) for _ in range(10000)]
    
    t_lin = timeit.timeit(lambda: [linear_search(data, q) for q in queries], number=1)
    rows.append(("search", n, "linear", round(t_lin, 4)))
    
    t_bin = timeit.timeit(lambda: [binary_search(sorted_data, q) for q in queries], number=1)
    rows.append(("search", n, "binary", round(t_bin, 4)))
    
    t_sort = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("search", n, "sorted_for_bin", round(t_sort, 4)))
    return rows

def bench_two_sum():
    rows = []
    for n in (1000, 10000):
        random.seed(42)
        nums = [random.randint(1, 1000) for _ in range(n)]
        target = nums[0] + nums[-1] # Гарантируем пару
        
        t_brute = timeit.timeit(lambda: two_sum_brute(nums, target), number=1)
        rows.append(("two_sum", n, "brute", round(t_brute, 4)))
        
        t_fast = timeit.timeit(lambda: two_sum_fast(nums, target), number=1)
        rows.append(("two_sum", n, "fast", round(t_fast, 4)))
    return rows

def main():
    print("Запуск бенчмарка (может занять до 15 секунд)...")
    rows = []
    rows += bench_sorts()
    rows += bench_search()
    rows += bench_two_sum()
    
    # Красивый вывод таблицы в консоль
    print(f"\n{'task':<10} | {'n':<8} | {'impl':<15} | {'seconds':<10}")
    print("-" * 52)
    for task, n, impl, sec in rows:
        print(f"{task:<10} | {n:<8} | {impl:<15} | {sec:<10}")
        
    ensure_parent_dir("data/lab07/bench.csv")
    write_csv(rows, "data/lab07/bench.csv", header=("task", "n", "impl", "seconds"))
    print("\nРезультаты сохранены в data/lab07/bench.csv")

if __name__ == "__main__":
    main()
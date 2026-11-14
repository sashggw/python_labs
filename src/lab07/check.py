"""Проверка алгоритмов против эталона (ЛР7)."""
import random
import sys
from pathlib import Path

# Добавляем корень проекта в sys.path (как в Лекции 10)
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)  # Копия для проверки мутации
        result = fn(nums)
        
        # 1. Сравниваем с эталоном sorted
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        # 2. Проверяем, что исходный список не изменен
        assert nums == original, f"{fn.__name__} изменила исходный список"

def check_search():
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-100, 100)
        
        # 1. Линейный поиск (здесь мы ищем первое вхождение, как в list.index)
        res_lin = linear_search(nums, x)
        try:
            expected_lin = nums.index(x)
        except ValueError:
            expected_lin = -1
        assert res_lin == expected_lin, f"linear_search ошиблась на {nums}, искали {x}"
        
        # 2. Бинарный поиск (может вернуть ЛЮБОЕ вхождение)
        sorted_nums = sorted(nums)
        res_bin = binary_search(sorted_nums, x)
        
        try:
            sorted_nums.index(x) # Проверяем, есть ли вообще число
            # Если есть, проверяем, что бинарный поиск вернул индекс именно этого числа
            assert res_bin != -1 and sorted_nums[res_bin] == x, \
                f"binary_search вернула неверный индекс для {x} на {sorted_nums}"
        except ValueError:
            # Если числа нет, бинарный поиск обязан вернуть -1
            assert res_bin == -1, f"binary_search должна была вернуть -1 для {x}, но вернула {res_bin}"
            
def check_two_sum(trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-200, 200)
        
        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)
        
        if res_brute is None:
            assert res_fast is None, f"two_sum_fast нашла пару {res_fast}, а brute нет. {nums}, target={target}"
        else:
            i, j = res_brute
            assert nums[i] + nums[j] == target, "two_sum_brute вернула неверную пару"
            if res_fast is not None:
                i2, j2 = res_fast
                assert nums[i2] + nums[j2] == target, "two_sum_fast вернула неверную пару"

if __name__ == "__main__":
    random.seed(42)  # Фиксируем seed для повторяемости
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print("OK: все проверки пройдены успешно")
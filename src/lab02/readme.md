## ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

### * Задание 1 — arrays.py

#### В коде реализованы функции:
* min_max()
Возвращает кортеж (минимум, максимум). Если список пуст — ValueError.
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    min_val = max_val = nums[0]

    for num in nums[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val

```

* unique_sorted()
Возвращает отсортированный список уникальных значений (по возрастанию).


```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
```

* flatten()
«Расплющивает» список списков/кортежей в один список по строкам (row-major). Если встретилась строка/элемент, который не является списком/кортежем — TypeError.


```python
def flatten(mat: list[list | tuple]) -> list:
    for i in mat:
        if i.__class__ != list and i.__class__ != tuple :
            #raise ValueError("TypeError:строка/элемент не является списком/кортежем")
            return 'TypeError:строка/элемент не является списком/кортежем'
    big_list = []
    for stroka in mat:
        for element in stroka:
           big_list.append(element)
    return big_list

```
### Тест-кейсы:
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab02/min_max.png)
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab02/uniquue_sorted.png)
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab02/flatten.png)

### * Задание 2 — matrix.py

#### Программа на входе получает матрицу и совершает над ней разные действия:
* transpose()
##### Меняет строки и столбцы местами. Пустая матрица [] → [].
##### Если матрица «рваная» (строки разной длины) — ValueError.

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    for i in range(len(mat)):
        if len(mat[i]) != len(mat[0]):
            return 'TypeError:матрица рваная '
            
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
```
* row_sums()
##### Суммирует по каждой строке. Требуется прямоугольность (см. выше).
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(mat)):
            if len(mat[i]) != len(mat[0]):
                return 'TypeError:матрица рваная '


    return [sum(row) for row in mat]
```
* col_sums()
##### Суммирует по каждому столбцу. Требуется прямоугольность.
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(mat)):
                if len(mat[i]) != len(mat[0]):
                    return 'TypeError:матрица рваная '
    return [sum(col) for col in zip(*mat)]
```

### Тест-кейсы: 
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab02/transpose.png)
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab02/row_sum.png)
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab02/col_sum.png)

### * Задание 3 - tuples.py

#### Код преобразовывает полученные ФИО , группу и GPA в стандартый формат с правилами:


* ФИО может быть «Фамилия Имя Отчество» или «Фамилия Имя» — инициалы формируются из 1–2 имён (в верхнем регистре).
* Лишние пробелы нужно убрать (strip, «схлопнуть» внутри).
* GPA печатается с 2 знаками (округление правилами Python).

```python

def format_record(rec: tuple[str, str, float]) -> str:

    if rec.__class__!= tuple: raise TypeError("был введен не кортеж")
    if len(rec) < 3: raise TypeError("недостаточно данных")
    if len(rec) > 3: raise TypeError("излишек данных")

    fio, group, gpa = rec

    if group.__class__ != str: raise TypeError("не правильный формат группы")
    if fio.__class__ != str: raise TypeError("не правильный формат ФИО")
    if gpa.__class__ != int and gpa.__class__ != float: raise TypeError("не правильный формат gpa")

    fio_parts = fio.split()
    if len(fio_parts) < 2: raise ValueError("Слишком короткое ФИО")
    if not group.strip(): raise ValueError("пустая группа")

    surname = fio_parts[0].capitalize()

    initials = ""
    for name in fio_parts[1:3]:
        initials += name[0].upper() + "."

    return f"{surname} {initials}, гр. {group.strip()}, GPA {gpa:.2f}"

```
### Тест-кейсы:
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab02/format_record.png)
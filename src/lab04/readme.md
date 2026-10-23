# README по ЛР4 — под ваш код

## Задание A — `io_txt_csv.py`

Модуль для чтения текстовых файлов и записи результатов в CSV. Для работы с путями используется `Path`, для формирования CSV — стандартный модуль `csv`. Все функции имеют докстринги и аннотации типов.

Реализованы следующие функции:

### 1. Функция **read_text**

Функция читает файл целиком и возвращает его содержимое в виде одной строки. По умолчанию используется кодировка UTF-8, но при необходимости можно передать другую кодировку, например `encoding="cp1251"`.

Если файл не найден — возникает `FileNotFoundError`. При несовпадении кодировки — `UnicodeDecodeError`. Оба исключения пробрасываются наверх (по ТЗ «пусть падает»), а вызывающий код (`text_report.py`) ловит их и выводит понятное сообщение.

**Код:**

```python
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Прочитать файл целиком и вернуть содержимое как строку.

    Если файл сохранён в другой кодировке (например, Windows-1251),
    передайте encoding="cp1251".
    """
    p = Path(path)
    return p.read_text(encoding=encoding)
```

#### При правильной кодировке
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/case_A_basic.png)
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/1.png)

#### При иной кодировке
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/5.png)
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/case_E_bad_encoding.png)

### 2. Функция **write_csv**

Функция записывает строки в CSV-файл с разделителем `,` и кодировкой UTF-8. Перед записью проверяется, что все строки имеют одинаковую длину. Если длины различаются — вызывается `ValueError`.

Логика проверки: если передан `header`, его длина выбирается за эталонную; иначе эталоном служит длина первой строки. Если `rows` пуст и `header is None` — создаётся пустой файл (0 строк). Если `rows` пуст, но `header` задан — файл содержит только заголовок (это и есть политика для пустого входа из ТЗ).

Перед открытием файла вызывается `ensure_parent_dir(path)` — чтобы не падать, если папки `data/lab04/` ещё нет.

**Код:**

```python
def write_csv(
        rows: Iterable[Sequence],
        path: str | Path,
        header: tuple[str, ...] | None = None,
) -> None:
    """Записать строки в CSV-файл (UTF-8, разделитель ',').

    ValueError, если строки имеют разную длину.
    """
    rows = list(rows)

    if header is not None:
        expected = len(header)
    elif rows:
        expected = len(rows[0])
    else:
        expected = None

    for number, row in enumerate(rows, start=1):
        if len(row) != expected:
            raise ValueError(
                f'Строка {number} содержит {len(row)} значений, ожидалось {expected}'
            )
    ensure_parent_dir(path)
    with Path(path).open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)
```

#### Пример, когда длины строк отличаются
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/case_F_write_csv_error.png)

### 3. Функция **ensure_parent_dir**

Функция проверяет наличие родительской папки и создаёт её вместе со всеми отсутствующими вложенными папками (`parents=True`), не падая, если папка уже существует (`exist_ok=True`). Нужна перед записью CSV, чтобы скрипт работал в чистом репозитории, где `data/lab04/` ещё нет.

**Код:**

```python
def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории для path, если их нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
```

#### Пример запуска
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/case_G_ensure_dir.png)
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/6.png)

Результат записи данных в CSV-файл.


## Задание B — скрипт `text_report.py`

Скрипт читает текстовые файлы, использует функции `normalize`, `tokenize`, `count_freq` и `top_n` из лабораторной работы №3, а затем сохраняет частоты слов в CSV-файл.

Поведение:

- Один входной файл → `data/lab04/report.csv` с колонками `word,count`, отсортированными по `count ↓`, затем `word ↑`.
- В консоль печатается резюме: всего слов, уникальных слов, топ-5.
- Пустой файл → `report.csv` содержит только заголовок `word,count` (0 строк данных).
- Несуществующий файл → сообщение в `stderr` и `sys.exit(1)`.
- Неверная кодировка → подсказка попробовать `--encoding cp1251`, `sys.exit(1)`.
- Для корректной работы импортов `src/lab04/text_report.py` добавляет в `sys.path` и `src/` (для `lib.text`), и `src/lab04/` (для `io_txt_csv`), поэтому запускается из корня репозитория.

**Ключевые фрагменты кода:**

```python
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Считает частоты слов в тексте и сохраняет отчёт в CSV."
    )
    parser.add_argument(
        "--in", dest="input_path", default="data/lab04/input.txt",
        help="входной файл (по умолчанию data/lab04/input.txt)",
    )
    parser.add_argument(
        "--out", dest="output_path", default="data/lab04/report.csv",
        help="выходной файл (по умолчанию data/lab04/report.csv)",
    )
    parser.add_argument(
        "--encoding", default="utf-8",
        help="кодировка входного файла (по умолчанию utf-8)",
    )
    return parser.parse_args()


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Пары (слово, частота), сортировка: count ↓, слово ↑."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def main() -> None:
    args = parse_args()

    try:
        text = read_text(args.input_path, encoding=args.encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input_path}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(
            f"Ошибка: не удалось прочитать файл в кодировке {args.encoding}. "
            "Попробуйте указать другую, например --encoding cp1251",
            file=sys.stderr,
        )
        sys.exit(1)

    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    write_csv(sorted_word_counts(freq), args.output_path,
              header=("word", "count"))

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")
```

### Пример запуска для одного файла

```bash
python src/lab04/text_report.py
```

В этом режиме читается `data/lab04/input.txt` (дефолт из `parse_args`), а результат записывается в `data/lab04/report.csv`.

#### Пример запуска
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/case_A_basic.png)
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/1.png)

### Запуск файла с нестандартной кодировкой

```bash
python src/lab04/text_report.py --in data/lab04/cp1251.txt --encoding cp1251
```

#### Кодировка cp1251
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/case_C_cp1251.png)
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/3.png)

### Запуск несуществующего файла

```bash
python src/lab04/text_report.py --in data/lab04/nope.txt
```

Скрипт печатает `Ошибка: файл не найден: data/lab04/nope.txt` в `stderr` и завершается с кодом 1.

#### Пример запуска
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/case_D_not_found.png)

### Политика для пустого входа

Если `data/lab04/input.txt` пуст, `data/lab04/report.csv` будет содержать **только заголовок** `word,count` (0 строк данных).

#### Пример запуска
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/case_B_empty.png)
![](https://github.com/sashggw/python_labs/blob/main/image/lab04/2.png)
# Отчет по лабораторной работе №6 — CLI-утилиты с argparse

## Структура лабораторной работы
- `src/lab06/cli_text.py` — утилиты для работы с текстом (команды `cat` и `stats`);
- `src/lab06/cli_convert.py` — конвертеры данных (команды `json2csv`, `csv2json`, `csv2xlsx`).

Все команды запускаются из корня проекта. Для вывода справки по любой команде используется флаг `--help`.


## Задание A — Утилита для текста (`cli_text.py`)

Модуль поддерживает две подкоманды.

### 1. Подкоманда `cat`
Выводит содержимое файла в консоль. С флагом `-n` нумерует строки.

Пример запуска:
```bash
python src/lab06/cli_text.py cat --input data/samples/people.csv -n
```

Код реализации:
```python
def cmd_cat(args):
    """Вывод содержимого файла (аналог cat)."""
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            if args.n:
                for i, line in enumerate(f, start=1):
                    print(f"{i:6d}  {line}", end='')
            else:
                print(f.read(), end='')
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input}", file=sys.stderr)
        sys.exit(1)
```
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab06/02_cat.png)
Рис. 1. Вывод содержимого файла с нумерацией строк.

### 2. Подкоманда stats
Анализирует частоту слов в текстовом файле, используя функции из ЛР3.

Пример запуска:
```bash
python src/lab06/cli_text.py stats --input data/samples/people.txt --top 3
```
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab06/03_stats.png)
Рис. 2. Анализ частот слов.

## Задание B — CLI-конвертеры (cli_convert.py)
Модуль использует функции конвертации из ЛР5, обернутые в argparse.

Поддерживаемые команды:
json2csv — конвертирует JSON в CSV;
csv2json — конвертирует CSV в JSON;
csv2xlsx — конвертирует CSV в Excel (XLSX).

Пример запуска всех трех конвертеров:
```bash
python src/lab06/cli_convert.py json2csv --in data/samples/people.json --out data/out/cli_people.csv
python src/lab06/cli_convert.py csv2json --in data/samples/people.csv --out data/out/cli_people.json
python src/lab06/cli_convert.py csv2xlsx --in data/samples/people.csv --out data/out/cli_people.xlsx
```

Код реализации:
```python
def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)
    
    # ... добавление других подкоманд ...

    args = parser.parse_args()

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        # ... обработка других команд ...
        print(f"Успешно: {args.input} -> {args.output}")
    except Exception as e:
        print(f"Ошибка конвертации: {e}", file=sys.stderr)
        sys.exit(1)
```
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab06/04_convert.png)
Рис. 3. Успешное выполнение трех конвертаций.

Справка и обработка ошибок
Для вывода всех доступных команд и параметров используется стандартный флаг --help.

Пример запуска:
```bash
python src/lab06/cli_text.py --help
python src/lab06/cli_convert.py --help
```
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab06/01_help.png)
Рис. 4. Работа встроенной справки argparse.

При передаче несуществующего файла программа не выбрасывает стек вызовов (Traceback), а выводит аккуратное сообщение об ошибке.

Пример запуска:
```bash
python src/lab06/cli_text.py cat --input data/samples/nope.txt
```
![Пример работы](https://github.com/sashggw/python_labs/blob/main/image/lab06/05_error.png)
Рис. 5. Обработка ошибки (файл не найден).
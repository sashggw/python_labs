# Отчет по лабораторной работе №5 — JSON, CSV и XLSX

## Структура лабораторной работы
- `src/lab05/json_csv.py` — преобразование JSON в CSV и CSV в JSON;
- `src/lab05/csv_xlsx.py` — преобразование CSV в XLSX.

Входные примеры находятся в каталоге `data/samples/`, а результаты конвертаций — в каталоге `data/out/`.

---

## Задание A — JSON ↔ CSV

Модуль `json_csv.py` содержит две функции.

### 1. Функция `json_to_csv`

Функция читает JSON-файл (список словарей) и сохраняет его в CSV. Если у объектов разные ключи, они объединяются в общий список колонок, а отсутствующие значения заполняются пустыми строками. Кодировка — строго UTF-8.

Код:

```python
def json_to_csv(json_path: str, csv_path: str) -> None:
    jp = Path(json_path)
    cp = Path(csv_path)

    if not jp.exists():
        raise FileNotFoundError("Указанный JSON файл не найден")

    if jp.suffix.lower() != '.json':
        raise ValueError("Указанный файл не формата JSON")

    with jp.open('r', encoding='utf-8') as p:
        try:
            data = json.load(p)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError('Файл JSON пустой или имеет неправильный формат')
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка JSON должны быть словарями")

    ensure_parent_dir(cp)
    fieldnames = {}
    for element in data:
        for key in element.keys():
            fieldnames[key] = None

    with cp.open('w', newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames.keys()))
        w.writeheader()
        w.writerows(data)
```

Функция:
Проверяет существование входного файла.
Проверяет расширение .json.
Читает JSON в кодировке UTF-8.
Проверяет, что корневой объект является непустым списком словарей.
Собирает названия всех ключей в порядке их первого появления.
Записывает заголовок и строки в CSV в кодировке UTF-8.

Пример вызова:

```python
json_to_csv(
    "data/samples/people.json",
    "data/out/people_from_json.csv",
)
```
![Пример работы (JSON → CSV)](https://github.com/sashggw/python_labs/blob/main/image/lab05/samples%20-%20out.png)
Рис. 1. Результат преобразования JSON в CSV.

### 2. Функция csv_to_json
Функция читает CSV-файл, использует первую строку как заголовок, а каждую последующую строку превращает в словарь. Результат сохраняется в отформатированный JSON (с отступом в 2 пробела).

Код:

```python
def csv_to_json(csv_path: str, json_path: str) -> None:
    jp = Path(json_path)
    cp = Path(csv_path)

    if not cp.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")

    if cp.suffix.lower() != '.csv':
        raise ValueError("Указанный файл не формата CSV")

    with cp.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("Файл CSV пустой")

        data = list(reader)

    if not data:
        raise ValueError("Файл CSV не содержит данных")

    ensure_parent_dir(jp)
    with jp.open('w', encoding='utf-8') as p:
        json.dump(data, p, ensure_ascii=False, indent=2)
```

Функция:
Проверяет существование входного файла.
Проверяет расширение .csv.
Читает CSV в кодировке UTF-8.
Проверяет наличие заголовка и хотя бы одной строки данных.
Преобразует каждую строку в словарь.
Сохраняет список словарей в JSON с отступом в два пробела.

Пример вызова:

```python
csv_to_json(
    "data/samples/people.csv",
    "data/out/people_from_csv.json",
)
```
![Пример работы (CSV → JSON)](https://github.com/sashggw/python_labs/blob/main/image/lab05/img_xlsx_result.png)
Рис. 2. Результат преобразования CSV в JSON.


## Задание B — CSV → XLSX
Модуль csv_xlsx.py содержит функцию конвертации таблицы в формат Excel.

Функция csv_to_xlsx
Функция создает книгу Excel (через библиотеку openpyxl), переносит туда данные из CSV и автоматически подбирает ширину колонок (минимум 8 символов), чтобы текст не обрезался.

Код:

```python
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    cp = Path(csv_path)
    xlp = Path(xlsx_path)

    if not cp.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")

    if cp.suffix.lower() != '.csv':
        raise ValueError("Указанный файл не формата CSV")

    with cp.open('r', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))

    if not reader:
        raise ValueError("Файл CSV пустой")

    wb = Workbook()
    ws = wb.active
    assert ws is not None
    ws.title = "Sheet1"
    for row in reader:
        ws.append(row)

    for col in ws.columns:
        max_len = 0
        letter = col[0].column_letter

        for cell in col:
            if cell.value and len(str(cell.value)) > max_len:
                max_len = len(str(cell.value))

        ws.column_dimensions[letter].width = max(max_len, 8)

    ensure_parent_dir(xlp)
    wb.save(xlp)
```

Функция:
Проверяет существование CSV-файла.
Проверяет расширение .csv.
Читает строки в кодировке UTF-8.
Создаёт книгу Excel с помощью openpyxl.
Добавляет строки CSV на лист Sheet1.
Рассчитывает ширину столбцов (по самому длинному значению, но не менее 8).
Сохраняет результат по указанному пути.

Пример вызова:

```python
csv_to_xlsx(
    "data/samples/people.csv",
    "data/out/people.xlsx",
)
```
![Пример работы (CSV → XLSX)](https://github.com/sashggw/python_labs/blob/main/image/lab05/img_xlsx_result.png)
Рис. 3. Результат преобразования CSV в XLSX.

### Обработка ошибок (Валидация)

При попытке передать в функцию `json_to_csv` файл с другим расширением (например, CSV) или невалидные данные, выбрасывается исключение `ValueError` (или `JSONDecodeError`). Это защищает программу от создания битых файлов.

![Ошибка валидации](https://github.com/sashggw/python_labs/blob/main/image/lab05/img_validation_error.png)
Рис. 4. Проверка обработки исключения при неверном формате файла.*
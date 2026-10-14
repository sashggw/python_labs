# ЛР3 — Тексты и частоты слов
## text.py
### --------------------NORMALIZE--------------------
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not isinstance(text, str):
        raise ValueError("ожидалась строка (str), получено: " + type(text).__name__) # проверка на принадлежность к определённому классу

    # 1. Регистр.
    if casefold: text = text.casefold()
    else: text = text.lower()

    # 2. ё → е (после смены регистра обе буквы уже в нижнем регистре).
    if yo2e: text = text.replace("ё", "е")

    # 3. Пробельные → один пробел, без ведущего и хвостового.
    chars = []
    prev_space = True 
    for ch in text:
        if _is_whitespace(ch):
            if not prev_space:
                chars.append(" ")
                prev_space = True
        else:
            chars.append(ch)
            prev_space = False

    if chars and chars[-1] == " ": chars.pop()
    return "".join(chars)
```

Функция приводит строку к единому виду: меняет регистр (casefold или lower), при необходимости заменяет ё/Ё на е/Е, а все пробельные символы (\n, \t, \r, пробелы) схлопывает в один пробел и обрезает края. Список chars копит символы, флаг prev_space не даёт записать два пробела подряд и убирает ведущий пробел, а pop() в конце снимает хвостовой.

![Примеры](https://github.com/sashggw/python_labs/blob/main/image/lab03/lib.normalize.png)

### --------------------TOKENIZE--------------------
```python
def tokenize(text: str) -> list[str]:
    if not isinstance(text, str):
        raise ValueError("ожидалась строка (str), получено: " + type(text).__name__) # проверка на принадлежность к определённому классу

    tokens = []
    buf = []           
    pending_dash = False  

    for ch in text:
        if _is_word_char(ch):
            if pending_dash and buf: buf.append("-")
            pending_dash = False
            buf.append(ch)
        elif ch == "-":
            if buf: pending_dash = True
        else:
            if buf:
                tokens.append("".join(buf))
                buf = []
            pending_dash = False

    if buf: tokens.append("".join(buf))
    return tokens
```

Функция разбивает текст на слова. Идёт по символам, копит буквы/цифры/подчёркивание в буфер buf, а дефис запоминает в pending_dash и вставляет его в слово, только если после дефиса снова идёт буква или цифра (так «по-настоящему» остаётся одним словом, а «-привет-» превращается в «привет»). Всё остальное — разделитель: буфер сбрасывается в tokens.

![Примеры](https://github.com/sashggw/python_labs/blob/main/image/lab03/lib.tokensize.png)

### --------------------COUNT_FREQ--------------------
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    if not isinstance(tokens, list): 
        raise ValueError("ожидался список (list), получено: " + type(tokens).__name__) # проверка на принадлежность к определённому классу

    freq = {}
    for tok in tokens:
        if tok in freq: freq[tok] = freq[tok] + 1
        else: freq[tok] = 1
    return freq
```

Функция заводит словарь с ключом-словом и значением-количеством вхождений. Метод get при отсутствии слова в словаре возвращает 0 и не бросает KeyError, поэтому freq[w] = freq.get(w, 0) + 1 работает и для первого вхождения слова.

### --------------------TOP_N--------------------
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not isinstance(freq, dict):
        raise ValueError("ожидался словарь (dict), получено: " + type(freq).__name__) # проверка на принадлежность к определённому классу
    if not isinstance(n, int):
        raise ValueError("ожидалось целое число (int), получено: " + type(n).__name__) # проверка на принадлежность к определённому классу
    if n <= 0: return []
```

Функция возвращает первые n пар «слово → частота» из словаря. Сортирует пары по ключу (-частота, слово): минус перед частотой даёт убывание без reverse=True, а второй элемент кортежа обеспечивает алфавитный порядок при равных частотах. Срез [:n] берёт только первые n записей.

![Пример](https://github.com/sashggw/python_labs/blob/main/image/lab03/lib.count_freq%2Btop_n.png)

## --------------------TEXT_STATS.PY--------------------
```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.text import normalize, tokenize, count_freq, top_n


def main() -> None:
    text = sys.stdin.read()
    text = normalize(text)
    tokens = tokenize(text)
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
```

Функция читает весь ввод из stdin через sys.stdin.read(), прогоняет его через normalize, tokenize и count_freq, а затем печатает статистику: сколько всего слов (len(tokens)), сколько уникальных (len(freq) — ключи словаря уникальны по определению) и топ-5 частотных слов в формате слово:количество. Список пар для печати даёт top_n(freq, n=5), а распаковка for word, count in ... сразу разбирает каждую пару на слово и число.

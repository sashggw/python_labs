def _is_whitespace(ch: str) -> bool:
    return ch.isspace() # проверяет, состоит ли вся строка исключительно из пробельных символов


def _is_word_char(ch: str) -> bool:
    return ch.isalnum() or ch == "_" # проверяет, состоит ли строка только из букв и/или цифр

#--------------------NORMALIZE--------------------
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


# print("----------normalize----------")
# print(f'"ПрИвЕт\\nМИр\\t" → "{normalize("ПрИвЕт\nМИр\t")}"')
# print(f'"ёжик, Ёлка" → "{normalize("ёжик, Ёлка")}"')
# print(f'"Hello\\r\\nWorld" → "{normalize("Hello\r\nWorld")}"')
# print(f'"  двойные   пробелы  " → "{normalize("  двойные   пробелы  ")}"')


#--------------------TOKENIZE--------------------
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


# print("----------tokenize----------")
# print(f'"привет мир" → {tokenize("привет мир")}')
# print(f'"hello,world!!!" → {tokenize("hello,world!!!")}')
# print(f'"по-настоящему круто" → {tokenize("по-настоящему круто")}')
# print(f'"2025 год" → {tokenize("2025 год")}')
# print(f'"emoji 😀 не слово" → {tokenize("emoji 😀 не слово")}')


#--------------------COUNT_FREQ--------------------
def count_freq(tokens: list[str]) -> dict[str, int]:
    if not isinstance(tokens, list): 
        raise ValueError("ожидался список (list), получено: " + type(tokens).__name__) # проверка на принадлежность к определённому классу

    freq = {}
    for tok in tokens:
        if tok in freq: freq[tok] = freq[tok] + 1
        else: freq[tok] = 1
    return freq


#--------------------TOP_N--------------------
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not isinstance(freq, dict):
        raise ValueError("ожидался словарь (dict), получено: " + type(freq).__name__) # проверка на принадлежность к определённому классу
    if not isinstance(n, int):
        raise ValueError("ожидалось целое число (int), получено: " + type(n).__name__) # проверка на принадлежность к определённому классу
    if n <= 0: return []

    pairs = list(freq.items())
    pairs = sorted(pairs, key=lambda p: p[0])        
    pairs = sorted(pairs, key=lambda p: p[1], reverse=True) 
    return pairs[:n]


# print("----------count_freq + top_n----------")
# print(f'["a","b","a","c","b","a"] → {count_freq(["a","b","a","c","b","a"])}')
# print(f'top_n(freq, n=2) → {top_n({"a":3,"b":2,"c":1}, n=2)}')
# print(f'["bb","aa","bb","aa","cc"] → {count_freq(["bb","aa","bb","aa","cc"])}')
# print(f'top_n(freq, n=2) → {top_n({"aa":2,"bb":2,"cc":1}, n=2)}')
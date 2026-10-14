"""Тесты для src/lib/text.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.text import normalize, tokenize, count_freq, top_n

print("----------normalize----------")
print(f'"ПрИвЕт\\nМИр\\t" → "{normalize("ПрИвЕт\nМИр\t")}"')
print(f'"ёжик, Ёлка" → "{normalize("ёжик, Ёлка")}"')
print(f'"Hello\\r\\nWorld" → "{normalize("Hello\r\nWorld")}"')
print(f'"  двойные   пробелы  " → "{normalize("  двойные   пробелы  ")}"')

print("----------tokenize----------")
print(f'"привет мир" → {tokenize("привет мир")}')
print(f'"hello,world!!!" → {tokenize("hello,world!!!")}')
print(f'"по-настоящему круто" → {tokenize("по-настоящему круто")}')
print(f'"2025 год" → {tokenize("2025 год")}')
print(f'"emoji 😀 не слово" → {tokenize("emoji 😀 не слово")}')

print("----------count_freq + top_n----------")
print(f'["a","b","a","c","b","a"] → {count_freq(["a","b","a","c","b","a"])}')
print(f'top_n(freq, n=2) → {top_n({"a":3,"b":2,"c":1}, n=2)}')
print(f'["bb","aa","bb","aa","cc"] → {count_freq(["bb","aa","bb","aa","cc"])}')
print(f'top_n(freq, n=2) → {top_n({"aa":2,"bb":2,"cc":1}, n=2)}')
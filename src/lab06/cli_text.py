"""CLI-утилиты для работы с текстом (ЛР6)."""
import argparse
import sys
from pathlib import Path

# Подключаем пути, чтобы видеть функции из ЛР3
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.text import normalize, tokenize, count_freq, top_n

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

def cmd_stats(args):
    """Анализ частот слов (аналог stats)."""
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input}", file=sys.stderr)
        sys.exit(1)

    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{args.top}:")
    for word, count in top_n(freq, args.top):
        print(f"{word}: {count}")

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты для текста")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Подкоманда cat
    parser_cat = subparsers.add_parser("cat", help="Вывести содержимое файла")
    parser_cat.add_argument("--input", required=True, help="Путь к файлу")
    parser_cat.add_argument("-n", action="store_true", help="Нумеровать строки")
    parser_cat.set_defaults(func=cmd_cat)

    # Подкоманда stats
    parser_stats = subparsers.add_parser("stats", help="Частоты слов")
    parser_stats.add_argument("--input", required=True, help="Путь к файлу")
    parser_stats.add_argument("--top", type=int, default=5, help="Сколько слов вывести")
    parser_stats.set_defaults(func=cmd_stats)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
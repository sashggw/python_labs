from __future__ import annotations
import argparse
import sys
from pathlib import Path

# Делаем доступными и src/ (для lib.text), и src/lab04/ (для io_txt_csv),
# чтобы скрипт работал при запуске из корня репозитория.
_HERE = Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parent.parent))   # src/
sys.path.insert(0, str(_HERE.parent))          # src/lab04/

from lib.text import normalize, tokenize, count_freq, top_n  # noqa: E402
from io_txt_csv import read_text, write_csv, ensure_parent_dir  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Считает частоты слов в тексте и сохраняет отчёт в CSV.",
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
    rows = sorted_word_counts(freq)

    ensure_parent_dir(args.output_path)
    write_csv(rows, args.output_path, header=("word", "count"))

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
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
"""CLI-конвертеры данных (ЛР6)."""
import argparse
import sys
from pathlib import Path

# Подключаем пути для импорта функций ЛР5
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # JSON -> CSV
    p1 = sub.add_parser("json2csv", help="Конвертировать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV")
    
    # CSV -> JSON
    p2 = sub.add_parser("csv2json", help="Конвертировать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON")

    # CSV -> XLSX
    p3 = sub.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX")

    args = parser.parse_args()

    try:
        if args.cmd == "json2csv": json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json": csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx": csv_to_xlsx(args.input, args.output)
        print(f"Успешно: {args.input} -> {args.output}")
    except Exception as e:
        print(f"Ошибка конвертации: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
"""Модуль конвертации JSON ↔ CSV (ЛР5)."""
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    """Преобразует JSON (список словарей) в CSV."""
    p_in = Path(json_path)
    p_out = Path(csv_path)
    
    with p_in.open("r", encoding="utf-8") as f:
        data = json.load(f)
        
    if not isinstance(data, list) or not data: raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(item, dict) for item in data): raise ValueError("JSON должен содержать список словарей")
        
    # Собираем все уникальные ключи
    fieldnames = []
    for item in data:
        for key in item.keys():
            if key not in fieldnames: fieldnames.append(key)
                
    p_out.parent.mkdir(parents=True, exist_ok=True)
    
    with p_out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    """Преобразует CSV в JSON (список словарей)."""
    p_in = Path(csv_path)
    p_out = Path(json_path)
    
    with p_in.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None: raise ValueError("В CSV отсутствует заголовок")
            
        data = [row for row in reader]
        
    if not data: raise ValueError("Пустой CSV")
        
    p_out.parent.mkdir(parents=True, exist_ok=True)
    
    with p_out.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
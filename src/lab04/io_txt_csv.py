from __future__ import annotations
import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории для ``path``, если их нет."""
    p = Path(path)
    parent = p.parent
    if parent and not parent.exists(): parent.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    rows = list(rows)
    if rows:
        widths = {len(r) for r in rows}
        if len(widths) > 1: raise ValueError(f"Строки имеют разную длину: {sorted(widths)}")
    p = Path(path)
    ensure_parent_dir(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None: w.writerow(header)
        for r in rows: w.writerow(r)
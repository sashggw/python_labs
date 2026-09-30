#/////////////////////////////FORMAT_RECORD///////////////////////////////////////////

def format_record(rec: tuple[str, str, float]) -> str:

    if rec.__class__!= tuple:
        raise TypeError("был введен не кортеж")

    if len(rec)<3:
        raise TypeError("не достаточно данных")

    fio, group, gpa = rec

    if group.__class__ != str:
        raise TypeError("не правильный формат группы")
    if fio.__class__ != str:
        raise TypeError("не правильный формат ФИО")
    if gpa.__class__ != int and gpa.__class__ != float:
        raise TypeError("не правильный формат gpa")

    slova = fio.split()
    if len(slova) < 2:
        raise ValueError("Слишком короткое ФИО")
    if not group.strip():
        raise ValueError("пустая группа")

    familia = slova[0].capitalize()

    initialy = ""
    for imya in slova[1:3]:
        initialy += imya[0].upper() + "."

    return f"{familia} {initialy}, гр. {group.strip()}, GPA {gpa:.2f}"

print("format_record")
print(f'("Иванов Иван Иванович", "BIVT-25", 4.6)→{format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}')
print(f'("Петров Пётр", "IKBO-12", 5.0)→{format_record(("Петров Пётр", "IKBO-12", 5.0))}')
print(f'("Петров Пётр Петрович", "IKBO-12", 5.0)→{format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}')
print(f'("  сидорова  анна   сергеевна ", "ABB-01", 3.999)→{format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}')
print(f'("Иван", "", "4.6")→{format_record(("Иван", "", "4.6"))}')
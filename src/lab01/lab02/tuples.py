def format_record(rec: tuple[str, str, float]) -> str:

    if rec.__class__!= tuple:
        raise TypeError("Был введен не кортеж")

    if len(rec)<3:
        raise TypeError("Было введено не достаточно данных")

    fio, group, gpa = rec

    if group.__class__ != str:
        raise TypeError("Был введён не правильный формат группы")
    if fio.__class__ != str:
        raise TypeError("Был введён не правильный формат ФИО")
    if gpa.__class__ != int and gpa.__class__ != float:
        raise TypeError("Был введён не правильный формат gpa")

    fio_parts = fio.split()
    if len(fio_parts) < 2:
        raise ValueError("Было введено слишком короткое ФИО")
    if not group.strip():
        raise ValueError("Была введена пустая группа")

    surname = fio_parts[0].capitalize()

    initials = ""
    for name in fio_parts[1:3]:
        initials += name[0].upper() + "."

    return f"{surname} {initials}, гр. {group.strip()}, GPA {gpa:.2f}"
# print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
# print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
# print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
# print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

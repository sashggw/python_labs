full_name = input("ФИО: ")

parts = full_name.split()
initials = "".join([part[0].upper() for part in parts])
or_len = len(full_name)
clean_len = len(full_name.replace(" ", ""))
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {clean_len}")
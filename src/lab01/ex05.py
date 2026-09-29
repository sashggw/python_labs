full_name = " ".join(str(input("ФИО:")).split())
parts = full_name.split()
initials = "".join([part[0].upper() for part in parts])
print(f"Инициалы: {initials}.")
<<<<<<< HEAD
print(f"Длина (символов): {len(full_name)}")
=======
print(f"Длина (символов): {len(full_name)}")
>>>>>>> 7300b1aabe4b04674a4740c96c571eba44e63971

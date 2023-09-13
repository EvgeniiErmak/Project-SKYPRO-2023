employees = [
 {"fio": "Киселёв Всеволод Эдуардович", "vaccinated": True},
 {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
 {"fio": "Аверин Мартын Егорович", "vaccinated": True},
 {"fio": "Князева Августа Егоровна", "vaccinated": False},
 {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
 {"fio": "Куприна Марина Викторовна", "vaccinated": False},
 {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []

def workers():
    for worker in employees:
        if worker["vaccinated"] == True:
            vaccinated.append(worker["fio"])
        else:
            not_vaccinated.append(worker["fio"])


workers()

print(f"Вакцинированные:")
for new_worker in vaccinated:
    print(new_worker)

print(f"Остальные:")
for new_worker in not_vaccinated:
    print(new_worker)
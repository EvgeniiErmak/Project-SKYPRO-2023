import json

def load_students():
    """
    Загрузка студентов из файла
    """
    with open("students.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_professions():
    """
    Загузка профессий из файла
    """
    with open("professions.json", "r", encoding="utf-8") as file1:
        data = json.load(file1)
    return data


def get_student_by_pk(pk):
    """
    Получаем словарь с данными студента по его pk
    """
    students = load_students()
    for student in students:
        if student.get("pk") == pk:
            return student
    return None


def get_profession_by_title(title):
    """
    Получаем словарь с информацией о профессии по названию
    """
    professions = load_professions()
    for profession in professions:
        if profession.get("title") == title:
            return profession
    return None


def check_fitness(student, profession):
    """
    Получив имя студента и профессию, возвращает словарь
    """
    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])
    has_skills = student_skills.intersection(profession_skills)
    lacks_skills = profession_skills - student_skills
    fit_percent = len(has_skills)/ len(profession_skills)*100
    return{
        "has": list(has_skills),
        "lacks": list(lacks_skills),
        "fit_percent": fit_percent
    }

def main ():
    """
    Основная программа
    """
    while True:
        print("Введите номер студента")
        number_student = int(input())
        student = get_student_by_pk(number_student)
        if student:
            print (f'Студент {student["full_name"]}')
            print (f"Знает {', '.join (student['skills'])}")
        else:
            print("У нас нет такого студента")
            continue

        print (f'Выберите специальность для оценки студента {student["full_name"]}')
        profession_title = input().title()
        profession = get_profession_by_title(profession_title)
        if profession:
            result = check_fitness(student, profession)
            print (f'Пригодность: {result["fit_percent"]}%')
            print (f'{student["full_name"]} знает {", ".join(result["has"])}')
            print (f'{student["full_name"]} не знает {", ".join(result["lacks"])}')
        else:
            print ("У нас нет такой специальности")
        break

if __name__=="__main__":
    main()
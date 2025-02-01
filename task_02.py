# class Teacher:
#     def __init__(self, first_name, last_name, age, email, can_teach_subjects):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = email
#         self.can_teach_subjects = set(can_teach_subjects)
#         self.assigned_subjects = set()


# def create_schedule(subjects, teachers):
#     remaining_subjects = set(subjects)
#     assigned_teachers = []

#     while remaining_subjects:
#         best_teacher = None
#         max_new_subjects = 0

#         for teacher in teachers:
#             new_subjects = teacher.can_teach_subjects & remaining_subjects
#             if len(new_subjects) > max_new_subjects or (len(new_subjects) == max_new_subjects and teacher.age < (
#             best_teacher.age if best_teacher else float('inf'))):
#                 best_teacher = teacher
#                 max_new_subjects = len(new_subjects)

#         if not best_teacher:
#             print("Неможливо покрити всі предмети наявними викладачами.")
#             return None

#         best_teacher.assigned_subjects = best_teacher.can_teach_subjects & remaining_subjects
#         remaining_subjects -= best_teacher.assigned_subjects
#         assigned_teachers.append(best_teacher)

#     return assigned_teachers


# if __name__ == '__main__':
#     subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
#     teachers = [
#         Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
#         Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
#         Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
#         Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
#         Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
#         Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"})
#     ]

#     schedule = create_schedule(subjects, teachers)

#     if schedule:
#         print("Розклад занять:")
#         for teacher in schedule:
#             print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
#             print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
#     else:
#         print("Неможливо покрити всі предмети наявними викладачами.")


class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)  
    assigned_teachers = []

   
    while remaining_subjects:
        best_teacher = None
        max_new_subjects = 0

      
        sorted_teachers = sorted(teachers, key=lambda t: (-len(t.can_teach_subjects & remaining_subjects), t.age))

        for teacher in sorted_teachers:
            new_subjects = teacher.can_teach_subjects & remaining_subjects
            if len(new_subjects) > max_new_subjects:
                best_teacher = teacher
                max_new_subjects = len(new_subjects)

       
        if not best_teacher:
            print("❌ Неможливо покрити всі предмети наявними викладачами!")
            return None

      
        best_teacher.assigned_subjects = best_teacher.can_teach_subjects & remaining_subjects
        remaining_subjects -= best_teacher.assigned_subjects
        assigned_teachers.append(best_teacher)

    return assigned_teachers


if __name__ == '__main__':
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("\n✅ Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("❌ Неможливо покрити всі предмети наявними викладачами!")

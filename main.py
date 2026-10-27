def main():
    students = []
    teachers = []
    supervisors = []

    while True:
        cmd = input("Enter command (create, manage, end): ").strip().lower()

        if cmd == "create":
            while True:
                sub_cmd = input(
                    "Creation (student, teacher, supervisor, end): ").strip().lower()
                if sub_cmd == "end":
                    break
                elif sub_cmd == "student":
                    name = input("Enter student's first and last name: ")
                    student_class = input("Enter class name (e.g., 3C): ")
                    students.append({"name": name, "class": student_class})
                elif sub_cmd == "teacher":
                    name = input("Enter teacher's first and last name: ")
                    subject = input("Enter subject name: ")
                    classes = []
                    print("Enter class names (empty line to finish):")
                    while True:
                        c = input()
                        if not c:
                            break
                        classes.append(c)
                    teachers.append(
                        {"name": name, "subject": subject, "classes": classes})
                elif sub_cmd == "supervisor":
                    name = input("Enter supervisor's first and last name: ")
                    student_class = input("Enter managed class name: ")
                    supervisors.append({"name": name, "class": student_class})
                else:
                    print("Unknown option.")

        elif cmd == "manage":
            while True:
                sub_cmd = input(
                    "Management (class, student, teacher, supervisor, end): ").strip().lower()
                if sub_cmd == "end":
                    break
                elif sub_cmd == "class":
                    target_class = input("Enter class name (e.g., 3C): ")
                    print(f"\n--- Students of class {target_class} ---")
                    found_students = [s["name"]
                                      for s in students if s["class"] == target_class]
                    if found_students:
                        for s in found_students:
                            print(f"- {s}")
                    else:
                        print("No students found in this class.")

                    print("--- Class Supervisor ---")
                    supervisor = next(
                        (sup["name"] for sup in supervisors if sup["class"] == target_class), None)
                    if supervisor:
                        print(f"- {supervisor}")
                    else:
                        print("No supervisor assigned to this class.")
                    print()
                elif sub_cmd == "student":
                    target_student = input(
                        "Enter student's first and last name: ")
                    student_obj = next(
                        (s for s in students if s["name"].lower() == target_student.lower()), None)
                    if not student_obj:
                        print("Student not found.\n")
                        continue

                    student_class = student_obj["class"]
                    print(
                        f"\n--- Lessons and teachers for student {target_student} (class {student_class}) ---")
                    found = False
                    for t in teachers:
                        if student_class in t["classes"]:
                            print(
                                f"Subject: {t['subject']}, Teacher: {t['name']}")
                            found = True
                    if not found:
                        print("No assigned lessons for this class.")
                    print()
                elif sub_cmd == "teacher":
                    target_teacher = input(
                        "Enter teacher's first and last name: ")
                    teacher_obj = next(
                        (t for t in teachers if t["name"].lower() == target_teacher.lower()), None)
                    if not teacher_obj:
                        print("Teacher not found.\n")
                        continue

                    print(
                        f"\n--- Classes taught by teacher {target_teacher} ---")
                    for c in teacher_obj["classes"]:
                        print(f"- {c}")
                    print()
                elif sub_cmd == "supervisor":
                    target_supervisor = input(
                        "Enter supervisor's first and last name: ")
                    sup_obj = next((sup for sup in supervisors if sup["name"].lower(
                    ) == target_supervisor.lower()), None)
                    if not sup_obj:
                        print("Supervisor not found.\n")
                        continue

                    sup_class = sup_obj["class"]
                    print(
                        f"\n--- Students managed by supervisor {target_supervisor} (class {sup_class}) ---")
                    found_students = [s["name"]
                                      for s in students if s["class"] == sup_class]
                    if found_students:
                        for s in found_students:
                            print(f"- {s}")
                    else:
                        print("No students found in this class.")
                    print()
                else:
                    print("Unknown option.")

        elif cmd == "end":
            print("Exiting program.")
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()

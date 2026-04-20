students = {
    "S001": ("Бат", 20, "Компьютерын ухаан"),
    "S002": ("Болд", 21, "Программ хангамж")
}
def add_student(student_id, name, age, major):
    students[student_id] = (name, age, major)
    print("added successfully.")
    print(students[student_id])


def find_student_by_id(student_id):
    print(f"searching for student with id {student_id}")
    for student in students:
        if student == student_id:
            print(students[student_id])
            return
    print("Student not found")
    

def list_students_by_major(major):
    print(f"listing all students of {major} major")
    # Тодорхой хөтөлбөрийн бүх оюутнуудыг жагсаах
    for student in students:
        if students[student][2] == major:
            print(students[student])

def count_students():
    # Нийт оюутны тоог тоолох
    print("counting all students...")
    print(f"there are  {len(students)} students")
def main():
    add_student("S003", "Уянга", 22, "Компьютерын ухаан")
    find_student_by_id("S002") # Гаралт: ("Болд", 21, "Программ хангамж")
    list_students_by_major("Компьютерын ухаан") # Гаралт: [("Бат", 20, "Компьютерын ухаан), ("Уянга", 22, "Компьютерын ухаан")]
    count_students() # Гаралт: 3

if __name__ == "__main__":
    main()
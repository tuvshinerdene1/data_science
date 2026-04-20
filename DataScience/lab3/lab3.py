# computing and data science lab3 tuvshin-erdene 23b1num0869

import json

with open("schedule.json", "r", encoding="utf-8") as file:
    data = json.load(file)

teacher_course_count = {}
autumn_courses = []
spring_courses = []

for entry in data:
    name = entry["zaasan_bagshiin_ner"]
    if name in teacher_course_count:
        teacher_course_count[name] += 1
    else:
        teacher_course_count[name] = 1

    if entry["uliral"] == "Намрын улирал":
        if not entry["khicheeliin_ner"] in autumn_courses:
            autumn_courses.append(entry["khicheeliin_ner"])
    else:
        if not entry["khicheeliin_ner"] in spring_courses:
            spring_courses.append(entry["khicheeliin_ner"])



print("autumn only courses: ")
for course in autumn_courses:
    if not course in spring_courses:
        print(f"{course}\n")
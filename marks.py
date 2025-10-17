students_profile = {
    "name" : 'Manoj',
    "Subjects" : { 
        "Math" : 95,
        "science" : 90,
        "Computer" : 100
    }
}

def operations():
    # simple operation: print the student's profile
    print("Student Name:", students_profile.get("name"))
    print("Subjects and scores:")
    for subject, score in students_profile.get("Subjects", {}).items():
        print(f"  {subject}: {score}")

if __name__ == "__main__":
   while True:
        list_op = ("1 - Total of a student", "2 - Average mark of a student")
        for list in list_op:
            print(list)
        lv_op = int(input("Enter operations"))
        if lv_op == 1:
            lv_name = students_profile.get("name")
            lv_total = 0 
            for subject, score in students_profile.get("Subjects", {}).items():
                lv_total += score 

            print(f"Total Mark of a Student: {lv_name} is {lv_total}")
        elif lv_op == 2:
            lv_name = students_profile.get("name")
            subjects = students_profile.get("Subjects", {})
            lv_total = sum(subjects.values())
            lv_avg = lv_total / len(subjects)
            print(f"Average Mark of a Student: {lv_name} is {lv_avg:.2f}")
        else:
            break


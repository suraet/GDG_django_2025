a=input("the name ")
def get_grade(student_grade , student_name):
    try:
        return student_grade[student_name]
    except:
        return "student name dont found"
test_grade = {
    "surafel" : "B"
}
print(get_grade(test_grade,a))
s1_name = "Ayush"
s1_marks = 92
s1_attendance = 94


s2_name = "Arpit"
s2_marks = 98
s2_attendance = 91

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    else:
        return "C"
    
def update_marks(old_marks, new_marks):
    return new_marks

print("Student: ", s1_name)
print("Marks: ", s1_marks)
print("Grade: ", calculate_grade(s1_marks))
print("Attendance: ", s1_attendance)
print()

print("Student: ", s2_name)
print("Marks: ", s2_marks)
print("Grade: ", calculate_grade(s2_marks))
print("Attendance: ", s2_attendance)
print()

s1_marks = update_marks(s1_marks, 99)
print("After update")
print("Student: ", s1_name)
print("Marks: ", s1_marks)
print("Grade: ", calculate_grade(s1_marks))
print("Attendance: ", s1_attendance)
print()

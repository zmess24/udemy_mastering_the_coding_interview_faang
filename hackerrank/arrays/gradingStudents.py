def gradingStudents(grades):
    rounded = []
    for grade in grades:
        remainder = 5- (grade % 5)
        if grade < 38 or grade % 5 == 0:
            rounded.append(grade)
        elif remainder < 3:
            new_grade = grade + remainder
            rounded.append(new_grade)
        else:
            rounded.append(grade)
    
    return rounded
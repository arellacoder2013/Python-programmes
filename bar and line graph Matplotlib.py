import matplotlib.pyplot as  mplt
students_names=["Ella", "Matthew", "Catherine","Alicia","Tom","Ben","Isabelle","Krystal"]
students_marks=[35,32,20,45,25,40,23,12]

marks_perc = []
for x in students_marks:
    res =(x/50)*100
    marks_perc.append(res)
print(marks_perc)

def marks_line_chart():
    mplt.plot(students_names,students_marks)
    mplt.title("Students Marks Graph")
    mplt.xlabel("students Name")
    mplt.ylabel("Student Marks")
    mplt.show()

marks_line_chart()

def percentage_bar_chart():
    mplt.bar(students_names,marks_perc)
    mplt.title("Students' Percentage Graph")
    mplt.xlabel("Student Names")
    mplt.ylabel("Students Percentage")
    mplt.show()

percentage_bar_chart()
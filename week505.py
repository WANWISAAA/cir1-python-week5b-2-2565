mark = -1
mark = int(input("enter score: "))
if mark>=80 and mark<80:
    print(mark,": GRADE is A")
elif mark >= 70 and mark < 80:
    print(mark,": GRADE is B")
elif mark >= 60 and mark < 70:
    print(mark,": GRADE is C")
elif mark >= 50 and mark < 60:
    print(mark,": GRADE is D")
elif mark >= 40 and mark < 50:
    print(mark,": GRADE is F")
else :
    print(mark,": GRADE is ERROR")
    
totalgrades=int(input("Enter the units registered for this semester: "))
grade=[]
for i in range(0,totalgrades,1):
    grade=int(input("Enter the marks for the units registered this semester: "))
    if grade>90:
        print("You scored an A")
    elif grade<90 and grade>80:
        print("You scored an A-")
    elif grade<80 and grade>=70:
        print("You scored a B+")
    elif grade<70 and grade>=60:
        print("You scored a B")
    elif grade<60 and grade>=50:
        print("You scored a B-")
else:
    print("You failed")
for i in range(0,totalgrades,1):
    print(grade)
prelim = float(input("Enter your Preliminary Period Grade: "))
midterm = float(input("Enter your Midterm Period Grade: "))
final = float(input("Enter your Final Period Grade: "))

if prelim < 40.0 or prelim > 100.0:
    print("Error, your grade must stay between 40 and 100.")
elif midterm < 40.0 or midterm > 100.0:
    print("Error, your grade must stay between 40 and 100.")
elif final < 40.0 or final > 100.0:
    print("Error, your grade must stay between 40 and 100.")
else:
    #the calculation of the grades
    final_grade = (prelim * (1/3)) + (midterm * (1/3)) + (final * (1/3))

    #the grades and it's corresponding status
    if final_grade >= 99.0 and final_grade <= 100.0:
        GPA = 1.00
        status = "Excellent"
    elif final_grade >= 96.0 and final_grade < 99.0:
        GPA = 1.25
        status = "Outstanding"
    elif final_grade >= 93.0 and final_grade < 96.0:
        GPA = 1.50
        status = "Superior"
    elif final_grade >= 90.0 and final_grade < 93.0:
       GPA = 1.75
        status = "Very Good"
    elif final_grade >= 87.0 and final_grade < 90.0:
        GPA = 2.00
        status = "Good"
    elif final_grade >= 84.0 and final_grade < 87.0:
        GPA = 2.25
        status = "Satisfactory"
    elif final_grade >= 81.0 and final_grade < 84.0:
        GPA = 2.50
        status = "Fairly Satisfactory"
    elif final_grade >= 78.0 and final_grade < 81.0:
        GPA = 2.75
        status = "Fair"
    elif final_grade >= 75.0 and final_grade < 78.0:
        GPA = 3.00
        status = "Passed"
    else:
        grade = 5.00
        status = "Failed"
    #final output
    print(f"Final Grade: {final_grade:.2f}")
    print(f"Your GPA: {GPA}")
    print(f"Status: {status}")

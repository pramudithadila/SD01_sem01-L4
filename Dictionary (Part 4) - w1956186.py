# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1956186
# Date: 2022.11.28

# Creating the dictionary
studentIdDict = {}

done = True

while done:
    try:
        # Validation of Student ID
        student_id = str(input("Please enter your student ID (ID format - w1234567): "))
        student_id = student_id.lower()
        id_num = student_id[1:]
        if len(student_id) != 8:
            print('Enter a valid student ID (Format - w1234567)')
            continue
        elif student_id[0] != 'w':
            print('Enter a valid student ID (Format - w1234567)')
            continue
        else:
            try:
                id_num = int(id_num)
            except:
                print('Enter a valid student ID (Format - w1234567)')
                continue
    except:
        print("Enter a valid student ID (Format - w1234567)")
        continue

    # Using 3 while loops for validation of pass, defer and fail credits
    while True:
        try:
            pass_mark = int(input("Please enter your credits at pass: "))
            if pass_mark > 120 or pass_mark < 0:
                print("Out of range")
                continue
            if pass_mark % 20 != 0:
                print("Out of range")
                continue
            break
        except:
            print("Integer required")
            continue

    while True:
        try:
            defer_mark = int(input("Please enter your credits at defer: "))
            if defer_mark > 120 or defer_mark < 0:
                print("Out of range")
                continue
            if defer_mark % 20 != 0:
                print("Out of range")
                continue
            break
        except:
            print("Integer required")
            continue

    while True:
        try:
            fail_mark = int(input("Please enter your credits at fail: "))
            if fail_mark > 120 or fail_mark < 0:
                print("Out of range")
                continue
            if fail_mark % 20 != 0:
                print("Out of range")
                continue
            break
        except:
            print("Integer required")
            continue

    if pass_mark + defer_mark + fail_mark != 120:
        print("Total incorrect")
        continue

    # Selecting the progression outcome for the relevant set of pass, defer and fail credits
    # Adding the set of credits of each student for the dictionary
    if pass_mark == 120:
        print("Progress")
        studentIdDict[student_id] = ("Progress -", pass_mark, defer_mark, fail_mark)
    elif pass_mark == 100:
        print("Progress(module trailer)")
        studentIdDict[student_id] = ('Progress(module trailer) -', pass_mark, defer_mark, fail_mark)
    elif fail_mark >= 80:
        print("Exclude")
        studentIdDict[student_id] = ('Exclude -', pass_mark, defer_mark, fail_mark)
    else:
        print("Do not Progress - module retriever")
        studentIdDict[student_id] = ('Do not Progress - module retriever -', pass_mark, defer_mark, fail_mark)

    # Asking the user for enter another set of credits or not
    while done:
        print('Would you like to enter another set of data?')
        response = str(input('Enter \'y\' for yes or \'q\' to quit and view results: '))
        if response == 'y':
            break
        elif response == 'q':
            done = False
        else:
            print('Please enter a valid input!')

print('''

''')

# Printing out the dictionary
i = 1
for x, y in studentIdDict.items():
    print(i)
    print(x, '=', y)
    i += 1

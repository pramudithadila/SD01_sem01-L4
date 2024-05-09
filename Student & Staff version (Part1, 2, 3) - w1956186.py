# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1956186
# Date: 2022.11.28

# All variables assigned.
progress = 0
trailer = 0
retriever = 0
exclude = 0
total = 0

# Lists made for the Part 2.
progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []
done = True

# Creating a function for print the lists and write the text file.
def checkList(listType, gradeType):
    for i in listType:
        listString = str(i)
        listString = listString[1:-1]
        print(gradeType, listString)
        with open('studentDetails.txt', 'a') as file:
            file.write(gradeType + listString + '\n')

# Asking the user for logging as a student or logging as a staff member
print("If you are a student, please enter 'student'")
typeResponse = input("If you are a staff member, please enter 'staff': ")
typeResponse = typeResponse.lower()

# Start of student version
if typeResponse == 'student':
    while done:
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
        if fail_mark >= 80:
            print("Exclude")
        elif pass_mark == 120:
            print("Progress")
        elif pass_mark == 100:
            print("Progress(module trailer)")
        else:
            print("Do not Progress - module retriever")
        break

# Start of Staff version
elif typeResponse == 'staff':
    while done:
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

        # Creating lists for each student
        progressStudent = []
        trailerStudent = []
        retrieverStudent = []
        excludeStudent = []

        if pass_mark + defer_mark + fail_mark != 120:
            print("Total incorrect")
            continue

        # Selecting the progression outcome for the relevant set of pass, defer and fail credits
        if fail_mark >= 80:
            print("Exclude")
            excludeStudent.extend([pass_mark, defer_mark, fail_mark])
            exclude_list.append(excludeStudent)
            exclude += 1
        elif pass_mark == 120:
            print("Progress")
            progressStudent.extend([pass_mark, defer_mark, fail_mark])
            progress_list.append(progressStudent)
            progress += 1
        elif pass_mark == 100:
            print("Progress(module trailer)")
            trailerStudent.extend([pass_mark, defer_mark, fail_mark])
            trailer_list.append(trailerStudent)
            trailer += 1
        else:
            print("Do not Progress - module retriever")
            retrieverStudent.extend([pass_mark, defer_mark, fail_mark])
            retriever_list.append(retrieverStudent)
            retriever += 1
        total += 1

        # Asking the user for enter another set of credits or not
        while done:
            print('Would you like to enter another set of data?')
            response1 = str(input('Enter \'y\' for yes or \'q\' to quit and view results: '))
            print()
            response = response1.lower()
            if response == 'y':
                break
            elif response == 'q':
                # Creating Histogram
                print('Histogram is calculating')
                print()
                print('-'*50)
                print('Histogram')
                print()
                print('Progress', progress, ':', progress * '*')
                print('Trailer', trailer, ':', trailer * '*')
                print('Retriever', retriever, ':', retriever * '*')
                print('Excluded', exclude, ':', exclude * '*')
                print()
                print(total, 'outcomes in total')
                print('-'*50)
                done = False
            else:
                print('Please enter a valid input!')

    # Creating the Text file
    file = open('studentDetails.txt', 'w')
    file.close()

    # Calling the function
    checkList(progress_list, 'Progress - ')
    checkList(trailer_list, 'Progress (module trailer) - ')
    checkList(retriever_list, 'Module retriever - ')
    checkList(exclude_list, 'Exclude - ')


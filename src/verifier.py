file = open("../data/generated.in") # Name of input file goes here
n = file.readline() # Read n from first line
if n == "":
    print("Error! Input missing n")
    exit() # Terminate if file is empty
else:
    n = int(n)
hospital_lists = []
for i in range(1, n + 1): # Read hospital preference lists from next n lines
    line = file.readline()
    if line == "":
        print("Error! Input missing hospital line", i)
        exit()
    hospital_lists.append(line.split())
student_lists = []
for i in range(1, n + 1): # Read student preference lists from next n lines
    line = file.readline()
    if line == "":
        print("Error! Input missing student line", i)
        exit()
    student_lists.append(line.split())

file = open("../data/generated.out") # Name of output file goes here
matchings = {}
for i in range(0, n): # Read matchings from the next n lines
    line = file.readline()
    if line == "":
        print("Error! Missing line", i)
        exit()
    try:
        matchings[int(line.split()[0])] = int(line.split()[1]) # Create dictionary of matchings
    except IndexError: # If hospital has empty matching
        print(f"INVALID: Hospital {line.split()[0]} not matched!")
        exit()

for i in range(1, n): # Compares each hospital with all the others to see if there are any duplicate matchings
    for j in range(i + 1, n + 1):
        if matchings[i] == matchings[j]:
            print(f"INVALID: Hospital {i} and {j} have the same assignment!")

'''
The verifier will check each hospital's preference list, if they would prefer a different student than their
current matching, go through that student's preference list and see if they would prefer the previously mentioned
hospital over their current matching. If this is the case, then we have a blocking pair.
'''
for i in range(0, n): # Iterates through each hospital
    for j in range(0, n): # Go through each hospital's preference list
        if int(hospital_lists[i][j]) == matchings[i + 1]:
            break # If hospital reaches their current matching on their preference list, break
        else: # Else iterate through the corresponding student's preference list
            current_student = int(hospital_lists[i][j]) - 1
            for k in range(0, n):
                if matchings[int(student_lists[current_student][k])] - 1 == current_student:
                    break # If student reaches their current matching, break
                elif int(student_lists[current_student][k]) == i + 1: # Else check if current preference is the current hospital in the loop
                    blocking_pair = f"Hospital {i + 1} and student {current_student + 1} would prefer each other!"
                    print(f"UNSTABLE: {blocking_pair}")
                    exit()
print("VALID STABLE")
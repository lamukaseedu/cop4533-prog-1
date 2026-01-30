file = open("../data/example.in") # Name of input file goes here
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

matches = {} # Dictionary matching hospitals to students; only contains matched hospitals
choices = {key: 0 for key in range(1, n + 1)} # Dictionary keeping track of the index on each hospital's preference list
hospital = 1 # Number of the hospital currently iterated to
while (len(matches) < n): # Iterate as long as there is an unmatched hospital
  if not hospital in matches.keys(): # If the current hospital is not matched, try to match the next student on its preference list
    student = int(hospital_lists[hospital - 1][choices[hospital]])
    if not student in matches.values(): # If student is not currently matched, make a match
      matches[hospital] = student
    else: # If the student is matched, make a match if they prefer the current hospital to their current match
      current_match = [h for h, s in matches.items() if s == student][0]
      for preference in student_lists[student - 1]:
        if int(preference) == hospital: # If current hospital is first in the preference list
          matches[hospital] = student
          matches.pop(current_match) # Remove old match
          break
        elif int(preference) == current_match: # If student's current match is first, do nothing
          break
      choices[hospital] += 1 # Go to hospital's next preference
  hospital += 1 # Iterate to next hospital
  if hospital == n + 1:
    hospital = 1

with open("../data/example.out", "w") as file: # Name of output file goes here
  for h in range(1, n + 1):
    s = matches[h]
    file.write(str(h) + " " + str(s)) # Write hospital and matched student combination
    if (h != n):
      file.write("\n")
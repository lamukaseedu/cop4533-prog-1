file = open("example.in") # Name of input file goes here
n = int(file.readline()) # Read n from first line
hospital_lists = []
for i in range(0, n): # Read hospital preference lists from next n lines
  hospital_lists.append(file.readline().split())
student_lists = []
for i in range(0, n): # Read student preference lists from next n lines
  student_lists.append(file.readline().split())

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
      for preference in student_lists[student]:
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

print(matches)
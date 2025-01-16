"""This program prompts user for the number of students and group size.
Displays how many groups will be needed and how many will be left over."""

# Input: Number of students from user.
total_students = int(input("How many students? "))

# Input: Get the group size from the user.
total_groups = int(input("Required group size? "))

# Calculate the number of groups.
group_size = total_students // total_groups

# Calculate the number of students left over.
leftover_students = total_students % total_groups

# Output with correct grammer.
if group_size == 1:
    group_text = "group"
else:
    group_text = "groups"

if leftover_students <= 1:
    leftover_text = "student"
else:
    leftover_text = "students"

print(f"There will be {group_size} {group_text} with {leftover_students} {leftover_text} left over.")


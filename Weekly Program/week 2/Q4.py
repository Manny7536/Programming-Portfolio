""" This program prompts the user for total count of sweets and pupil.
It then calculates the number of sweets each pupil will get and leftover if any.
Displays how many sweets to give to each pupil, and how many she will have left over. """

# Input: Total count of sweets.
total_sweets = int(input("How many sweets are in the tub? "))

# Input: Total count of pupils.
total_pupils = int(input("How many pupils are attending today? "))

# Calculate the number of sweets each pupil will get.
sweets_per_pupil = total_sweets // total_pupils

# Calculate the number of sweets left over.
leftover_sweets = total_sweets % total_pupils

# Output with correct grammer.
if sweets_per_pupil <=1:
    sweet_text = "sweet"
else:
    sweet_text = "sweets"

if leftover_sweets <=1:
    leftover_text = "sweet"
else:
    leftover_text = "sweets"

#Check if the total number of sweets is less than the total number of pupils.
if total_sweets < total_pupils:
    print("There will not be enough sweets for everyone attending today.")
else:
    print(f"Each pupil will get {sweets_per_pupil} {sweet_text} and there will be {leftover_sweets} {leftover_text} left over.")

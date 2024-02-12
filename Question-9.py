"""9.Define a function that accepts roll number and returns whether the student is present or absent."""


def check_attendance(roll_number):
    # List of roll numbers representing absent students
    x = [6,2,33,48,22,15,50,10]

    # Check if the provided roll number is in the list of absent students
    if roll_number in x:
        print(f"Roll number {roll_number} is absent")
    else:
        print(f"Roll number {roll_number} is present")

# Get roll number input from the user
roll_number = int(input("Enter roll no:"))
check_attendance(roll_number) # Call the check_attendance function 


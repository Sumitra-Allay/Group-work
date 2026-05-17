# Starting empty list to store selected names
selected_students = [] #creating empty list

# Try to open the file named students.txt 
# If there isn't try creating another one
try:
    file = open("students.txt", "r") #open students.txt
except FileNotFoundError: #if not "FileNotFoundError"
    file = open("..\students.txt", "r") #Opening students.txt

with file: #use "with" to close file
    # Read every line from the file into a list of lines
    lines = file.readlines() #read it from lines

    # Loop the lines
    for line in lines[1:]: #Loop it

        # Remove the extra line
        line = line.strip() #Use line.strip

        if not line: #see if line empty
            # Skip empty lines if there is
            continue #Use continue

        # Split the line if necessary
        data = line.split() 
        if len(data) < 3:
            # Skip any lines that do not have at least three columns
            continue

        # Skip the heading row if it appears again
        if data[0].lower().startswith("sl.no"):
            continue

        # The first piece is the serial number
        serial_number = data[0].strip()
        # The middle pieces are the student's name
        student_name = " ".join(data[1:-1]).strip()
        # The last piece is the student ID
        student_id = data[-1].strip()

        # Convert the student ID from text to a number
        try:
            sid = int(student_id)
        except ValueError:
            # Skip rows where the ID is not a valid number
            continue

        # Only keep students whose ID is an odd number
        if sid % 2 != 0:
            selected_students.append([serial_number, student_name, sid])

# Sort the selected students by their student ID number
selected_students.sort(key=lambda x: x[2])

# Print how many students were selected
print("Total Students in Group 7:", len(selected_students))

print("\nSelected Students:")

# Print each selected student's name and ID
for student in selected_students:
    print(student[1], "-", student[2])

if selected_students:
    # Print the first student after sorting by ID
    print("\nFirst Student According to Student ID:")
    print(selected_students[0][1], "-", selected_students[0][2])

    # Print the last student after sorting by ID
    print("\nLast Student According to Student ID:")
    print(selected_students[-1][1], "-", selected_students[-1][2])
else:
    # If no odd-ID students were found, show a message
    print("\nNo students found with an odd student ID.")

# Save the selected student records into a new file
with open("group_7.txt", "w") as output_file:
    output_file.write("Serial Number,Student Name,Student ID\n")
    for student in selected_students:
        output_file.write(f"{student[0]},{student[1]},{student[2]}\n")

print("\nData has been stored in group_7.txt") 
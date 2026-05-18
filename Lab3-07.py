import os

# Starting empty list to store selected names
selected_students = []

# Check which file exists and open it
if os.path.exists("students.txt"):
    file = open("students.txt", "r")
elif os.path.exists("../students.txt"):
    file = open("../students.txt", "r")
else:
    print("students.txt file not found.")
    exit()

# Read every line from the file into a list
lines = file.readlines()

# Close the file manually
file.close()

# Loop through the lines
for line in lines[1:]:

    # Remove extra spaces and newline
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Split the line
    data = line.split()

    # Skip invalid rows
    if len(data) < 3:
        continue

    # Skip heading row if repeated
    if data[0].lower().startswith("sl.no"):
        continue

    # Extract data
    serial_number = data[0].strip()
    student_name = " ".join(data[1:-1]).strip()
    student_id = data[-1].strip()

    # Check if student ID is a valid number
    if not student_id.isdigit():
        continue

    sid = int(student_id)

    # Check if ID is odd
    if sid % 2 != 0:
        selected_students.append([serial_number, student_name, sid])

# Sort students by ID
selected_students.sort(key=lambda x: x[2])

# Print total students
print("Total Students in Group 7:", len(selected_students))

print("\nSelected Students:")

# Print selected students
for student in selected_students:
    print(student[1], "-", student[2])

if selected_students:
    print("\nFirst Student According to Student ID:")
    print(selected_students[0][1], "-", selected_students[0][2])

    print("\nLast Student According to Student ID:")
    print(selected_students[-1][1], "-", selected_students[-1][2])
else:
    print("\nNo students found with an odd student ID.")

# Save data into a new file
output_file = open("group_7.txt", "w")

output_file.write("Serial Number,Student Name,Student ID\n")

for student in selected_students:
    output_file.write(f"{student[0]},{student[1]},{student[2]}\n")

# Close the output file manually
output_file.close()

print("\nData has been stored in group_7.txt")
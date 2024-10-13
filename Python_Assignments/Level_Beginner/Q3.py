def calculate_grade(marks):
    # Calculate total and percentage
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100  # Total marks for 5 subjects is 500

    # Determine the grade based on percentage
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 40:
        grade = 'E'
    else:
        grade = 'F'

    return percentage, grade

# Main function to input marks
def main():
    subjects = ["Physics", "Chemistry", "Biology", "Mathematics", "Computer"]
    marks = []

    # Input marks for each subject
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (out of 100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Calculate percentage and grade
    percentage, grade = calculate_grade(marks)

    # Print the results
    print(f"\nTotal Marks: {sum(marks)} / 500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

# Run the main function
if __name__ == "__main__":
    main()

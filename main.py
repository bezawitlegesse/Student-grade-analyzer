# Student Grade Analyzer

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


subjects = {}

print("=== Student Grade Analyzer ===")

while True:
    subject = input("Enter a subject (or type 'done' to finish): ")

    if subject.lower() == "done":
        break

    while True:
        try:
            mark = float(input(f"Enter the mark for {subject} (0-100): "))

            if 0 <= mark <= 100:
                subjects[subject] = mark
                break
            else:
                print("Please enter a mark between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

if subjects:
    average = sum(subjects.values()) / len(subjects)
    highest_subject = max(subjects, key=subjects.get)
    lowest_subject = min(subjects, key=subjects.get)

    print("\n=== Results ===")

    for subject, mark in subjects.items():
        print(f"{subject}: {mark:.1f}")

    print(f"\nAverage: {average:.2f}")
    print(f"Grade: {get_grade(average)}")
    print(f"Highest: {highest_subject} ({subjects[highest_subject]:.1f})")
    print(f"Lowest: {lowest_subject} ({subjects[lowest_subject]:.1f})")

else:
    print("No subjects were entered.")

'''
**************************************************
 STUDENT GRADING SYSTEM USING OOP
 *************************************************
 '''

class Student:
    def __init__(self, name, Reg_number):
        self.name = name
        self.Reg_number = Reg_number
        self.tests = []
        self.quizzes = []
        self.assignments = []

    def calculate_total_mark(self):
        # Extract the highest score from each category
        best_test = max(self.tests)
        best_quiz = max(self.quizzes)
        best_assignment = max(self.assignments)
        
        # Calculate and return the average
        return (best_test + best_quiz + best_assignment) / 3

def get_valid_score(prompt):
    # Helper function to ensure user input is a valid number between 0 and 100
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input: Please enter a numeric value.")

def main():
    print("--- Student Grading System ---")
    
    # 1. Enter student name
    name = input("Enter the student's name: ").strip()

    # 2. Enter student registration number
    Reg_number = input("Enter the student's registration number: ").strip()
    student = Student(name, Reg_number)

    
    print(f"\nEntering marks for {student.name} (Out of 100):")
    
    # 3. Enter 2 Test marks
    for i in range(1, 3):
        mark = get_valid_score(f"Enter mark for Test {i}: ")
        student.tests.append(mark)
        
    # 4. Enter 2 Quiz marks
    for i in range(1, 3):
        mark = get_valid_score(f"Enter mark for Quiz {i}: ")
        student.quizzes.append(mark)
        
    # 5. Enter 2 Assignment marks
    for i in range(1, 3):
        mark = get_valid_score(f"Enter mark for Assignment {i}: ")
        student.assignments.append(mark)
        
    # 6. Calculate final results
    final_score = student.calculate_total_mark()

    if final_score >= 80:
        print("GRADE: A")

    elif final_score >= 79:
        print("GRADE: B+")

    elif final_score >=74:
        print("GRADE: B")

    elif final_score >= 69:
        print("GRADE: C")

    elif final_score >= 64:
        print("GRADE: D")

    elif final_score >= 55:
        print("GRADE: E")

    else:
        print("GRADE: F")

    
    
    # 7. Display the formatted output
    print("\n" + "="*35)
    print(f" STUDENT'S NAME: {student.name.upper()}")
    print(f"REG. NUNMBER: {student.Reg_number}")
    print("="*35)
    print(f" Best Test:       {max(student.tests):.2f}")
    print(f" Best Quiz:       {max(student.quizzes):.2f}")
    print(f" Best Assignment: {max(student.assignments):.2f}")
    print("-" * 35)
    print(f" FINAL TOTAL MARK:{final_score:.2f}")
    print(f" GRADE SCORE: {'A' if final_score >= 80 else 'B+' if final_score >= 75 else "B" if final_score >= 74 else 'C' if final_score >= 69 else 'D' if final_score >= 64 else 'E' if final_score >= 55 else 'F' }")
    print("="*35)

if __name__ == "__main__":
    # Execute the demonstration script
    main()
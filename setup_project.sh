#!/bin/bash
echo "Setting up project environment..." 
mkdir -p src data output
echo "Directories created" 

cat > data/students.csv <<EOL
name,age,grade,subject
George,15,100,Math
Hannah,14,98,Science
Alice,16,86,History
Jane,15,70,English
Gal,16,100,Math
Ariel,17,95,Science
Kathy,15,99,History
EOL
echo "students.csv created with sample data"

cat > src/data_analysis.py <<EOL
# data_analysis.py
# TODO: implement main entry point

def main():
    # TODO: implement program logic
    pass

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Basic Data Analysis Script"""


#TODO: Load data into my script from CSV

def load_students(file_path):
    """Load student data from a CSV file."""
    import csv
    students = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['age'] = int(row['age'])
                row['grade'] = int(row['grade'])
                students.append(row)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return students

    # TODO: Open file, read lines, skip header
    # TODO: Split each line by comma
    # TODO: Return list of student data

    lines = [ln.strip() for ln in lines if ln.strip()]
    if not lines:
        return []

    students = []
    for line in lines[1:]:  
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 4:
            continue
        name, age_s, grade_s, subject = parts[:4]

        try:
            age = int(age_s)
        except ValueError:
            age = None
        try:
            grade = float(grade_s)
        except ValueError:
            grade = 0.0
        students.append({"name": name, "age": age, "grade": grade, "subject": subject})
    return students

    pass

def calculate_average_grade(students):
    """Return average grade as a float; uses only numeric grades."""
    grades = [s["grade"] for s in students if isinstance(s.get("grade"), (int, float))]
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

    """Calculate average grade."""
    # TODO: Sum all grades
    # TODO: Divide by number of students
    pass

def count_math_students(students):
    """Count students whose subject is Math (case-insensitive)."""
    return sum(1 for s in students if str(s.get("subject", "")).strip().lower() == "math")
    # TODO: Count students where subject is Math
    pass

def find_highest_grade(students):
    grades = [s["grade"] for s in students if isinstance(s.get("grade"), (int, float))]
    if not grades:
        return 0.0
    return max(grades) if grades else 0.0 
    #TODO: Find highest grade
    pass

def generate_report():
    """Create the formatted report string."""
    students = load_students(CSV_PATH)
    total_students = len(students)
    average = calculate_average_grade(students)
    math_count = count_math_students(students)
    highest_grade = find_highest_grade(students)

    # Who has the highest grade?
    top_students = [
        s["name"]
        for s in students
        if isinstance(s.get("grade"), (int, float)) and s["grade"] == highest_grade
    ]

    # Count students by subject (all subjects)
    by_subject = {}
    for s in students:
        subj = (s.get("subject") or "Unknown").strip() or "Unknown"
        by_subject[subj] = by_subject.get(subj, 0) + 1

    lines = []
    lines.append("Student Analysis Report")
    lines.append("=" * 30)
    lines.append(f"Total students: {total_students}")
    lines.append(f"Average grade: {average:.1f}")   # .1f formatting as required
    lines.append(f"Highest grade: {highest_grade:.1f} (by: {', '.join(top_students) if top_students else 'N/A'})")
    lines.append(f"Math students: {math_count}")
    lines.append("")
    lines.append("Counts by subject:")
    for subj in sorted(by_subject.keys()):
        lines.append(f"  {subj}: {by_subject[subj]}")
    return "\n".join(lines)
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    pass

def save_report(report, filename):
    out_dir = os.path.dirname(filename) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    # TODO: Create output directory if needed
    # TODO: Write report to file
    pass

def main():
    report = generate_report()
    save_report(report, "output/analysis_report.txt")
    print("Report written to output/analysis_report.txt")
    # TODO: Load data
    # TODO: Calculate statistics
    # TODO: Generate and save report
    pass

if __name__ == "__main__":
    main()


EOL

cat > src/data_analysis_function.py <<EOL
# data_analysis_function.py

from pathlib import Path 
from data_analysis import () 
# TODO: Begin by loading data from data_analysis.py, did not want to repeat loading of data 
pass

def analyze_grade_distribution(grades):
    """Analyze the distribution of grades."""
    if not grades:
        return {}

    distribution = {
        'A (90-100)': 0,
        'B (80-89)': 0,
        'C (70-79)': 0,
        'D (60-69)': 0,
        'F (0-59)': 0
    }

    for g in grades:
        if g >= 90:
            distribution['A (90-100)'] += 1
        elif g >= 80:
            distribution['B (80-89)'] += 1
        elif g >= 70:
            distribution['C (70-79)'] += 1
        elif g >= 60:
            distribution['D (60-69)'] += 1
        else:
            distribution['F (0-59)'] += 1

    return distribution             
# TODO: Grade distribution analysis function by letter grade buckets 
pass

def find_top_performers(students, threshold=90):
    """Find students who scored above a threshold."""
    return [s for s in students if s.get('grade', 0) >= threshold]
#TODO: Top performers function
pass

def generate_detailed_report(students, filename):
    """Generate a comprehensive analysis report."""
    if not students:
        print("No data to analyze")
        return False
#TODO: Generate comprehensive report function
pass

    grades = [float(s['grade']) for s in students]

    average = calculate_average_grade(students)
    highest = find_highest_grade(students)       
    lowest  = min(grades) if grades else 0.0

    distribution = analyze_grade_distribution(grades)
    top_performers = find_top_performers(students, 90)

    try:
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("COMPREHENSIVE STUDENT ANALYSIS REPORT\n")
            file.write("=" * 50 + "\n\n")

            file.write(f"Report generated on: "
                       f"{__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # Basic stats
            file.write("BASIC STATISTICS\n")
            file.write("-" * 20 + "\n")
            file.write(f"Total students: {len(students)}\n")
            file.write(f"Average grade: {average:.1f}\n")
            file.write(f"Highest grade: {highest:.1f}\n")
            file.write(f"Lowest grade: {lowest:.1f}\n")
            file.write(f"Grade range: {(highest - lowest):.1f}\n\n")

            # Grade distribution (counts + percentages)
            file.write("GRADE DISTRIBUTION\n")
            file.write("-" * 20 + "\n")
            for bucket, count in distribution.items():
                pct = (count / len(students)) * 100 if students else 0.0
                file.write(f"{bucket}: {count} students ({pct:.1f}%)\n")
            file.write("\n")

            # Top performers
            file.write("TOP PERFORMERS (90+)\n")
            file.write("-" * 20 + "\n")
            if top_performers:
                for s in top_performers:
                    file.write(f"{s['name']}: {s['grade']:.1f} ({s['subject']})\n")
            else:
                file.write("No students scored 90 or above\n")
            file.write("\n")

            # Individual records
            file.write("INDIVIDUAL STUDENT RECORDS\n")
            file.write("-" * 30 + "\n")
            for s in students:
                file.write(f"Name: {s['name']}\n")
                file.write(f"  Age: {s['age']}\n")
                file.write(f"  Grade: {float(s['grade']):.1f}\n")
                file.write(f"  Subject: {s['subject']}\n\n")

        print(f"Detailed report saved to {filename}")
        return True
    except Exception as e:
        print(f"Error generating report: {e}")
        return False
    #TODO: Basics stats, grade distribution, top performers, individual records
    pass

def main():
    print("Advanced Student Analysis - Module Usage")
    print("=" * 45)

    students = load_students('data/students.csv')
    if not students:
        print("No data loaded. Please check data/students.csv")
        return

    print(f"Loaded {len(students)} students")

    average = calculate_average_grade(students)
    highest = find_highest_grade(students)
    print(f"Average grade: {average:.1f}")
    print(f"Highest grade: {highest:.1f}")

    # Grade distribution
    grades = [float(s['grade']) for s in students]
    distribution = analyze_grade_distribution(grades)
    print("\nGrade Distribution:")
    for bucket, count in distribution.items():
        pct = (count / len(students)) * 100
        print(f"{bucket}: {count} students ({pct:.1f}%)")

    # Top performers
    top_performers = find_top_performers(students, 90)
    print(f"\nTop Performers (90+): {len(top_performers)} students")
    for s in top_performers:
        print(f"  {s['name']}: {float(s['grade']):.1f} ({s['subject']})")

    # Write the comprehensive report
    generate_detailed_report(students, 'output/analysis_modular_report.txt')

    basic_report_text = generate_report()                 
    save_report(basic_report_text, 'output/analysis_report.txt')

    print("\n✅ Advanced analysis complete!")

if __name__ == "__main__":
    main()
#TODO: Main function to demonstrate module usage
pass



EOL

echo "Python template files created"

echo "Project environment setup complete!"

#End of shell script!

chmod +x scripts/process_data.sh


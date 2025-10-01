# data_analysis.py
# TODO: implement main entry point

def main():
    # TODO: implement program logic
    pass

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Student Grade Analysis - Function Version
"""

import os

# Use a relative path so scripts work on CI and across platforms
CSV_PATH = "data/students.csv"

def load_students(file_path):
    """Read CSV using open() + readlines(), split by commas, return list of student dicts."""
    try:
        with open(file_path, "r", encoding="utf-8", newline="") as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"[ERROR] File not found: {file_path}")

    # Remove blanks, keep header, skip it later
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


def calculate_average_grade(students):
    """Return average grade as a float; uses only numeric grades."""
    grades = [s["grade"] for s in students if isinstance(s.get("grade"), (int, float))]
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def calculate_average_age(students):
    """Return average age as a float; uses only numeric grades."""
    ages = [s["age"] for s in students if isinstance(s.get("age"), (int, float))]
    if not ages:
        return 0.0
    return sum(ages) / len(ages)


def count_math_students(students):
    """Count students whose subject is Math (case-insensitive)."""
    return sum(1 for s in students if str(s.get("subject", "")).strip().lower() == "math")

def find_highest_grade(students):
    grades = [s["grade"] for s in students if isinstance(s.get("grade"), (int, float))]
    if not grades:
        return 0.0
    return max(grades) if grades else 0.0   


def generate_report():
    """Create the formatted report string."""
    students = load_students(CSV_PATH)
    total_students = len(students)
    average = calculate_average_grade(students)
    age_average = calculate_average_age(students)
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
    lines.append(f"Average age: {age_average:.1f}")
    lines.append(f"Highest grade: {highest_grade:.1f} (by: {', '.join(top_students) if top_students else 'N/A'})")
    lines.append(f"Math students: {math_count}")
    lines.append("")
    lines.append("Counts by subject:")
    for subj in sorted(by_subject.keys()):
        lines.append(f"  {subj}: {by_subject[subj]}")
    return "\n".join(lines)



def save_report(report, filename):
    out_dir = os.path.dirname(filename) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)


def main():
    report = generate_report()
    save_report(report, "output/analysis_report.txt")
    print("Report written to output/analysis_report.txt")


if __name__ == "__main__":
    main()

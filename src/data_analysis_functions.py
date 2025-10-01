#!/usr/bin/env python3
"""Merged advanced analysis and compatibility wrappers.

This single file contains the advanced analysis implementation plus the
compatibility wrapper functions expected by the tests: load_data,
analyze_data, save_results, and a main() entrypoint.
"""
from pathlib import Path
import os
import datetime

CSV_PATH = "data/students.csv"

# --- Basic data loading and helpers (from data_analysis) ---

def load_students(file_path=CSV_PATH):
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
    grades = [s.get("grade") for s in students if isinstance(s.get("grade"), (int, float))]
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def calculate_average_age(students):
    ages = [s.get("age") for s in students if isinstance(s.get("age"), (int, float))]
    if not ages:
        return 0.0
    return sum(ages) / len(ages)


def count_math_students(students):
    return sum(1 for s in students if str(s.get("subject", "")).strip().lower() == "math")


def find_highest_grade(students):
    grades = [s.get("grade") for s in students if isinstance(s.get("grade"), (int, float))]
    if not grades:
        return 0.0
    return max(grades)


def generate_report():
    """Create the formatted report string using current CSV data."""
    students = load_students(CSV_PATH)
    total_students = len(students)
    average = calculate_average_grade(students)
    age_average = calculate_average_age(students)
    math_count = count_math_students(students)
    highest_grade = find_highest_grade(students)

    top_students = [
        s["name"]
        for s in students
        if isinstance(s.get("grade"), (int, float)) and s["grade"] == highest_grade
    ]

    by_subject = {}
    for s in students:
        subj = (s.get("subject") or "Unknown").strip() or "Unknown"
        by_subject[subj] = by_subject.get(subj, 0) + 1

    lines = []
    lines.append("Student Analysis Report")
    lines.append("=" * 30)
    lines.append(f"Total students: {total_students}")
    lines.append(f"Average grade: {average:.1f}")
    lines.append(f"Average age: {age_average:.1f}")
    lines.append(f"Highest grade: {highest_grade:.1f} (by: {', '.join(top_students) if top_students else 'N/A'})")
    lines.append(f"Math students: {math_count}")
    lines.append("")
    lines.append("Counts by subject:")
    for subj in sorted(by_subject.keys()):
        lines.append(f"  {subj}: {by_subject[subj]}")
    return "\n".join(lines)

# --- Advanced modular implementation (previously in data_analysis_function) ---

def analyze_grade_distribution(grades):
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


def find_top_performers(students, threshold=90):
    return [s for s in students if s.get('grade', 0) >= threshold]


def generate_detailed_report(students, filename):
    if not students:
        print("No data to analyze")
        return False

    grades = [float(s['grade']) for s in students]
    average = calculate_average_grade(students)
    highest = find_highest_grade(students)
    lowest = min(grades) if grades else 0.0
    distribution = analyze_grade_distribution(grades)
    top_performers = find_top_performers(students, 90)

    try:
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("COMPREHENSIVE STUDENT ANALYSIS REPORT\n")
            file.write("=" * 50 + "\n\n")
            file.write(f"Report generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            file.write("BASIC STATISTICS\n")
            file.write("-" * 20 + "\n")
            file.write(f"Total students: {len(students)}\n")
            file.write(f"Average grade: {average:.1f}\n")
            file.write(f"Highest grade: {highest:.1f}\n")
            file.write(f"Lowest grade: {lowest:.1f}\n")
            file.write(f"Grade range: {(highest - lowest):.1f}\n\n")
            file.write("GRADE DISTRIBUTION\n")
            file.write("-" * 20 + "\n")
            for bucket, count in distribution.items():
                pct = (count / len(students)) * 100 if students else 0.0
                file.write(f"{bucket}: {count} students ({pct:.1f}%)\n")
            file.write("\n")
            file.write("TOP PERFORMERS (90+)\n")
            file.write("-" * 20 + "\n")
            if top_performers:
                for s in top_performers:
                    file.write(f"{s['name']}: {s['grade']:.1f} ({s['subject']})\n")
            else:
                file.write("No students scored 90 or above\n")
            file.write("\n")
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

# --- Compatibility wrapper functions expected by tests ---

def load_data(path='data/students.csv'):
    return load_students(path)


def analyze_data(students):
    if not students:
        return {}
    grades = [float(s.get('grade', 0)) for s in students]
    return {
        'average_grade': calculate_average_grade(students),
        'average_age': calculate_average_age(students),
        'highest_grade': find_highest_grade(students),
        'grade_distribution': analyze_grade_distribution(grades),
    }


def save_results(results, output_file='output/analysis_report.txt'):
    # Accept either a results dict or plain text
    if isinstance(results, dict):
        lines = ["Analysis Results", "================", ""]
        for k, v in results.items():
            lines.append(f"{k}: {v}")
        report = "\n".join(lines)
    else:
        report = str(results)
    save_report(report, output_file)
    return output_file


def save_report(report, filename):
    out_dir = os.path.dirname(filename) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)


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

    grades = [float(s['grade']) for s in students]
    distribution = analyze_grade_distribution(grades)
    print("\nGrade Distribution:")
    for bucket, count in distribution.items():
        pct = (count / len(students)) * 100
        print(f"{bucket}: {count} students ({pct:.1f}%)")

    top_performers = find_top_performers(students, 90)
    print(f"\nTop Performers (90+): {len(top_performers)} students")
    for s in top_performers:
        print(f"  {s['name']}: {float(s['grade']):.1f} ({s['subject']})")

    generate_detailed_report(students, 'output/analysis_modular_report.txt')

    basic_report_text = generate_report()
    save_report(basic_report_text, 'output/analysis_report.txt')

    print("\n✅ Advanced analysis complete!")


if __name__ == "__main__":
    main()


def load_data(path='data/students.csv'):
    """Load data from CSV and return list of student dicts.

    This is a small compatibility wrapper expected by the tests.
    """
    return load_students(path)


def analyze_data(students):
    """Perform a small analysis and return a dictionary of results.

    Tests only check that this function exists, but returning a useful
    dict allows further programmatic use.
    """
    return {
        'average_grade': calculate_average_grade(students),
        'average_age': calculate_average_age(students),
        'math_count': count_math_students(students),
        'highest_grade': find_highest_grade(students),
    }


def save_results(results, output_file='output/analysis_report.txt'):
    """Save a simple text representation of results to the given file.

    Uses the existing save_report utility for consistent behavior.
    """
    lines = ["Analysis Results", "================", ""]
    for k, v in results.items():
        lines.append(f"{k}: {v}")
    report = "\n".join(lines)
    save_report(report, output_file)
    return output_file

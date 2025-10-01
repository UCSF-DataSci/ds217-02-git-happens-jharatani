# data_analysis_function.py
# TODO: add helper functions here

#!/usr/bin/env python3
"""
Student Grade Analysis - Modular Function Version
"""
"""Compatibility wrapper expected by tests.

Re-exports the core functions from `data_analysis` and delegates a
`main()` entrypoint to the advanced module `data_analysis_function`.
"""
from data_analysis import (
    load_students,
    calculate_average_grade,
    calculate_average_age,
    count_math_students,
    find_highest_grade,
    generate_report,
    save_report,
)
from pathlib import Path
import data_analysis_function as _daf

__all__ = [
    'load_students',
    'calculate_average_grade',
    'calculate_average_age',
    'count_math_students',
    'find_highest_grade',
    'generate_report',
    'save_report',
    'main',
]


def main():
    """Delegate to the advanced analysis main() implementation.

    Tests look for a `def main():` symbol in this file, so expose a
    simple wrapper that calls the implementation in
    `data_analysis_function`.
    """
    return _daf.main()


if __name__ == '__main__':
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

def find_top_performers(students, threshold=90):
    """Find students who scored above a threshold."""
    return [s for s in students if s.get('grade', 0) >= threshold]

def generate_detailed_report(students, filename):
    """Generate a comprehensive analysis report."""
    if not students:
        print("No data to analyze")
        return False

    # grades list for distribution / min / max
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

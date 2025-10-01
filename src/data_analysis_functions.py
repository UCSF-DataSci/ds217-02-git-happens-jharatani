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

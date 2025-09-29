# DataSci Week 02 Integration Project

## Project Overview
This project demonstrates integration of Git workflows, CLI automation, and Python data processing.

## Project Structure
```
datasci-week02-integration/
├── README.md
├── .gitignore
├── requirements.txt
├── setup_project.sh
├── src/
│   ├── data_analysis.py
│   └── data_analysis_functions.py
├── data/
│   ├── students.csv
│   └── courses.json
└── output/
    └── analysis_report.txt
```

## Features
- **Project Scaffold**: Automated project setup with `setup_project.sh`
- **Data Processing**: Python scripts for student grade analysis
- **Git Workflow**: Feature branch development and merging

## Usage
1. Run `./setup_project.sh` to create project structure
2. Execute `python src/data_analysis.py` for basic analysis
3. Run `python src/data_analysis_functions.py` for advanced analysis

## Git Workflow
| Branch | Purpose | Status |
|--------|---------|--------|
| main | Production code | Active |
| feature/project-scaffold | CLI automation | Merged |
| feature/data-processing | Python analysis | Merged |
```

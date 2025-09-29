#!/bin/bash
echo "Setting up project environment..." 
mkdir -p src data output
echo "Directories created" 

cat > data/students.csv <<EOL
name, age, grade, subject
George, 15, 10, Math
Hannah, 14, 9, Science
Ian, 16, 11, History
Jane, 15, 10, English
Gal, 16, 11, Math
Ariel, 14, 12, Science
Kathy, 15, 11, History
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
EOL

cat > src/data_analysis_function.py <<EOL
# data_analysis_function.py
# TODO: add helper functions here
EOL

echo "Python template files created"

echo "Project environment setup complete!"




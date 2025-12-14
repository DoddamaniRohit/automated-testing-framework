import os
import csv

# Get the directory where this variables file lives
BASE_DIR = os.path.dirname(__file__)

# CSV is expected to be in the same folder as this file
csv_path = os.path.join(BASE_DIR, "students.csv")

STUDENTS = []
with open(csv_path, newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for r in reader:
        STUDENTS.append([r['name'], r['age'], r['course']])


# Demo change to trigger CI

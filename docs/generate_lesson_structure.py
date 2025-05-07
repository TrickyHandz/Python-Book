import csv
import os

BASE_PATH = "_lessons"  # Jekyll collection folder

def rename_existing_files(row, section_folder):
    correct_filename = row["filename"]
    expected_path = os.path.join(section_folder, correct_filename)

    # Skip if the correct file already exists
    if os.path.exists(expected_path):
        return

    # Try to find a misnamed file with matching title
    for file in os.listdir(section_folder):
        if file.endswith(".md") and file.startswith(f"{row['section']}-"):
            with open(os.path.join(section_folder, file), "r", encoding="utf-8") as f:
                content = f.read()
                if f'title: "{row["title"]}"' in content:
                    old_path = os.path.join(section_folder, file)
                    os.rename(old_path, expected_path)
                    print(f"Renamed: {file} -> {correct_filename}")
                    return

def create_new_file(row, section_folder):
    file_path = os.path.join(section_folder, row["filename"])

    # Skip if file already exists
    if os.path.exists(file_path):
        return

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"""---
section: {row['section']}
lesson: {row['lesson']}
sublesson: {row['sublesson']}
section_title: "{row['section_title']}"
title: "{row['title']}"
layout: lesson
---

# {row['title']}

<!-- Content goes here -->

""")
        print(f"Created: {row['filename']}")

# Main execution
with open("python_book_content_map.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        section_folder = os.path.join(BASE_PATH, f"section-{row['section']}")
        os.makedirs(section_folder, exist_ok=True)

        rename_existing_files(row, section_folder)
        create_new_file(row, section_folder)

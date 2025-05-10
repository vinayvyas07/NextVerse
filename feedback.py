
import csv
from pathlib import Path

def save_feedback(input_text, output_text, rating, file_path="feedback.csv"):
    path = Path(file_path)
    file_exists = path.exists()
    with open(path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Input", "Output", "Rating"])
        writer.writerow([input_text, output_text, rating])

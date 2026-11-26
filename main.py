"""Entry for make.fun "Your AI Therapist's Diagnosis" (u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
"""
import os

LINE = 'Diagnosis: chronic tab-hoarding with acute fear of closing anything. Prognosis: you will die with 47 tabs open.'

def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

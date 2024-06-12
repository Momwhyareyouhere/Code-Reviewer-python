import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def choose_file():
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if not file_path:
        messagebox.showinfo("No file selected", "Please select a Python file.")
        return None
    return file_path

def calculate_score(num_issues):
    """ Calculate a score out of 10 based on the number of issues found. """
    if num_issues == 0:
        return 10
    elif num_issues < 5:
        return 8
    elif num_issues < 10:
        return 6
    elif num_issues < 20:
        return 4
    elif num_issues < 50:
        return 2
    else:
        return 0

def review_code(file_path):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"Reviewing file: {file_path}")
    
    
    result = subprocess.run(['flake8', file_path], capture_output=True, text=True)
    issues = result.stdout.strip().split('\n')
    num_issues = len(issues) if issues[0] else 0
    
   
    score = calculate_score(num_issues)
    
    if num_issues == 0:
        print("No issues found. Score: 10/10 (Excellent)")
    else:
        print(f"Issues found: {num_issues}\n")
        print(result.stdout)
        print(f"Score: {score}/10")

def main():
    file_path = choose_file()
    if file_path:
        review_code(file_path)

if __name__ == "__main__":
    main()

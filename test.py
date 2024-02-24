import subprocess
import os

files = {
    "ex00": ["Hello.py", "output"],
    "ex01": ["format_ft_time.py", "output"],
    "ex02": ["tester.py", "output"],
    "ex03": ["tester.py", "output"],
    "ex04": ["tester.py", "output"],
}

current_dir = os.getcwd()

for directory, file_info in files.items():
    script_name, output_file_name = file_info
    os.chdir(current_dir)
    os.chdir(directory)
    with open(output_file_name, "w") as output_file:
        subprocess.run(["python3", script_name], stdout=output_file)

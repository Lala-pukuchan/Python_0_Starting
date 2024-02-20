import subprocess
import os

# Change the current working directory to 'ex00'
os.chdir('ex00')

# Execute the 'Hello.py' Python script and redirect the output to a file named 'output'
with open('output', 'w') as output_file:
    subprocess.run(['python3', 'Hello.py'], stdout=output_file)

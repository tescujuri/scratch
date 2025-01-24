import subprocess
import re

# List of commands to run
commands = [
blah blah
]

def run_commands(commands):
    for command in commands:
        try:
            print(f"Running command: {command}")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(result.stdout)
            
            # Extract transferred files from the output
            transferred_files = re.findall(r'upload: (.+?) to', result.stdout)
            if transferred_files:
                print("Transferred files:")
                for file in transferred_files:
                    print(file)
            else:
                print("No files were transferred.")
                
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running command: {command}")
            print(f"Return code: {e.returncode}")
            print(f"Error output: {e.stderr}")
        except Exception as e:
            print(f"An unexpected error occurred while running command: {command}")
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    run_commands(commands)

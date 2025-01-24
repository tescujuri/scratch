import subprocess
import re

# List of commands to run
commands = [
    r'aws s3 sync C:\Users\tescu\Downloads s3://j141701012025/downloads_01012025 --delete',
    r'aws s3 sync C:\Users\tescu\code s3://j141701012025/code_01012025 --delete',
    r'aws s3 sync C:\Users\tescu\Videos s3://j141701012025/videos_01012025 --delete',
    r'aws s3 sync C:\Users\tescu\AppData\Roaming\Thunderbird s3://j141701012025/thunderbird_01012025  --delete',
    r'aws s3 sync C:\Users\tescu\Documents s3://j141701012025/docs_01012025  --delete',
    r'aws s3 sync C:\Users\tescu\Pictures s3://j141701012025/pics_01012025 --delete',
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

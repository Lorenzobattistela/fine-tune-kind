import os
import subprocess

def gather_prompts(directory, command, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                file_command = command.replace("<FILE>", file_path)
                
                with open(file_path, 'r') as f:
                    content = f.read()
                
                final_command = file_command.replace("<REQ>", content)
                
                try:
                    result = subprocess.run(final_command, shell=True, check=True, capture_output=True, text=True)
                    print(f"Processed {file_path}")
                    print(result.stdout)
                except subprocess.CalledProcessError as e:
                    print(f"Error processing {file_path}: {e}")
                    print(e.output)

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    command = input("Enter the command with <FILE> and <REQ> placeholders: ")
    extension = input("Enter the file extension (e.g., .txt): ")
    
    gather_prompts(directory, command, extension)

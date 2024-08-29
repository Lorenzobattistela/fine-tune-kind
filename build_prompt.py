import json
import os

def build_prompt(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    prompt = content.split('<PROMPT>')[1].split('</PROMPT>')[0].strip()
    deps = content.split('<DEPS>')[1].split('</DEPS>')[0].strip()
    correct_answer = content.split('<CORRECT_ANSWER>')[1].split('</CORRECT_ANSWER>')[0].strip()

    messages = [
        {
            "role": "system",
            "content": f"You are an assistant specialized in Kind programming language. Use the following type definitions:\n\n{deps}"
        },
        {
            "role": "user",
            "content": prompt
        },
        {
            "role": "assistant",
            "content": correct_answer
        }
    ]

    return json.dumps({"messages": messages})

def process_directory(directory_path, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(directory_path, filename)
                result = build_prompt(file_path)
                outfile.write(result + '\n')

# Specify the directory containing the input files and the output file
input_directory = "./training_set"
output_file = "./output.jsonl"

process_directory(input_directory, output_file)
print(f"Processing complete. Output saved to {output_file}")

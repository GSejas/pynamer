import os
from file_processor import process_and_generate_new_file


def traverse_repository(repo_directory):
    """
    This function takes a repository directory as input, walks through the directory,
    and processes all Python files using the process_and_generate_new_file function.
    """
    for root, _, files in os.walk(repo_directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                process_and_generate_new_file(file_path)
                print("\n")

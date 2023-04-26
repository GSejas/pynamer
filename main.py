import argparse
from repository_traverser import traverse_repository

def main():
    """
    This function parses the command line arguments, gets the input directory, and
    calls the traverse_repository function with the repo directory as input.
    """
    parser = argparse.ArgumentParser(description="Rename Python files' assets in a repository.")
    parser.add_argument(
        "input_directory",
        type=str,
        help="Path to the directory containing the Python files to be processed.",
    )
    args = parser.parse_args()
    repo_directory = args.input_directory

    traverse_repository(repo_directory)


if __name__ == "__main__":
    main()

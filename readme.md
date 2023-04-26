## Code Renamer
Code Renamer is a Python tool that automatically renames classes, functions, and variables in a given directory containing Python files. The tool uses the Abstract Syntax Tree (AST) library to parse and modify the code before generating new files with the renamed assets.

# Installation
Ensure you have Python 3.6 or higher installed on your system.
Clone the repository:
```bash
git clone https://github.com/yourusername/code-renamer.git
```
Navigate to the project directory:
``` bash
cd code-renamer
```
Install the required dependencies:
``` bash
pip install -r requirements.txt
```
# Usage
Run the starter.bat file (Windows) or use the following command:
``` bash
python main.py path/to/your/repository
```
Replace path/to/your/repository with the path to the directory containing the Python files you want to process.

The tool will traverse the provided directory, process each Python file, and generate new files with the renamed assets. The new files will have the same name as the original files, but with a _renamed.py suffix.

# Example
Suppose you have the following Python file in your target directory (sample.py):

```python
class TestClass:
    def testMethod(self):
        test_variable = 10
```
After running Code Renamer, a new file named sample_renamed.py will be generated with the following content:

```python
class PascalCaseTestClass:
    def snake_case_testMethod(self):
        snake_case_test_variable = 10
```

# Contributing
Fork the repository on GitHub.
```bash
git clone https://github.com/yourusername/code-renamer.git
```
Create a new branch for your changes:
```bash
git checkout -b my-feature-branch
```
Make your changes and commit them with a descriptive message.

Push your changes to your fork:
```bash
git push origin my-feature-branch
```

Create a pull request on the original repository.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
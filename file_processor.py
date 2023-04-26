import ast
import astunparse
from rename_transformer import RenameTransformer
import os

def process_and_generate_new_file(filename):
    """
    This function takes a filename as input, reads its content, parses the content into an AST,
    visits the AST using the RenameTransformer instance, generates new source code from the
    modified AST, and writes the new code to a new file with a "_renamed.py" suffix.
    """
    with open(filename, "r", encoding="utf-8") as file:
        file_content = file.read()

    try:
        tree = ast.parse(file_content)
        transformer = RenameTransformer()
        new_tree = transformer.visit(tree)
        new_code = astunparse.unparse(new_tree)

        new_filename = os.path.splitext(filename)[0] + "_renamed.py"
        with open(new_filename, "w", encoding="utf-8") as new_file:
            new_file.write(new_code)
    except Exception as e:
        print(f"Error while parsing {filename}: {e}")

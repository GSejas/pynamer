import ast
import os


class RenameTransformer(ast.NodeTransformer):
    """
    This class inherits from ast.NodeTransformer and renames the nodes in the AST.
    The class renames function names to a snake_case format, class names to a PascalCase format,
    and variable names to a snake_case format.
    """

    def visit_FunctionDef(self, node):
        node.name = f"snake_case_{node.name}"
        return self.generic_visit(node)

    def visit_ClassDef(self, node):
        node.name = f"PascalCase{node.name}"
        return self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                target.id = f"snake_case_{target.id}"
        return self.generic_visit(node)

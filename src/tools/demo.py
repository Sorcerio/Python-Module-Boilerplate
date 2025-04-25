# PYTHON_BOILER_PLATE Demo Tool
# An example of using the `BaseTool` class to create a command line tool.

# MARK: Imports
import argparse

from .baseTool import BaseTool

# MARK: Classes
class DemoTool(BaseTool):
    """
    Demo tool for command line tools.
    """
    # Constants
    TOOL_NAME = "demo"
    TOOL_HELP = "Demo tool for command line tools."

    # Initializer
    def __init__(self, isA: bool):
        self.isA = isA

    # CLI Functions
    @staticmethod
    def setupParser(parser: argparse.ArgumentParser):
        """
        Sets up the given `parser` with arguments for this tool.

        parser: The parser to apply the arguments to.
        """
        # Add a demo argument
        parser.add_argument(
            "-d",
            "--demo",
            action="store_true",
            help="Run the demo."
        )

    @classmethod
    def fromArgs(cls, args: argparse.Namespace) -> "DemoTool":
        """
        Creates an instance of this tool from the given `args`.

        args: The parser arguments to create the tool from.

        Returns an instance of this tool.
        """
        return cls(args.demo)

    def run(self):
        """
        Runs the tool as configured.
        """
        print("Running demo tool!")
        print(f"Is A: {self.isA}")

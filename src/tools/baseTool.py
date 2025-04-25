# PYTHON_BOILER_PLATE Base Tool
# BaseTool definition for command line tools.

# MARK: Imports
import argparse

# MARK: Classes
class BaseTool:
    """
    Base class for command line tools.
    """
    # Constants
    TOOL_NAME = "base_tool"
    TOOL_HELP = "Base tool for command line tools."

    # CLI Functions
    @staticmethod
    def setupParser(parser: argparse.ArgumentParser):
        """
        Sets up the given `parser` with arguments for this tool.

        parser: The parser to apply the arguments to.
        """
        raise NotImplementedError("applyParserArgs() must be implemented in the subclass.")

    @classmethod
    def fromArgs(cls, args: argparse.Namespace) -> "BaseTool":
        """
        Creates an instance of this tool from the given `args`.

        args: The parser arguments to create the tool from.

        Returns an instance of this tool.
        """
        raise NotImplementedError("fromArgs() must be implemented in the subclass.")

    def run(self):
        """
        Runs the tool as configured.
        """
        raise NotImplementedError("run() must be implemented in the subclass.")

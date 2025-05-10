# PYTHON_BOILER_PLATE Base Tool
# BaseTool definition for command line tools.

# MARK: Imports
import argparse
from typing import Optional

from ..config import ConfigManager

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
        raise NotImplementedError("setupParser() must be implemented in the subclass.")

    @classmethod
    def fromArgs(cls, args: argparse.Namespace, config: Optional[ConfigManager]) -> "BaseTool":
        """
        Creates an instance of this tool from the given `args`.

        args: The parser arguments to create the tool from.
        config: The config manager to use for the tool or `None` if not present.

        Returns an instance of this tool.
        """
        raise NotImplementedError("fromArgs() must be implemented in the subclass.")

    def _run(self, args: argparse.Namespace, config: Optional[ConfigManager]):
        """
        Runs the tool as configured by the CLI.

        args: The parser arguments to create the tool from.
        config: The config manager to use for the tool or `None` if not present.
        """
        raise NotImplementedError("_run() must be implemented in the subclass.")

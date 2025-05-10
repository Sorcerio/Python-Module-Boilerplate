# PYTHON_BOILER_PLATE Command Line Interface
# Command line starter for PYTHON_BOILER_PLATE.

# MARK: Imports
import inspect
import importlib
import argparse
from pathlib import Path
from typing import Optional, Union

from .config import ConfigManager
from .tools.baseTool import BaseTool

# MARK: Constants
CONFIG_PATH: Optional[Union[str, Path]] = None # `None` to use default
SILENCE_MISSING_CONFIG = False

PY_FILE_BLACKLIST = [
    "__init__.py",
    "baseTool.py",
    "cli.py"
]

# MARK: Functions
def collectTools() -> list[BaseTool]:
    """
    Collects all tools in the current directory and subdirectories.

    Returns a list of `BaseTool` objects.
    """
    # Prepare list
    basePath = Path(__file__).parent
    tools: list[BaseTool] = []
    for pyFile in basePath.glob("**/*.py"):
        # Check blacklist
        if pyFile.name in PY_FILE_BLACKLIST:
            continue

        # Convert file path to module path
        pathRelative = pyFile.relative_to(basePath.parent).with_suffix("")
        pathModule = ".".join(pathRelative.parts)

        # Attempt import
        try:
            # Dynamically import the module
            module = importlib.import_module(pathModule)

            # Inspect module for classes derived from BaseTool
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, BaseTool) and (obj is not BaseTool):
                    tools.append(obj)
        except Exception as e:
            print(f"Error importing {pathModule} from '{pathRelative}': {e}")

    # Remove duplicates
    tools = list({tool.TOOL_NAME: tool for tool in tools}.values())

    # Order alphabetically
    tools.sort(key=lambda x: x.TOOL_NAME)

    return tools

def startCli():
    # Prepare parser
    parser = argparse.ArgumentParser(
        description="Command line interface for PYTHON_BOILER_PLATE.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Prepare command subparser group
    commandParsers = parser.add_subparsers(dest="command", title="commands")

    # Get the tools
    tools = collectTools()
    if len(tools) == 0:
        print("No tools found.")
        return

    # Build command parsers
    for tool in tools:
        # Create subparser for tool
        toolParser = commandParsers.add_parser(
            tool.TOOL_NAME,
            help=tool.TOOL_HELP,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        tool.setupParser(toolParser)

    # Parse args
    args = parser.parse_args()

    # Load config
    config: Optional[ConfigManager] = None
    try:
        config = ConfigManager()
    except FileNotFoundError as e:
        if not SILENCE_MISSING_CONFIG:
            print("Configuration file not found. If this is intentional, set `SILENCE_MISSING_CONFIG` to `True` in `cli.py`.")

    # Decide what tool to run
    if args.command is None:
        # No tool specified
        parser.print_help()
        return

    for tool in tools:
        if tool.TOOL_NAME == args.command:
            # Run the tool
            tool.fromArgs(args, config)._run(args, config)
            return

    # No tool found
    print(f"Tool '{args.command}' not found.\n")
    parser.print_help()

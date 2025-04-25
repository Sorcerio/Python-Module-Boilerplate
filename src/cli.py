# PYTHON_BOILER_PLATE Command Line Interface
# Command line starter for PYTHON_BOILER_PLATE.

# MARK: Imports
import inspect
import importlib
import argparse
from pathlib import Path

from .tools.baseTool import BaseTool

# MARK: Constants
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

    return tools

def startCli():
    # Prepare parser
    parser = argparse.ArgumentParser(
        description="Command line interface for PYTHON_BOILER_PLATE.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # > Tools Setup Start
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
    # > Tools Setup End

    # Parse args
    args = parser.parse_args()

    # > Tools Usage Start
    # Decide what tool to run
    if args.command is None:
        # No tool specified
        parser.print_help()
        return

    for tool in tools:
        if tool.TOOL_NAME == args.command:
            # Run the tool
            tool.fromArgs(args).run()
            return

    # No tool found
    print(f"Tool '{args.command}' not found.\n")
    parser.print_help()
    # > Tools Usage End

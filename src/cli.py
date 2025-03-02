# PYTHON_BOILER_PLATE Command Line Interface
# Command line starter for PYTHON_BOILER_PLATE.

# MARK: Imports
import argparse

# MARK: Functions
def startCli():
    # Prepare parser
    parser = argparse.ArgumentParser(
        description="Command line interface for PYTHON_BOILER_PLATE."
    )

    # Parse args
    args = parser.parse_args()

    # TODO: Function
    print(args)

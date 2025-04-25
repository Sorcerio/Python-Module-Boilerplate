# PYTHON_BOILER_PLATE

MODULE_DESCRIPTION

---

## PBP Instructions

1. Replace `MODULE_DESCRIPTION` with a description of your module's function.
1. Replace `PYTHON_BOILER_PLATE` in all files with the name of your project.
1. Replace `DEVELOPER_IDENTIFIER` with your name or other developer identifier.
    1. This is primarily for the [LICENSE.txt](./LICENSE.txt).
1. Decide if you want to use tools for this module:
    * **I *do* want to use tools:**
        1. Leave the rest of the package as is.
        1. Use [BaseTool](./src/tools/baseTool.py) as a super class for any tools you make.
        1. Implement the required methods from [BaseTool](./src/tools/baseTool.py) in any tools you make.
            * See [DemoTool](./src/tools/demo.py) for an example implementation of [BaseTool](./src/tools/baseTool.py).
        1. Delete [DemoTool](./src/tools/demo.py) as needed.
    * **I *do not* want to use tools:**
        1. Remove the [tools/](./src/tools/) directory.
        1. Open [cli.py](./src/cli.py) then:
            1. Remove `PY_FILE_BLACKLIST`.
            1. Remove `collectTools()`.
            1. Remove all code in `startCli()` between `Tools Setup Start` and `Tools Setup End`.
            1. Remove all code in `startCli()` between `Tools Usage Start` and `Tools Usage End`.
1. Remove this section from the README.
1. Implement additional functionality as needed

---

## Local Setup

1. Create a Python 3 virtual environment: `python -m venv .venv`
1. Enter the environment:
    * Windows: `.\.venv\Scripts\activate`
    * MacOS/Linux: `source .venv/bin/activate`
1. Install the requirements: `pip install -r requirements.txt`
1. View the help: `python start.py --help`

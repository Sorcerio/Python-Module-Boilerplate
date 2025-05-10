# Python Boiler Plate Setup

Python Boiler Plate is a module boilerplate with built-in CLI tool support using `argparse`.

To configure the boilerplate for your project follow these instructions:

1. Replace `MODULE_DESCRIPTION` with a description of your module's function.
1. Replace `PYTHON_BOILER_PLATE` in all files with the name of your project.
1. Replace `DEVELOPER_IDENTIFIER` with your name or other developer identifier.
    * This is primarily for the [LICENSE.txt](./LICENSE.txt).
1. Remove this section from the README.
1. Configure `config.toml` as needed.
    * Make sure not to commit any keys or private information!
1. Implement additional functionality as needed.

---

# PYTHON_BOILER_PLATE

MODULE_DESCRIPTION

---

## Local Setup

1. Create a Python 3.11 *or higher* virtual environment: `python -m venv .venv`
1. Enter the environment:
    * Windows: `.\.venv\Scripts\activate`
    * MacOS/Linux: `source .venv/bin/activate`
1. Install the requirements: `pip install -r requirements.txt`
1. View the help: `python start.py --help`

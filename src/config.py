# Config Manager
# Class to manage file-based configuration settings.

# MARK: Imports
import tomllib
from typing import Union, Optional, Any
from pathlib import Path

# MARK: Classes
class ConfigManager:
    """
    Class to manage file-based configuration settings.
    """
    # Initializer
    def __init__(self, configPath: Optional[Union[str, Path]] = None):
        """
        configPath: Path to the configuration file. If `None`, will attempt to load `config.toml` from the current working directory.
        """
        # Prep parameters
        self.path = (Path(configPath) if configPath else Path.cwd() / "config.toml").absolute()
        self.data = self._loadConfig()

    # Python Functions
    def __repr__(self) -> str:
        return f"ConfigManager(path={self.path.absolute()}, data={self.data})"

    def __str__(self) -> str:
        return self.__repr__()

    # Private Functions
    def _loadConfig(self) -> dict[str, Any]:
        """
        Load the configuration file.
        """
        # Check if the file exists
        if not self.path.exists():
            raise FileNotFoundError(f"Configuration file not found at: {self.path}")

        # Load the configuration file
        with open(self.path, "rb") as f:
            return tomllib.load(f)

    # Functions
    def get(self, *keys) -> Optional[Union[dict[str, Any], list[Any], Any]]:
        """
        Retrieve a value from the configuration using a sequence of `keys`.

        keys: A sequence of keys to traverse the configuration dictionary.

        Returns the value found at the specified `keys`.
        """
        # Go find it
        data = self.data

        for key in keys:
            if not isinstance(data, dict) or key not in data:
                raise KeyError(f"Key '{key}' not found in configuration.")
            data = data[key]

        return data

    # TODO: Implement writing once PEP gets around to supporting it (never)
    # def set(self, *keys, value):
    #     """
    #     Set a value in the configuration using a sequence of keys.

    #     keys: A sequence of keys to traverse the configuration dictionary.
    #     value: The value to set at the specified `keys`.
    #     """
    #     # Go find it and set it
    #     data = self.data

    #     for key in keys[:-1]:
    #         if key not in data or not isinstance(data[key], dict):
    #             data[key] = {}
    #         data = data[key]

    #     data[keys[-1]] = value

    # def save(self, toPath: Optional[Union[str, Path]] = None, overwrite: bool = False):
    #     """
    #     Save the current configuration to a file.

    #     toPath: Alternative path to save the configuration file. If `None`, will save to the original path.
    #     overwrite: If `True`, will overwrite the existing file. If `False`, will raise an error if the file already exists.
    #     """
    #     # Resolve the path
    #     if toPath:
    #         toPath = Path(toPath)
    #     else:
    #         toPath = self.path

    #     # Check if exists
    #     if toPath.exists() and not overwrite:
    #         raise FileExistsError(f"Config file already exists at: {toPath}")

    #     # Save the configuration file
    #     with open(self.path, "w") as f:
    #         tomllib. # Wow... this doesn't support this.

"""
load env
"""
import os
from dotenv import load_dotenv

load_dotenv(override=True)


class ConfigBase:
    """
    A base class for managing configuration settings using environment variables.

    Attributes:
        _config (dict): A dictionary to store configuration settings.
    """

    def __init__(self):
        """
        Initializes the ConfigBase instance and sets up the _config dictionary.
        """
        self._config = {}

    def _get_and_check_variable(self, key, cast):
        """
        Retrieves, checks, and casts environment variables.

        Args:
            key (str): The environment variable key.
            cast (type): The type to which the value should be cast.

        Returns:
            The value of the environment variable after casting it to the specified type.

        Raises:
            ValueError: If the environment variable is not set or if the value cannot be cast to the specified type.
        """
        value = os.getenv(key)
        if value is None:
            raise ValueError(f"Environment variable {key} is not set.")

        try:
            if cast is bool:
                return eval(value)
            return cast(value)
        except ValueError:
            raise ValueError(f"Environment variable {key}'s format is incorrect.")

    def __setattr__(self, name, value):
        """
        Sets an attribute and updates the _config dictionary with the environment variable value.

        Args:
            name (str): The name of the attribute.
            value (tuple): A tuple containing the environment variable key and the type to cast the value to.

        Raises:
            ValueError: If the environment variable is not set or if the value cannot be cast to the specified type.
        """
        if name != "_config":
            self._config[name] = value
            value = self._get_and_check_variable(value[0], value[1])
        super().__setattr__(name, value)


class System(ConfigBase):
    """
    An object to hold the configuration for system-related settings.
    """

    def __init__(self):
        """
        Initializes the System configuration object with values from the provided configuration dictionary.
        Args:
            config (Configuration): The configuration object containing the necessary variables.
        """
        super().__init__()
        self.SERVER_HOST = ("SERVER_HOST", str)
        self.SERVER_PORT = ("SERVER_PORT", int)


class LoadEnv:
    """
    An object to load environment variables from .env file and provide them as attributes of the object.
    Methods:
        _get_and_check_variable(key, cast): Helper method to retrieve, check and cast environment variables.
    """

    def __init__(self):
        """
        Initializes the LoadEnv object and loads all necessary environment variables into attributes.
        Args: None
        """
        self.system = System()


env = LoadEnv()

"""
Utilities for feygnn package.
"""
from typing import Dict
import yaml


def load_yaml(path: str) -> Dict:
    """Load YAML file as dict.

    Args:
        path (str): path to YAML file.

    Raises:
        exc: yaml.YAMLError for loading/parsing errors.

    Returns:
        Dict: nested dict representation of parsed YAML file.
    """
    with open(path, "r", encoding="utf-8") as yaml_file:
        try:
            loaded_config = yaml.safe_load(yaml_file)
        except yaml.YAMLError as exc:
            print(exc)
            raise exc
    return loaded_config
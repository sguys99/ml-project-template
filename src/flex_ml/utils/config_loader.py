from typing import Any, Dict

import yaml

from flex_ml.utils.path import DATA_CONFIG_PATH


def load_config(path: str) -> Dict[str, Any]:
    """Configuration loader.

    Description:
        Load configuration yaml file into python dictionary.

    Args:
        path (str): Configuration path.

    Returns:
        (Dict[str, Any]): Dictionary of configuration.
    """
    config = {}
    with open(path, "r", encoding="utf-8") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config


def load_all_configs(data_type="HPMC"):
    """
    Load various configuration files required for data processing and model training.
    Depending on the data_type, different training configuration paths are used.
    """

    configs = {
        "data": load_config(path=DATA_CONFIG_PATH),
    }

    return configs

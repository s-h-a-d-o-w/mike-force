import json
import os
from utils import script_dir

CONFIG_PATH = os.path.join(script_dir(), "config.json")
config = {}
default_config = {"volume": 100, "interval": 0.5, "keep_unmuted": True}


def load_config():
    global config

    if not os.path.exists(CONFIG_PATH):
        config = default_config.copy()
    else:
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)


def save_config():
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f)


load_config()

import json
import os
import tkinter.simpledialog
import threading
import time
from comtypes import CLSCTX_ALL, CoInitialize, CoUninitialize
from ctypes import windll
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from utils import script_dir
from tray import create_tray_icon

# See https://stackoverflow.com/a/43046744/5040168
windll.shcore.SetProcessDpiAwareness(1)

running = True
CONFIG_PATH = os.path.join(script_dir(), "config.json")
config = {}
default_config = {"volume": 100, "interval": 0.5, "keep_unmuted": True}


# Function to stop the execution
def stop_execution():
    global running

    running = False
    mike_thread.join()  # Wait for the mic_thread to finish


# Function to control microphone volume
def force_microphone():
    CoInitialize()

    while running:
        devices = AudioUtilities.GetMicrophone()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)

        # print(config["keep_unmuted"])
        if config["keep_unmuted"]:
            volume.SetMute(0, None)
        volume.SetMasterVolumeLevelScalar(config["volume"] * 0.01, None)

        time.sleep(config["interval"])

    CoUninitialize()


def on_change_interval():
    global config

    tmp = tkinter.simpledialog.askfloat(
        title="Change Interval",
        prompt="How frequently to apply settings (0.1-100 sec.):",
        minvalue=0.1,
        maxvalue=100,
        initialvalue=config["interval"],
    )

    if tmp is not None:
        config["interval"] = tmp
        save_config()


def on_change_volume():
    global config

    tmp = tkinter.simpledialog.askinteger(
        title="Change Volume",
        prompt="Target volume (0-100):",
        minvalue=0,
        maxvalue=100,
        initialvalue=config["volume"],
    )

    if tmp is not None:
        config["volume"] = tmp
        save_config()


def on_change_keep_unmuted(checked):
    global config

    config["keep_unmuted"] = checked


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

# Start the microphone control in a separate thread
mike_thread = threading.Thread(target=force_microphone)
mike_thread.start()

create_tray_icon(
    on_change_keep_unmuted, on_change_interval, on_change_volume, stop_execution
)

import json
import os
import tkinter.simpledialog
import threading
import time
import pystray
from comtypes import CLSCTX_ALL, CoInitialize, CoUninitialize
from ctypes import windll
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from PIL import Image
from utils import local_path, script_dir

# See https://stackoverflow.com/a/43046744/5040168
windll.shcore.SetProcessDpiAwareness(1)

running = True
CONFIG_PATH = os.path.join(script_dir(), "config.json")
config = {}
default_config = {"volume": 100, "interval": 0.5, "keep_unmuted": True}


# Function to stop the execution
def stop_execution(icon):
    global running
    running = False
    mike_thread.join()  # Wait for the mic_thread to finish
    icon.stop()


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


def on_change_keep_unmuted(_, item):
    global config

    config["keep_unmuted"] = not item.checked


# Create the tray icon
def create_tray_icon():
    menu = (
        pystray.MenuItem(
            "Keep Unmuted",
            on_change_keep_unmuted,
            checked=lambda _: config["keep_unmuted"],
        ),
        pystray.MenuItem("Change Target Volume", on_change_volume),
        pystray.MenuItem("Change Interval", on_change_interval),
        pystray.MenuItem("Exit", stop_execution),
    )
    return pystray.Icon("name", Image.open(local_path("icon.ico")), "Mike Force", menu)


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

# See https://pyinstaller.org/en/stable/usage.html#the-pyi-splash-module
try:
    import pyi_splash

    pyi_splash.close()
except:
    pass

# Create and run the tray icon
icon = create_tray_icon()
icon.run()

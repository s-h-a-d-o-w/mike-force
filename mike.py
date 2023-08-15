import threading
import time
import pystray
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from PIL import Image
from comtypes import CoInitialize, CoUninitialize

running = True


# Function to stop the execution
def stop_execution(icon, unused):
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
        volume.SetMute(0, None)
        volume.SetMasterVolumeLevelScalar(1.0, None)
        time.sleep(1)

    CoUninitialize()


# Create the tray icon
def create_tray_icon():
    menu = (pystray.MenuItem("Exit", stop_execution),)
    return pystray.Icon("name", Image.open("icon.png"), "Title", menu)


# Start the microphone control in a separate thread
mike_thread = threading.Thread(target=force_microphone)
mike_thread.start()

# Create and run the tray icon
icon = create_tray_icon()
icon.run()

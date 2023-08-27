<p align="center"><img src="./assets/icon.ico" width="100px" /></p>

# mike-force

Mike Force lurks in a tray icon to help you ensure that the settings for your default microphone on Windows stick (also keep it unmuted if you want to). He e.g. defends the (partially) disabled against attacks by Nuance's dragon. 😉

## Other tools

Inspired by (and some code fragments from): https://github.com/wolfinabox/Windows-Mic-Volume-Locker

But like mentioned, Mike Force also has the ability to keep the microphone unmuted. And running `nircmd` repeatedly didn't seem ideal (laptop battery usage - although the difference is admittedly probably negligible...) to me.

While this tool is larger, actually running it is more efficient (these values were measured using the .exe files, at an interval of 0.1s):

|     | Mike Force | Mic-Volume-Locker |
| -------- | ------- | ------- |
| Processor time  | **0-0.016%**  | ~0.2%  |
| RAM used | ~19 MB  | ~18 MB    |
| Drive space used  | ~73 MB  | **~10 MB**  |

## Release process

The only noteworthy thing here is that after building the release, it should **always** be run. Not just to confirm that changes work as intended but because Windows Defender frequently falsely flags .exe files created with PyInstaller as trojans. If that happens, simply submit the .exe to Microsoft as described in the following article. It'll probably be whitelisted within 24h or so.

https://medium.com/@markhank/how-to-stop-your-python-programs-being-seen-as-malware-bfd7eb407a7

## Architectural decisions

`PyQt` is used because `infi.systray` doesn't support checked tray menu items and with `pystray`, the dialogs that can be triggered only focused correctly the first time that they opened.

(As an added bonus, `PyQt` does things so much faster that a splash screen isn't needed.)

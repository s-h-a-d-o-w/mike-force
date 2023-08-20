<p align="center"><img src="./assets/icon.ico" width="100px" /></p>

# mike-force

Mike Force is here to help you ensure that your microphone settings on Windows stick. He e.g. defends the (partially) disabled against attacks by Nuance's dragon. 😉

## Other tools

Inspired by (and some code fragments from): https://github.com/wolfinabox/Windows-Mic-Volume-Locker

But I also needed the ability to keep the microphone unmuted. Something that wouldn't work well with `infi.systray` (see *Architectural decisions*). And running `nircmd` repeatedly didn't seem ideal (laptop battery usage - although the difference is admittedly probably negligible...) to me.

While this tool is larger, actually running it is more efficient (these values were measured using the .exe files, at an interval of 0.1s):

|     | Mike Force | Mic-Volume-Locker |
| -------- | ------- | ------- |
| Processor time  | **0-0.016%**  | ~0.2%  |
| RAM used | ~19 MB  | ~18 MB    |
| Drive space used  | ~73 MB  | **~10 MB**  |

## Architectural decisions

`PyQt` is used because `infi.systray` doesn't support checked tray menu items and with `pystray`, the dialogs that can be triggered only focused correctly the first time that they opened.

(As an added bonus, `PyQt` does things so much faster that a splash screen isn't needed.)

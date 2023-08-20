# mike-force

Mike Force is here to help you ensure that your microphone settings on Windows stick. He e.g. defends the (partially) disabled against attacks by Nuance's dragon.

Inspired by (and some code fragments from): https://github.com/wolfinabox/Windows-Mic-Volume-Locker

While this is much larger on the hard drive, running it is much more efficient: (Run as .exe @ 0.1s update interval: Mic-Volume-Locker: ~18 MB RAM / ~0.2% Processor time used, Mike Force: ~19 MB RAM / 0-0.016% Processor time used)

| Month    | Mike Force | Mic-Volume-Locker |
| -------- | ------- | ------- |
| Processor time  | 0-0.016%  | ~0.2%  |
| RAM used | ~19 MB  | ~18 MB    |
| Drive space used  | ~73 MB  | ~10 MB  |

## Architectural decisions

`PyQt` is used because even though it results in a huge package, RAM usage isn't that high. `infi.systray`` doesn't support checked tray menu items and with `pystray``, the dialogs that can be triggered only focused correctly the first time that they opened.

(As an added bonus, `PyQt` starts so much faster that a splash screen is needed.)

+++
title = "Launch PS Remote Play with Controller on macOS"
slug = "launch-ps-remote-play-with-controller-on-macos"
date = 2024-06-24 06:52:43-06:00
+++

Here is a simple way to use the "PS" button on a Playstation controller to launch the PS Remote Play app on macOS. This requires [Keyboard Maestro](http://www.keyboardmaestro.com/).

First you must disable the "Press Home button to open Launchpad" setting. This is on by default after you pair a controller to macOS. You can find it in System Settings -> Game Controllers. Turn this off. Now when you press the PS button on your paired controller, nothing should happen.

![](/images/ps-remote-play-controller-settings.png)

Now you can build a simple Macro in Keyboard Maestro. Set the Trigger to "USB Device Key Trigger". Press the PS button, mine shows up as "DUALSHOCK 4 Wireless Controller Button 13".

Now in the Actions for the Macro, choose "Activate a Specific Application" and find "PS Remote Play".
![](/images/ps-remote-play-keyboard-maestro.png)

This same idea could be used to launch your favorite emulator application instead of Remote Play. I tried to find a way to trigger a Macro anytime it detected the controlled was connected via Bluetooth, but it seems like querying Bluetooth devices that way is too energy hungry and isn't allowed. This is the next best thing for me.



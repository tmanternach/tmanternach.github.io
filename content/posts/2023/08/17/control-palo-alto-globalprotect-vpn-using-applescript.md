+++
title = "Control Palo Alto GlobalProtect VPN using AppleScript"
slug = "control-palo-alto-globalprotect-vpn-using-applescript"
date = 2023-08-17 19:35:22-06:00
+++

I know it's a little strange to still be writing AppleScript in 2023, but this was the best way I found to easily connect and disconnect from a GlobalProtect VPN "automatically". I trigger this from a Keyboard Maestro shortcut, you are free to trigger it any way you wish!

This is a simple script that will toggle the connect/disconnect state of GlobalProtect on macOS. Tested with the latest version of GlobalProtect (v6.2.0-89) and macOS Ventura (13.4.1).
```
(*
Toggle GlobalProtect VPN with AppleScript
Tested using macOS Ventura 13.4.1 and GlobalProtect version 6.2.0-89
Written by Trevor Manternach, August 2023.
*)

tell application "System Events" to tell process "GlobalProtect"
  click menu bar item 1 of menu bar 2
  set statusText to name of static text 1 of window 1
  if statusText is "Not Connected" then
    # GlobalProtect is disconnected, so let's connect
    click button "Connect" of window 1
    set entireContents to entire contents of window 1
  else if statusText is "Connected" then
    # GlobalProtect is connected, so let's disconnect
    set windowText to entire contents of window 1
    repeat with theItem in windowText
      if (class of theItem is button) then
        if (value of attribute "AXTitle" of theItem is "Disconnect") then
          # We found a Disconnect button on the main page, let's click it.
          click theItem
          exit repeat
        else
          # We did not find a Disconnect button on the main page, let's hope there is one in the Settings Menu.
          click button "Global Protect Options Menu" of window 1
          click menu item "Disconnect" of menu "Global Protect Options Menu" of button "Global Protect Options Menu" of window 1
          exit repeat
        end if
      end if
    end repeat
  end if
  click menu bar item 1 of menu bar 2
end tell
```
I also have this hosted as a [gist](https://gist.github.com/tmanternach/cbd4c213eab8569e38d6cd021b6255e5) on github. Any changes I make to it are more likely to end up there than here. Comments are welcome over there, too!
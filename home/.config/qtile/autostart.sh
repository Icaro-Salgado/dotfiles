#!/usr/bin/env bash

# festival --tts $HOME/.config/qtile/welcome_msg &
# lxsession &
# picom &
# /usr/bin/emacs --daemon &
# conky -c $HOME/.config/conky/doomone-qtile.conkyrc
# volumeicon &
nm-applet &
xrandr --auto --output HDMI-1-0 --mode 1920x1080 --right-of eDP-1 --primary &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.xwallpaper &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess

from libqtile import bar, widget, hook
from libqtile.config import Screen
from libqtile.utils import guess_terminal

import default_config as current_config

# mod = "mod4"
terminal = guess_terminal()
default_font = "MesloLGLDZ Nerd Font"


if __name__ in ["config", "__main__"]:
    # Constructors
    bindings = current_config.Bindings()

    layouts_module = current_config.Layouts()
    floating_layout_module = current_config.FloatingLayouts()

    # Qtile config variables
    keys = bindings.setup_keys(setup_groups=True)
    mouse = bindings.setup_mouse()

    layouts = layouts_module.setup_layouts()
    floating_layout = floating_layout_module.setup_floating_layouts()

    # Constants
    dgroups_key_binder = None
    dgroups_app_rules = []
    follow_mouse_focus = True
    bring_front_click = False
    cursor_warp = False

    auto_fullscreen = True
    focus_on_window_activation = "smart"
    reconfigure_screens = True

    # If things like steam games want to auto-minimize themselves when losing
    # focus, should we respect this or not?
    auto_minimize = True


widget_defaults = dict(
    font=default_font,
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


def get_widgets():

    widgets = [
        # widget.CurrentLayout(),
        widget.Spacer(length=2),  # type: ignore
        widget.GroupBox(),  # type: ignore
        widget.WindowName(show_state=False),  # type: ignore
        # widget.Prompt(),
        widget.Chord(  # type: ignore
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        # widget.TextBox("default config", name="default"),
        widget.TextBox("", fontsize=20),  # type: ignore
        widget.CPU(format="{load_percent}%"),  # type: ignore
        widget.TextBox("", fontsize=20),  # type: ignore
        widget.BatteryIcon(),  # type: ignore
        widget.Battery(  # type: ignore
            charge_char="",
            discharge_char="",
        ),
        widget.KeyboardLayout(),  # type: ignore
        widget.CheckUpdates(  # type: ignore
            update_interval=1000, distro="Arch_checkupdates", display_format="Updates: {updates}"
        ),
        widget.Systray(),  # type: ignore
        widget.PulseVolume(),  # type: ignore
        widget.Clock(format="%A, %B %d - %H:%M "),  # type: ignore
        widget.QuickExit(),  # type: ignore
    ]

    return widgets


def setup_screens():
    screens = [
        Screen(
            top=bar.Bar(
                get_widgets(),
                24,
                # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ),
        ),
        Screen(
            top=bar.Bar(
                get_widgets(),
                24,
                # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ),
        ),
    ]

    return screens


if __name__ in ["config", "__main__"]:
    screens = setup_screens()


# Start of my configs
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

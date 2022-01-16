# pyright: reportGeneralTypeIssues=false

from libqtile import widget
from . import global_definitions
from . import utils


class Widgets(object):
    def setup_widgets(self):
        widgets = [
            widget.Spacer(length=2),
            widget.GroupBox(),
            widget.WindowName(
                show_state=False, font=global_definitions.default_bold_font, parse_text=utils.parse_window_name
            ),
            widget.Chord(
                chords_colors={
                    "launch": ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.Spacer(length=2),
            # Current layout
            widget.TextBox(text=""),
            widget.CurrentLayout(),
            # RAM
            widget.TextBox(fontsize=14, text=""),
            widget.Memory(
                format="RAM:{MemUsed: .0f}M",
                update_interval=1,
            ),
            widget.Spacer(length=2),
            # Swap
            widget.TextBox(fontsize=14, text=""),
            widget.Memory(
                format="SWAP:{SwapUsed: .0f}M",
                update_interval=1,
            ),
            widget.Spacer(length=2),
            # Thermal Sensoor
            widget.TextBox(text=""),
            widget.ThermalSensor(
                # tag_sensor="CPU",
                threshold=85,
                update_interval=1,
                # foreground_alert=self.color.red,
                # foreground=self.color.white,
            ),
            widget.Spacer(length=2),
            # Battery
            widget.TextBox(text=""),
            widget.Battery(
                format="{char} {percent:0.1%}",
                update_interval=5,
                low_percentage=0.10,
                unknown_char="",
                full_char="",
                charge_char="+",
                discharge_char="-",
                empty_char="",
                # low_foreground=self.color.red,
            ),
            widget.Spacer(length=2),
            # widget.Spacer(length=2),
            widget.TextBox(text="墳"),
            widget.Volume(),
            # # Keyboard layout
            # widget.KeyboardLayout(),
            widget.Spacer(length=2),
            # Check updates
            widget.TextBox(text=""),
            widget.CheckUpdates(update_interval=1000, distro="Arch_checkupdates", display_format="{updates}"),
            widget.Spacer(length=2),
            # Volume
            # widget.PulseVolume(),
            widget.Spacer(length=2),
            # Clock
            widget.TextBox(""),
            widget.Clock(format="%A, %B %d - %H:%M "),
            # Systray
            widget.Systray(),
            # Misc
            # widget.QuickExit(),
        ]

        return widgets

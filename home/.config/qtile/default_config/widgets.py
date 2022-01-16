from libqtile import widget
from . import global_definitions
from . import utils


class Widgets(object):
    def setup_widgets(self):
        widgets = [
            widget.Spacer(length=2),  # type: ignore
            widget.GroupBox(),  # type: ignore
            widget.WindowName(  # type: ignore
                show_state=False, font=global_definitions.default_bold_font, parse_text=utils.parse_window_name
            ),
            widget.Chord(  # type: ignore
                chords_colors={
                    "launch": ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.Spacer(length=2),  # type: ignore
            # RAM
            widget.TextBox(fontsize=14, text=""),  # type: ignore
            widget.Memory(  # type: ignore
                # fmt = "{.0f}",
                format="RAM:{MemUsed: .0f}M",
                update_interval=1,
            ),
            widget.Spacer(length=2),  # type: ignore
            # Swap
            widget.TextBox(fontsize=14, text=""),  # type: ignore
            widget.Memory(  # type: ignore
                format="SWAP:{SwapUsed: .0f}M",
                update_interval=1,
            ),
            widget.Spacer(length=2),  # type: ignore
            # Thermal Sensoor
            widget.TextBox(text=""),  # type: ignore
            widget.ThermalSensor(  # type: ignore
                # tag_sensor="CPU",
                threshold=85,
                update_interval=1,
                # foreground_alert=self.color.red,
                # foreground=self.color.white,
            ),
            widget.Spacer(length=2),  # type: ignore
            # Battery
            widget.TextBox(text=""),  # type: ignore
            widget.Battery(  # type: ignore
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
            widget.Spacer(length=2),  # type: ignore
            # Current layout
            widget.TextBox(text=""),  # type: ignore
            widget.CurrentLayout(),  # type: ignore
            # widget.Spacer(length=2),  # type: ignore
            # # Keyboard layout
            # widget.KeyboardLayout(),  # type: ignore
            widget.Spacer(length=2),  # type: ignore
            # Check updates
            widget.TextBox(text=""),  # type: ignore
            widget.CheckUpdates(  # type: ignore
                update_interval=1000, distro="Arch_checkupdates", display_format="{updates}"
            ),
            widget.Spacer(length=2),  # type: ignore
            # Systray
            widget.Systray(),  # type: ignore
            # Volume
            # widget.PulseVolume(),  # type: ignore
            widget.Spacer(length=2),  # type: ignore
            # Clock
            widget.TextBox(""),  # type: ignore
            widget.Clock(format="%A, %B %d - %H:%M "),  # type: ignore
            # Misc
            # widget.QuickExit(),  # type: ignore
        ]

        return widgets

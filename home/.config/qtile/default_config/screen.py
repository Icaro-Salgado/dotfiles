from libqtile import bar
from libqtile.config import Screen

from .widgets import Widgets


class Screens(object):
    def setup_screen(self):
        widget_list = Widgets().setup_widgets()

        screens = [
            Screen(
                top=bar.Bar(
                    widget_list,
                    24,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                    background="#000000",
                    opacity=0.6,
                ),
            ),
            Screen(
                top=bar.Bar(
                    widget_list,
                    24,
                    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
                ),
            ),
        ]

        return screens
from typing import Literal
from libqtile import bar
from libqtile.config import Screen

from .widgets import Widgets
from .global_definitions import Colors


class Screens(object):
    def __init__(self):
        self.colors = Colors()

        self.widget_list = Widgets().setup_widgets()

    def setup_screen(self):
        screens = [Screen(top=self.get_bar(pos="top"))]
        return screens

    def get_bar(self, pos: Literal["top"]):
        if pos == "top":
            return bar.Bar(
                self.widget_list,
                size=24,
                background=self.colors.primary_bg_color,
                opacity=0.7,
            )
